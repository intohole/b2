#!/usr/bin/env python
# encoding: utf8
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
# Author: huangkuan<huangkuan@baidu.com>
# Created on 2013-06-06 13:58:46

import os
import re
import sys
import shlex
import pipes
import inspect
import logging
import getpass
import threading
from datetime import datetime

try:
    sorted
except NameError:
    def sorted(l):
        l = list(l)
        l.sort()
        return l

try:
    from subprocess import Popen
    def popen(cmd, stdin=None, stdout=None, wait=False):
        if stdin is None:
            _stdin = stdin = open('/dev/null', 'rb')
        if isinstance(stdin, int):
            stdin = os.fdopen(stdin, 'rb')
        if stdout is None:
            _stdout = stdout = open('/dev/null', 'wb')
        if isinstance(stdout, int):
            stdout = os.fdopen(stdout, 'wb')
        pipe = Popen(cmd, shell=True, close_fds=True, stdin=stdin, stdout=stdout)
        if wait:
            return pipe.wait()
        else:
            return pipe.pid
except ImportError:
    import gc
    try:
        MAXFD = os.sysconf('SC_OPEN_MAX')
    except:
        MAXFD = 256
    def popen(cmd, stdin=None, stdout=None, wait=False):
        if stdin is None:
            _stdin = stdin = open('/dev/null', 'rb')
        if not isinstance(stdin, int):
            stdin = stdin.fileno()
        if stdout is None:
            _stdout = stdout = open('/dev/null', 'wb')
        if not isinstance(stdout, int):
            stdout = stdout.fileno()

        # exec
        if isinstance(cmd, basestring):
            cmd = [cmd]
        else:
            cmd = list(cmd)
        cmd = ["/bin/sh", "-c"]+cmd

        gc_was_enabled = gc.isenabled()
        gc.disable()
        try:
            pid = os.fork()
        except:
            if gc_was_enabled:
                gc.enable()
            raise
        if pid == 0:
            if stdout == 0:
                stdout = os.dup(stdout)

            os.dup2(stdin, 0)
            os.dup2(stdout, 1)

            if hasattr(os, 'closerange'):
                os.closerange(3, MAXFD)
            else:
                for i in xrange(3, MAXFD):
                    try:
                        os.close(i)
                    except:
                        pass

            os.execvp(cmd[0], cmd)
            os._exit(255)
        # parent
        if gc_was_enabled:
            gc.enable()

        if stdin is not None and stdin != 0:
            os.close(stdin)
        if stdout is not None and stdout != 1:
            os.close(stdout)

        if wait:
            pid, sts = os.waitpid(pid, 0)
            if os.WIFSIGNALED(sts):
                return os.WTERMSIG(sts)
            elif os.WIFEXITED(sts):
                return os.WEXITSTATUS(sts)

        return pid

