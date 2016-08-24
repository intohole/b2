#coding=utf-8


import time
from threading import RLock
from collections import OrderedDict

class CacheItem(object):


    def __init__(self , value , expired_time):
        self.value = value
        self.expired_time = time.time() + expired_time
        self._lastUsedTime = time.time()

    def update(self):
        self._lastUsedTime = time.time()

    def expired(self):
        return time.time() > self.expired_time

class CacheDict(OrderedDict):


    def __init__(self , max_len , max_age_seconds):
        super(CacheDict,self).__init__()
        self.max_len = max_len
        self.max_age_seconds = max_age_seconds
        self.lock = RLock()



    def __contains__(self, key):
        try:
            with self.lock:
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
        with self.lock:
            item = super(CacheDict,self).__getitem__(key)
            if item.expired():
                self.update()
                return item
            else:
                del self[key]
                raise KeyError(key)

    def __setitem__(self ,key ,value):
        if value and isinstance(value , CacheItem):
            with self.lock:
                if len(self) >= self.max_len:
                    self.popitem(last=False)
                super(CacheDict,self).__setitem__(key , value)
                return
        raise TypeError




