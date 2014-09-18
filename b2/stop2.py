# coding=utf-8


from object2 import Singleton
from collections import defaultdict



class StopStartsWords(object):
    
    def __init__(self, arg):
        super(StopStartsWords, self).__init__()
        self.arg = arg

    def __eq__(self, value):
        if isinstance(value , str):
            value = value.decode('utf-8')
        if isinstance(value , (str , unicode)):
            pass


    def has_key()
