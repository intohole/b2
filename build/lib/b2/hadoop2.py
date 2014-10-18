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


def reservoir_sample(sample_num , k = 1):
    data = []
    idx = 0 
    for line in sys.stdin:
        line = line.strip()
        if idx < sample_num:
            data.append(line)
        else:
            sample = randint( 0 , idx  )
            if sample < sample_num:
                data[sample] = line
        idx += 1
    for line in data:
        print '\t'.join(line.split())
    return 


if __name__ == '__main__':
    h = Hadoop2()
    print int()
