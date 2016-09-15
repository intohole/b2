#coding=utf-8


import subprocess

class PipeCommandItem(object):


    def __init__(self , command ,shell = False):
        if command and isinstance(command,(basestring ,tuple ,list)):
            self.command = command
        else:
            raise TypeError
        self.shell = shell

class PipeCommand(object):


    def __init__(self):
        self._commands = []

    def add(self,command):
        pass
def _check_pipe_items(pipe_commands):
    if pipe_commands and hasattr(pipe_commands):
        for pipe_command in pipe_commans:
            if isinstance(pipe_command,PipeCommandItem) is False:
                raise TypeError
        return
    raise ValueError

def run_pipe(pipe_commands):
    self._check_pipe_items(pipe_commands)
    pipes = []
    for pipe_command in pipe_commands:
        stdin = subprocess.PIPE.stdin
        if len(pipes) != 0:
            stdin = pipes[-1]
        pipes.append(subprocess.Popen(pipe_command.command,shell=pipe_command.shell,stdin = stdin,stdout=subprocess.PIPE.stdout))
    pipes[-1].communicate()
