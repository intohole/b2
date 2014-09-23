# coding=utf-8


from object2 import Singleton
from collections import defaultdict


class StopWords(object):


    def __init__(self, **kw):
        self.__stop_words = defaultdict(set)
        if kw.has_key('path'):
            with open(kw['path']) as f:
                for line in f.readlines():
                    line = line.strip()
                    if len(line) > 0:
                        self.__stop_words[len(line)].add(line)


    def endswith(self ,words):
        l = len(words)
        for __l in self.__stop_words.keys():
            if l > __l:
                continue
            if words[__l:] in self.__stop_words[__l] :
                return True
        return False

    def startswith(self , words):
        l = len(words)
        for __l in self.__stop_words.keys():
            if l > __l:
                continue
            if words[:__l] in self.__stop_words[__l]:
                return True
        return False



    def __eq__(self, value):
        if isinstance(value, str):
            value = value.decode('utf-8')
        if isinstance(value, (str, unicode)):
            pass


if __name__ == '__main__':
    s = StopWords(path = 'd:\\a.txt')
    print s.endswith('a')