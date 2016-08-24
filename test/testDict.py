#coding=utf-8

import threading

class DataStamp(object):

    def __init__(self , timestamp , key):
        self.timestamp = timestamp 
        self.key = key 

class StampList(object):
    
    def __init__(self):
        self.l = []
    
    def add(self , datastamp):
        self.l.insert() 
    
class TairDict(threading.Thread,dict):

    def __init__(self):
        super(TairDict,self).__init__()
        self.start() 

    def run(self):
        print "i'm run "

    def __setitem__(self, key , value):
        if key in self:
            pass
    
    def put(self , key , value , endTime = None):
        pass
 
    def __getitem__(self , key):
        if key in self:
            value = super(TairDict , self).__getitem__(key) 
            if value.timestamp > long(time.time()):
                return None
            else:
                return value.value 
        else:
            return None 
    
    def get(self , key):
        pass
if __name__ == "__main__":
    t = TairDict()
