#coding=utf-8

from Queue import Queue
import threading
from datetime import datetime
import time
import file2
import os

class RateHourQueue(Queue):

    def __init__(self, *argv , **kw):
        Queue.__init__(self,*argv)
        self.__count = 0
        self.limit = kw.get("hour_rate",300)
        self.__time = self.get_current_hour()
        self.lock = threading.Lock()

    def get_current_hour(self):
        now = datetime.now()
        return now.hour

    def get(self):
        with self.lock:
            while True:
                cur_time = self.get_current_hour()
                if self.__time != cur_time:
                    self.__time = cur_time
                    self.__count = 1
                    return Queue.get(self)
                if self.__count >= self.limit:
                    time.sleep(5)
                    continue
                if self.__count < self.limit:
                    self.__count += 1
                    return Queue.get(self)


class FileCacheQueue(Queue):


    def __init__(self,*argv,**kw):
        Queue.__init__(self)
        self.lock = threading.Lock()
        self.__cache_size = kw.get("cache_size" , 1000)
        self.__cache_dir = kw.get("cache_dir", "./.cache_dir/")
        self.__cache_file_prefix = kw.get("cache_prefix" ,"cache")
        file2.mkdir_p(self.__cache_dir)
        self.__read_index = 0
        self.__write_index = 0
        self.__write_file_count = 0
        self.__write_file_handle = None
        self.__write_count = 0
        self.__read_count = 0

    def _write_to_file(self , obj):
        if self.__write_file_handle is None or self.__write_file_count == self.__cache_size:
            cache_file = "%s.%s" % (self.__cache_file_prefix,self.__write_index)
            self.__write_file_handle = open(
                os.path.join(self.__cache_dir ,cache_file),"w")
            self.__write_index += 1
            self.__write_file_count = 0
        self.__write_file_handle.write("%s\n" % obj)
        self.__write_file_count += 1
        self.__write_count += 1


    def _load_file_cache(self):
        if self.__read_index > self.__write_index:
            return # no file cache , so return
        cache_file = "%s.%s" % (self.__cache_file_prefix,self.__read_index)
        cache_path = os.path.join(self.__cache_dir , cache_file)
        if os.path.exists(cache_path):
            # if write file not over cache size , close write file hadnle , and
            # set file handle None
            if self.__write_file_count < self.__cache_size or self.__read_index == self.__write_index:
                if self.__write_file_handle is not None:
                    self.__write_file_handle.close()
                    self.__write_file_handle = None

            with open(cache_path) as f:
                for line in f:
                    Queue.put(self , line.rstrip())
                    self.__read_count += 1
            self.__read_index += 1

    def get(self):
        with self.lock:
            if self.empty() is True:
                self._load_file_cache()
                return Queue.get(self , block = 0)
            return Queue.get(self , block = 0)

    def put(self,obj):
        with self.lock:
            if self.qsize() >= self.__cache_size:
                self._write_to_file(obj)
            else:
                Queue.put(self ,obj)



    def empty(self):
        with self.lock:
            if Queue.empty(self)  is True:
                if self.__read_count < self.__write_count:
                    return False
                return True
            return False




class RateHourFileCacheQueue(FileCacheQueue):

    def __init__(self, *argv , **kw):
        FileCacheQueue.__init__(self,*argv,**kw)
        self.__count = 0
        self.limit = kw.get("hour_rate",300)
        self.__time = self.get_current_hour()
        self._lock = threading.Lock()

    def get_current_hour(self):
        now = datetime.now()
        return now.hour

    def get(self):
        with self._lock:
            while True:
                cur_time = self.get_current_hour()
                if self.__time != cur_time:
                    self.__time = cur_time
                    self.__count = 1
                    return FileCacheQueue.get(self)
                if self.__count >= self.limit:
                    time.sleep(5)
                    continue
                if self.__count < self.limit:
                    self.__count += 1
                    return FileCacheQueue.get(self)


if __name__ == "__main__":
    f = RateHourFileCacheQueue(hour_rate = 2000)
    for i in range(1231):
        f.put(i)
    for i in range(1239):
        print f.get()
