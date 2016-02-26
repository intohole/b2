#coding=utf-8


import threading 
import time
import Queue
import sys


class Command(object):


    def __init__( self , func , *argv , **kw ):
        if func and ( callable(func) or isinstance(func , basestring)):
            self.func = func 
        else:
            raise TypeError
        self.argv = argv 
        self.kw = kw 



class Worker(threading.Thread):


    def __init__(self , queue , sleep = None):
        super(Worker, self).__init__()
        self.tasks = queue 
        self.setDaemon(True)
        self.status = "stop"
        self.running_flag = True

    def run(self):
        while self.running_flag:
            task = self.tasks.get()
            self.status = "running"
            if isinstance(task.func , basestring) and task.func.lower() == "kill":
                break
            try:
                task.func(*task.argv , **task.kw)
            except Exception,e:
                print e
        self.status = "finish"
    
    def stop(self):
        self.running_flag = False


class ThreadPool(object):

    def __init__(self , pool_size , sleep = None , queue_rate = 4):
        """简易线程池
            Test:
                >>> threads = ThreadPool(10)
                >>> threads.start()
                >>> x = lambda x: print x ;
                >>> threads.add_command(x, *argv , **kw)
                >>> threads.join()
        """
        self.queue = Queue.Queue()
        self.pool_size_range = xrange(pool_size)
        self.threads = [Worker(self.queue , sleep) for i in xrange(pool_size)]
        self.pool_size = pool_size

    def start(self):
        """线程池中所有线程启动
            params:
                None
            return 
                None
            raise 
                None
        """
        for thread in self.threads:
            thread.start()
    
    def wait(self):
        for thread in self.threads:
            thread.join()

    def add_command(self , func , *argv , **kw):
        self.queue.put(Command(func , *argv , **kw))
    
    def insert(self , command):
        self.queue.put(command)

    def add_worker(self , sleep = None):
        self.add_worker(self.queue , sleep)
    
    def kill(self  , thread = None ):
        if thread is None:
            for thread in threads:
                thread.stop()
            del self.threads[:]
        elif thread in self.pool_size_range:
            self.threads[thread].stop()
            self.pool_size -= 1 
            del self.threads[thread]
            self.pool_size_range = xrange(self.pool_size)
        else:
            raise ValueError

class CommandOrderThread(object):
   
    pass
if __name__ == "__main__":


    threads = ThreadPool(10)
    def func(*argv , **kw):
        n = kw.get("n" ,-1 )
        print "call me"
        time.sleep(1)
    for i in range(100):
        sys.stdout.write("add command \n") 
        threads.add_command(func , *[] , **{"n" : i})
    for i in range(10):
        threads.add_command("kill" , *[] , **{"n" : i})
    threads.start()
    print "good"
