#coding=utf-8

from Queue import Queue
import threading
from datetime import datetime
import time
import file2
import os
import glob
import json
import struct
from collections import deque
from type2 import split_array

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
        if self.__write_file_handle is None or self.__write_file_handle.closed() is True or self.__write_file_count == self.__cache_size:
            cache_file = "%s.%s" % (self.__cache_file_prefix,self.__write_index)
            self.__write_file_handle = open(
                os.path.join(self.__cache_dir ,cache_file),"w")
            self.__write_index += 1
            self.__write_file_count = 0
        self.__write_file_handle.write("%s\n" % obj)
        self.__write_file_count += 1
        if self.__write_file_count >= self.__cache_size:
            self.__write_file_handle.close() 
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


class FifoMemoryQueue(object):
    """In-memory FIFO queue, API compliant with FifoDiskQueue."""

    def __init__(self):
        self.q = deque()
        self.push = self.q.append

    def pop(self):
        q = self.q
        return q.popleft() if q else None

    def close(self):
        pass

    def __len__(self):
        return len(self.q)


class LifoMemoryQueue(FifoMemoryQueue):
    """In-memory LIFO queue, API compliant with LifoDiskQueue."""

    def pop(self):
        q = self.q
        return q.pop() if q else None


class FifoDiskQueue(object):
    """Persistent FIFO queue."""

    szhdr_format = ">L"
    szhdr_size = struct.calcsize(szhdr_format)

    def __init__(self, path, chunksize=100000):
        self.path = path
        if not os.path.exists(path):
            os.makedirs(path)
        self.info = self._loadinfo(chunksize)
        self.chunksize = self.info['chunksize']
        self.headf = self._openchunk(self.info['head'][0], 'ab+')
        self.tailf = self._openchunk(self.info['tail'][0])
        os.lseek(self.tailf.fileno(), self.info['tail'][2], os.SEEK_SET)
    
    def push_array(self , array):
        if array is None:
            raise ValueError("array is none")
        if not isinstance(array,(list,tuple)):
            raise TypeError('Unsupported type: {}'.format(type(array).__name__))
        for item in array:
            if not isinstance(item ,bytes):
                raise TypeError('Array item unsupported type: {}'.format(type(item).__name__))
        hnum, hpos = self.info['head']
        write_array = []
        write_array.append([])
        array_begin_size = min(len(array), self.chunksize - hpos) 
        for item in array[:array_begin_size]:
            write_array[0].append(item) 
        write_array.extend(
            split_array(array[array_begin_size:],self.chunksize)
        )
        
        for index , sub_array in enumerate(write_array):
            content = "".join(["%s%s" % 
                (struct.pack(self.szhdr_format, len(string)), string)     
                for string in sub_array    
            ])
            os.write(self.headf.fileno(),content) 
            hpos += len(sub_array)
            if hpos == self.chunksize:
                hpos = 0
                hnum += 1    
                self.headf.close()
                self.headf = self._openchunk(hnum, 'ab+')
            self.info['size'] += len(sub_array) 
            self.info['head'] = [hnum, hpos]

       
         
    def push(self, string):
        if not isinstance(string, bytes):
            raise TypeError('Unsupported type: {}'.format(type(string).__name__))
        hnum, hpos = self.info['head']
        hpos += 1
        szhdr = struct.pack(self.szhdr_format, len(string))
        os.write(self.headf.fileno(), szhdr + string)
        if hpos == self.chunksize:
            hpos = 0
            hnum += 1
            self.headf.close()
            self.headf = self._openchunk(hnum, 'ab+')
        self.info['size'] += 1
        self.info['head'] = [hnum, hpos]

    def _openchunk(self, number, mode='rb'):
        return open(os.path.join(self.path, 'q%05d' % number), mode)

    def pop(self):
        tnum, tcnt, toffset = self.info['tail']
        if [tnum, tcnt] >= self.info['head']:
            return
        tfd = self.tailf.fileno()
        szhdr = os.read(tfd, self.szhdr_size)
        if not szhdr:
            return
        size, = struct.unpack(self.szhdr_format, szhdr)
        data = os.read(tfd, size)
        tcnt += 1
        toffset += self.szhdr_size + size
        if tcnt == self.chunksize and tnum <= self.info['head'][0]:
            tcnt = toffset = 0
            tnum += 1
            self.tailf.close()
            os.remove(self.tailf.name)
            self.tailf = self._openchunk(tnum)
        self.info['size'] -= 1
        self.info['tail'] = [tnum, tcnt, toffset]
        return data

    def close(self):
        self.headf.close()
        self.tailf.close()
        self._saveinfo(self.info)
        if len(self) == 0:
            self._cleanup()

    def __len__(self):
        return self.info['size']

    def _loadinfo(self, chunksize):
        infopath = self._infopath()
        if os.path.exists(infopath):
            with open(infopath) as f:
                info = json.load(f)
        else:
            info = {
                'chunksize': chunksize,
                'size': 0,
                'tail': [0, 0, 0],
                'head': [0, 0],
            }
        return info

    def _saveinfo(self, info):
        with open(self._infopath(), 'w') as f:
            json.dump(info, f)

    def _infopath(self):
        return os.path.join(self.path, 'info.json')

    def _cleanup(self):
        for x in glob.glob(os.path.join(self.path, 'q*')):
            os.remove(x)
        os.remove(os.path.join(self.path, 'info.json'))
        if not os.listdir(self.path):
            os.rmdir(self.path)



class LifoDiskQueue(object):
    """Persistent LIFO queue."""

    SIZE_FORMAT = ">L"
    SIZE_SIZE = struct.calcsize(SIZE_FORMAT)

    def __init__(self, path):
        self.path = path
        if os.path.exists(path):
            self.f = open(path, 'rb+')
            qsize = self.f.read(self.SIZE_SIZE)
            self.size, = struct.unpack(self.SIZE_FORMAT, qsize)
            self.f.seek(0, os.SEEK_END)
        else:
            self.f = open(path, 'wb+')
            self.f.write(struct.pack(self.SIZE_FORMAT, 0))
            self.size = 0

    def push(self, string):
        if not isinstance(string, bytes):
            raise TypeError('Unsupported type: {}'.format(type(string).__name__))
        self.f.write(string)
        ssize = struct.pack(self.SIZE_FORMAT, len(string))
        self.f.write(ssize)
        self.size += 1

    def pop(self):
        if not self.size:
            return
        self.f.seek(-self.SIZE_SIZE, os.SEEK_END)
        size, = struct.unpack(self.SIZE_FORMAT, self.f.read())
        self.f.seek(-size-self.SIZE_SIZE, os.SEEK_END)
        data = self.f.read(size)
        self.f.seek(-size, os.SEEK_CUR)
        self.f.truncate()
        self.size -= 1
        return data

    def close(self):
        if self.size:
            self.f.seek(0)
            self.f.write(struct.pack(self.SIZE_FORMAT, self.size))
        self.f.close()
        if not self.size:
            os.remove(self.path)

    def __len__(self):
        return self.size


if __name__ == "__main__":
    f = RateHourFileCacheQueue(hour_rate = 2000)
    for i in range(1231):
        f.put(i)
    for i in range(1239):
        print f.get()
