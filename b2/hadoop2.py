# coding=utf-8


import sys
from random import randint

class DefaultDict(dict):

    def __init__(self, default_factory=None, *arg, **kw):
        super(DefaultDict, self).__init__(*arg, **kw)
        if default_factory == None:
            self.__default_factory = int
        else:
            if not callable(default_factory):
                raise TypeError, 'default factory isn\'t callable %s' % (
                    default_factory)

    def __missing__(self, key):
        if key:
            return self.__default_factory()

    def __getitem__(self, key):
        try:
            return dict.__getitem__(self, key)
        except KeyError:
            return self.__missing__(key)


class Hadoop2(object):

    def __init__(self, split_char=' '):
        self.split_char = ' '
        self.__start()

    def split(self, line):
        if line and len(line) > 0:
            return line.split(split_char)

    def __start(self):
        for line in sys.stdin:
            line = line.strip().split(self.split_char)
            self.do(line)

    def do(self, lineArray):
        print lineArray


def java_string_hashcode(s):
    h = 0
    for c in s:
        h = (31 * h + ord(c)) & 0xFFFFFFFF
    return ((h + 0x80000000) & 0xFFFFFFFF) - 0x80000000

def get_key_part(key , part_num ):
    '''
    应用场景 ：
        mapreduce计算完毕 ， 非单独map计算方式 ；
        reduce 根据 hash(key) % reduce_num 方式计算每条key放入的part
    key ：
        mapreduce reduce key
    part_num:
        reduce number 
    '''
    return java_string_hashcode(key) % part_num





if __name__ == '__main__':
    h = Hadoop2()
    print int()
