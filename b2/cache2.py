#coding=utf-8


import time
from threading import RLock
import threading
from collections import OrderedDict
import exceptions2

class CacheItem(object):
    """需要存储的单元
    """
    def __init__(self , value , expired_time):
        """初始化函数
            param:value:object:any thing you want to cache
            param:expired_time:float:set value cache expired time,like 
            return:None
        """
        self.value = value
        self.expired_time = expired_time 
        self.dirty = 0
    
    def __repr__(self):
        return '{"value":%s, "expired_time":%s, "dirty":%s}' % (self.value,self.expired_time,self.dirty)

    def __str__(self):
        return self.__repr__()



class CacheDict(threading.Thread):
    """缓存dict结构体
        Test:
            >>> cache = CacheDict(100)
            >>> cache["test"] = CacheItem("test",time.time() + 30)
            >>> "test" in cache
            >>> cache["test"]
            >>> time.sleep(31)
            >>> "test" in cache 
    """

    def __init__(self,max_len = None,update_rate = 300):
        """缓存结构体
            param:max_len:int:dict max size
            return:None
        """
        super(CacheDict,self).__init__()
        if not isinstance(max_len,int):
            exceptions2.raiseTypeError(max_len) 
        self._cached = OrderedDict() 
        self._update_rate = update_rate
        self._last_update = time.time()
        self.max_len = max_len

    def _now(self):
        return time.time()

    def run(self):
        while True:
            time.sleep(0.1)
            if (self._now() - self._last_update) > self._update_rate:
                now = self._now()
                for key in self._cached.keys():
                    try:
                        if self._cached[key].expired_time <= now:
                            self._cached[key].dirty += 1
                        if self._cached[key].dirty >= 2:
                            del self._cached[key]
                    except KeyError,e:
                        pass
                            
            
    def __contains__(self, key):
        if key in self._cached and self._cached[key].dirty == 0:
            if self._cached[key].expired_time < self._now():
                self._cached[key].dirty += 1 
            else:
                return True 
        return False

    def __getitem__(self, key):
        if key in self._cached and  self._cached[key].dirty == 0:
            if self._cached[key].expired_time > self._now():
                return self._cached[key]
        raise KeyError(key)

    def __setitem__(self ,key ,value):
        if value and isinstance(value , CacheItem):
            if self.max_len and len(self._cached) >= self.max_len:
                self.popitem(last=False)
            self._cached[key] = value
            return 
        raise TypeError

    def __len__(self):
        return min(len(self._cached),self.max_len)

    
    def items(self):
        return [(key,value) for key,value in self._cached().items() if value.dirty == 0 and value.expired_time > self._now()]


    def keys(self):
        return [key for key,value in self._cached.items() if value.dirty == 0 and value.expired_time > self._now() ]

    def get(self,key):
        return self[key]

    def put(self,key,value,expired_time = None):
        self[key] = CacheItem(value,expired_time) 
    
    def __missing__(self,key):
        """implement del  function for cached
        """
        if key in self._cached:
            if self._cached[key].dirty == 0 and self._cached[key].expired_time > self._now():
                self[key].dirty += 1 
                return 
        raise KeyError(key)