class HadoopRun:
    which_python = 'python'
    hadoop_tmp_path = 'hdfs://xxx/%s_%s_%s' % (
            str(datetime.now()).replace(' ', '_').replace(':', '_'), os.uname()[1], os.getpid())
    default_jobconf = {
                'map.output.key.field.separator': '\t',
                'stream.map.output.field.separator': '\t',
                'stream.reduce.input.field.separator': '\t',
                'stream.reduce.output.field.separator': '\t',
                'mapred.textoutputformat.separator': '\t',
                'mapred.textoutputformat.ignoreseparator': 'true',
                'mapred.reduce.slowstart.completed.maps': '1.0',
            }
    FS = None
    OFS = '\t'
    ORS = '\n'

    def __init__(self,
                 mapper = "cat",
                 reducer = None,
                 combiner = None,
                 partitioner = None,
                 num_reduce_tasks = None,
                 input = None,
                 inputformat = None,
                 output = None,
                 outputformat = None,
                 files = [],
                 jobconf = {},
                 cmdenv = {},
                 jobname = None,
                 cmdline = "",
                 hadoop_home = os.getenv('HADOOP_HOME'),
                 **kwargs):
        self.mapper = mapper
        self.mapper_cmd = None
        self.reducer = reducer
        self.reducer_cmd = None
        self.combiner = combiner
        self.partitioner = partitioner
        self.num_reduce_tasks = num_reduce_tasks
        self.input = input
        self.inputformat = inputformat
        self.output = output
        self.outputformat = outputformat
        self.files = files
        self.jobconf = dict(self.default_jobconf)
        self.jobconf.update(jobconf)
        self.cmdenv = cmdenv
        self.jobname = jobname
        self.cmdline = cmdline
        self.hadoop_home = hadoop_home
        self.__dict__.update(kwargs)

        self.check_config()

    def check_config(self):
        if self.jobconf.get('num.key.fields.for.partition', 1) != self.jobconf.get('stream.num.map.output.key.fields', 1) and not self.partitioner:
            raise Exception('num.key.fields.for.partition is differ from stream.num.map.output.key.fields; need set partitioner as "org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner"')

    def run(self, command=(len(sys.argv)>1 and sys.argv[1] or None),
                  arg1=(len(sys.argv)>2 and sys.argv[2] or None)):
        if command == None:
            os.environ.update(self.cmdenv)
            cmds = []

            if self.input is None:
                self.input = sys.stdin
            if isinstance(self.input, basestring):
                if self.input.startswith('hdfs://'):
                    self.input = sys.stdin
                else:
                    cmds.append('cat %s' % self.input)
                    self.input = sys.stdin
            else:
                hdfs = False
                for each in self.input:
                    if each.startswith('hdfs://'):
                        hdfs = True
                if hdfs:
                    self.input = sys.stdin
                else:
                    cmds.append('cat %s' % ' '.join(self.input))
                    self.input = sys.stdin

            if self.output is None or self.output.startswith('hdfs://'):
                self.output = sys.stdout
            else:
                self.output = open(self.output, 'w')

            cmds.append(self.mapper)

            if self.combiner:
                cmds.append('sort')
                cmds.append(self.combiner)
                
            if self.reducer:
                cmds.append('sort')
                cmds.append(self.reducer)

            sys.exit(self._run(cmds, input=self.input, output=self.output))
        elif command == 'mapper':
            sys.exit(self._run(self.mapper, input=sys.stdin, output=sys.stdout))
        elif command == 'combiner':
            sys.exit(self._run(self.combiner, input=sys.stdin, output=sys.stdout))
        elif command == 'reducer':
            if self.reducer:
                sys.exit(self._run(self.reducer, input=sys.stdin, output=sys.stdout))
            else:
                sys.exit(self._run('cat', input=sys.stdin, output=sys.stdout))
        elif command == 'hadoop':
            hadoop_debug = arg1 == 'debug'
            cmd = []
            cmd_end = []
            opt = []
            need_clear_tmp_path = False

            #input 
            if self.input and isinstance(self.input, basestring):
                self.input = [self.input, ]
            elif not self.input:
                raise Exception('no input')

            for each in self.input:
                if each.startswith('hdfs://'):
                    opt.append('-input %s' % pipes.quote(each[6:]))
                else:
                    if not hadoop_debug and popen('ls %s' % each, wait=True) != 0:
                        raise Exception('input path %s not exists!' % each)
                    if not need_clear_tmp_path:
                        cmd.append('%s/bin/hadoop fs -rmr %s || sh -c "exit 0"' % (self.hadoop_home , 
                            self.hadoop_tmp_path[6:]+'/input'))
                        cmd.append('%s/bin/hadoop fs -mkdir %s' % (self.hadoop_home , 
                            self.hadoop_tmp_path[6:]+'/input'))
                        opt.append('-input %s' % pipes.quote(self.hadoop_tmp_path[6:]+'/input/*'))

                    cmd.append('%s/bin/hadoop fs -put %s %s' % (self.hadoop_home , 
                        each, self.hadoop_tmp_path[6:]+'/input/'))

                    if not need_clear_tmp_path:
                        cmd_end.append('%s/bin/hadoop fs -rmr %s' % (self.hadoop_home , 
                            self.hadoop_tmp_path[6:]+'/input'))

                    need_clear_tmp_path = True

            #inputformat
            if self.inputformat:
                opt.append('-inputformat %s' % pipes.quote(self.inputformat))

            #output
            if self.output and self.output.startswith('hdfs://'):
                cmd.append('%s/bin/hadoop fs -rmr %s || sh -c "exit 0"' % (self.hadoop_home , pipes.quote(self.output[6:])))
                opt.append('-output %s' % pipes.quote(self.output[6:]))
            elif isinstance(self.output, basestring) or self.output is None:
                cmd.append('%s/bin/hadoop fs -rmr %s || sh -c "exit 0"' % (self.hadoop_home ,
                    self.hadoop_tmp_path[6:]+'/output'))
                need_clear_tmp_path = True

                opt.append('-output %s' % pipes.quote(self.hadoop_tmp_path[6:]+'/output'))

                if self.output is None:
                    pass
                elif os.path.isdir(self.output):
                    cmd_end.append('%s/bin/hadoop fs -get %s %s' % (self.hadoop_home , 
                        self.hadoop_tmp_path[6:]+'/output/*', self.output))
                elif os.path.isdir(os.path.dirname(self.output)) or hadoop_debug:
                    cmd_end.append('rm %s || sh -c "exit 0"' % self.output)
                    cmd_end.append('%s/bin/hadoop fs -getmerge %s %s' % (self.hadoop_home , 
                        self.hadoop_tmp_path[6:]+'/output/', self.output))
                else:
                    raise Exception('output path not exists!')

                cmd_end.append('%s/bin/hadoop fs -rmr %s' % (self.hadoop_home ,
                    self.hadoop_tmp_path[6:]+'/output'))
            else:
                raise Exception('no output')

            #outputformat
            if self.outputformat:
                opt.append('-outputformat %s' % pipes.quote(self.outputformat))

            #file
            files = {}
            for filepath in self.files:
                files[filepath] = 1
            frame = inspect.currentframe()
            origin_file = None
            while frame:
                origin_file = inspect.getframeinfo(frame)[0]
                files[origin_file] = 1
                frame = frame.f_back
            for filepath in files:
                opt.append('-file %s' % pipes.quote(filepath))

            #mapper
            if self.mapper_cmd:
                mapper_cmd = pipes.quote(self.mapper_cmd)
            elif isinstance(self.mapper, basestring):
                mapper_cmd = pipes.quote(self.mapper)
            elif not self.mapper:
                raise Exception('no mapper!')
            else:
                mapper_cmd = '%s %s mapper' % (self.which_python, os.path.basename(origin_file))

            #combiner
            if isinstance(self.combiner, basestring):
                mapper_cmd += ' | sort | %s' % self.combiner
            elif self.combiner:
                mapper_cmd += ' | sort | %s %s combiner' % (self.which_python, os.path.basename(origin_file))

            if mapper_cmd == 'cat':
                #opt.append('-mapper org.apache.hadoop.mapred.lib.IdentityMapper')
                opt.append('-mapper "%s"' % mapper_cmd)
            else:
                opt.append('-mapper "%s"' % mapper_cmd)

            #reducer
            if self.reducer_cmd:
                opt.append('-reducer %s' % pipes.quote(self.reducer_cmd))
            elif isinstance(self.reducer, basestring):
                opt.append('-reducer %s' % pipes.quote(self.reducer))
            elif self.reducer:
                opt.append('-reducer "%s %s reducer"' % (self.which_python, os.path.basename(origin_file)))
            else:
                opt.append('-reducer "NONE"')

            # partitioner
            if self.partitioner:
                opt.append('-partitioner %s' % pipes.quote(self.partitioner))

            # numReduceTasks
            if self.num_reduce_tasks:
                opt.append('-numReduceTasks %s' % self.num_reduce_tasks)

            # jobname
            if 'mapred.job.name' not in self.jobconf and self.jobname is None:
                self.jobname = 'hadoop_py %s %s@%s#%s' % (os.path.basename(origin_file),
                                               getpass.getuser(), os.uname()[1], os.getpid())
            self.jobconf['mapred.job.name'] = self.jobname

            # jobconf
            if self.jobconf:
                for k, v in self.jobconf.items():
                    opt.append('-jobconf %s=%s' % (k, pipes.quote(str(v))))

            # cmdenv
            if self.cmdenv:
                for k, v in self.cmdenv.items():
                    opt.append('-cmdenv %s=%s' % (k, pipes.quote(str(v))))

            # other cmdlines
            if self.cmdline:
                opt.append(self.cmdline)

            if need_clear_tmp_path:
                cmd_end.append('%s/bin/hadoop fs -rmr %s' % (self.hadoop_home , 
                    self.hadoop_tmp_path[6:]))

            if hadoop_debug:
                cmd.append(('%s/bin/hadoop streaming ' % self.hadoop_home ) +' \\\n\t\t\t\t'.join(opt))
            else:
                cmd.append(('%s/bin/hadoop streaming ' % self.hadoop_home )+' '.join(opt))

            cmd += cmd_end

            if hadoop_debug:
                for each in cmd:
                    print each
            else:
                for each in cmd:
                    print each
                    ret = popen(each, wait=True)
                    if ret != 0:
                        raise Exception('cmd [%s] exec failed: %d' % (each, ret))
        else:
            raise Exception("Command not supported.")

    def _run(self, func, input, output, wait=True):
        print >> sys.stderr, "hadoop.py run: ", func, input, output, wait
        if isinstance(func, basestring):
            return self.run_cmd(func, input, output, wait=wait)
        elif callable(func):
            return self.run_func(func, input, output, wait=wait)
        elif isinstance(func, tuple) or isinstance(func, list):
            for each in func[:-1]:
                r, w = os.pipe()
                self._run(each, input, w, wait=False)
                input = r
            return self._run(func[-1], input, output, wait=True)
        else:
            raise Exception('unknow func format')

    def run_cmd(self, func, input, output, wait=True):
        return popen(func, input, output, wait=wait)

    def run_func(self, func, input, output, wait=True):
        if not wait:
            td = threading.Thread(target=self.run_func, args=(func, input, output, True))
            td.daemon = True
            td.start()
            return

        if isinstance(input, int):
            input = os.fdopen(input, 'r')
        if isinstance(output, int):
            output = os.fdopen(output, 'w')

        try:
            args, has_args, _, values = inspect.getargspec(func)
        except TypeError:
            args, has_args, _, values = inspect.getargspec(func.__call__)
            args = args[1:]
        min_parts = len(args or []) - 1 - len(values or [])
        max_parts = has_args and 998 or len(args or []) - 1

        def _output(ret):
            if isinstance(ret, basestring):
                output.write(str(ret))
                output.write(self.ORS)
            else:
                output.write(self.OFS.join(map(str, ret)))
                output.write(self.ORS)

        if hasattr(func, '__begin__') and callable(getattr(func, '__begin__')):
            for ret in func.__begin__() or []:
                _output(ret)

        for line in input:
            line = line.rstrip()
            if not line:
                continue
            parts = line.split(self.FS)
            try:
                for ret in func(line, *parts):
                    _output(ret)
            except:
                print >> sys.stderr, "line error:", line
                raise

        if hasattr(func, '__end__') and callable(getattr(func, '__end__')):
            for ret in func.__end__() or []:
                _output(ret)
        return 0

#helper
def run(*args, **kwargs):
    return HadoopRun(*args, **kwargs).run()

def load_sh(path):
    r, w = os.pipe()
    popen('env -i /bin/sh -c "set -o posix; set"', stdin=None, stdout=w, wait=False)
    read = os.fdopen(r, 'r').read()
    config_orig = shlex.split(read)

    r, w = os.pipe()
    popen('env -i /bin/sh -c "source %s > /dev/null; set -o posix; set"' % pipes.quote(path), stdin=None, stdout=w, wait=False)
    read = os.fdopen(r, 'r').read()
    config = shlex.split(read)
    result = dict()
    for line in config:
        if line in config_orig:
            continue
        k, v = line.strip().split('=', 1)
        result[k] = v
    return result
    
def update_counter(group, counter, amount):
    print >> sys.stderr, "reporter:counter:%s,%s,%s" % (group, counter, amount)

def update_status(message):
    print >> sys.stderr, "reporter:status:%s" % message
