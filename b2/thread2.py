# coding=utf-8


"""
    thread pool 实现
"""

import sys
if sys.version_info[0] > 2:
    import Queue
else:
    import Queue as queue
from collections import deque
import threading

class Worker(threading.Thread):
    """Thread executing tasks from a given tasks queue"""
    def __init__(self, tasks, send_item, num_threads):
        threading.Thread.__init__(self)
        self.send_item = send_item
        self.tasks = tasks
        self.num_threads = num_threads
        self.daemon = True
        self.start()

    def run(self):
        while True:
            func, args, kargs = self.tasks.get()
            if self.send_item == True:
                try:
                    item = self.num_threads.popleft()
                    func(item, *args, **kargs)
                except Exception as e:
                    print(e)
            if self.send_item == False:
                try:
                    func(*args, **kargs)
                except Exception as e:
                    print(e)
            self.tasks.task_done()
            if self.send_item == True:
                self.num_threads.append(item)

class ThreadPool:
    """Pool of threads consuming tasks from a queue"""
    def __init__(self, num_threads, send_item=False, min_pool=0, max_pool=0, queue_type='fifo'):
        self.priority_queue = False
        min_pool = int(round(min_pool))
        max_pool = int(round(max_pool))
        if max_pool != 0:
            if min_pool > max_pool:
                min_pool = max_pool
        iterable_list = [dict, tuple, set]
        number_list = [float, int]
        """Item in list is sent as first argument to function"""
        if type(num_threads) in iterable_list:
            num_threads = deque(num_threads)
        elif type(num_threads) == str:
            num_threads = deque([num_threads])
        elif type(num_threads) in number_list:
            if num_threads < 1:
                num_threads = 1
            num_threads = deque(list(range(int(num_threads))))
        elif type(num_threads) is bool:
            if num_threads == False:
                num_threads = deque([False])
            elif num_threads == True:
                num_threads = deque([True])
        if type(num_threads) != deque:
            try: 
                iter(num_threads)
                num_threads = deque(num_threads)
            except TypeError as _:
                print(num_threads, ' is not iterable')
                raise
        pool_size = len(num_threads)
        if pool_size < min_pool and min_pool != 0:
            multiply_list = int(round((float(min_pool) / pool_size) + 0.5))
            pool_size = int(min_pool)
            num_threads = deque(list(num_threads))
            new_num_threads = deque()
            for _ in range(multiply_list):
                for i in num_threads:
                    new_num_threads.append(i)
            num_threads = new_num_threads
        if pool_size > max_pool and max_pool != 0:
            pool_size = int(max_pool)
        if queue_type == 'fifo':
            self.tasks = queue.Queue(pool_size)
        elif queue_type == 'lifo':
            self.tasks = queue.LifoQueue(pool_size)
        for _ in range(pool_size):
            Worker(self.tasks, send_item, num_threads)
        self.pool_size = pool_size

    def add_task(self, func, *args, **kargs):
        """Add a task to the queue"""
        self.tasks.put((func, args, kargs))
    
    def wait_completion(self):
        """Wait for completion of all the tasks in the queue"""
        self.tasks.join()
