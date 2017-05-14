#coding=utf-8


import time
from threading import RLock
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
        self.expired_time = time.time() + expired_time
        self._lastUsedTime = time.time()

    def update(self):
        self._lastUsedTime = time.time()

    def expired(self):
        return time.time() > self.expired_time

class CacheDict(OrderedDict):
    """缓存dict结构体
        Test:
            >>> cache = CacheDict()
    """

    def __init__(self , max_len , max_age_seconds):
        """缓存结构体
            param:max_len:int:dict max size
            param:max_age_seconds:float:value expire time max value;
            return:None
        """
        super(CacheDict,self).__init__()
        if not isinstance(max_len,int):
            exceptions2.raiseTypeError(max_len) 
        if not isinstance(max_age_seconds,(float,int)):
            exceptions2.raiseTypeError(max_age_seconds)
        self.max_len = max_len
        self.max_age_seconds = max_age_seconds
        self._lock = RLock()



    def __contains__(self, key):
        try:
            with self._lock:
                if super(CacheDict,self).__contains__(key):
                    item = super(CacheDict,self).__getitem__(key)
                    if item.expired():
                        del self[key]
                    else:
                        return True
        except KeyError:
            pass
        return False

    def __getitem__(self, key):
        with self._lock:
            item = super(CacheDict,self).__getitem__(key)
            if item.expired():
                self.update()
                return item
            else:
                del self[key]
                raise KeyError(key)

    def __setitem__(self ,key ,value):
        if value and isinstance(value , CacheItem):
            with self._lock:
                if len(self) >= self.max_len:
                    self.popitem(last=False)
                super(CacheDict,self).__setitem__(key , value)
                return
        raise TypeError
