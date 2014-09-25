# coding=utf-8


from object2 import Singleton
from collections import defaultdict


class StopWords(object):


    def __init__(self, **kw):
        self.__stop_words = defaultdict(set)
        self.__words = set()
        if kw.has_key('path'):
            with open(kw['path']) as f:
                for line in f.readlines():
                    line = line.strip()
                    if len(line) > 0:
                        self.__stop_words[len(line)].add(line)
                        self.__words(line)



    def endswith(self ,words):
        l = len(words)
        for __l in self.__stop_words.keys():
            if l > __l:
                continue
            if words[__l:] in self.__stop_words[__l] :
                return True
        return False

    def startswith(self , words):
        if word and isinstance(word , (str , unicode)):
            l = len(words)
            for __l in self.__stop_words.keys():
                if l > __l:
                    continue
                if words[:__l] in self.__stop_words[__l]:
                    return True
        return False


    def is_stop(self , word):
        if word and isinstance(word , (str , unicode)):
            return word in self.__words()
        return False





    def __eq__(self, value):
        if isinstance(value, str):
            value = value.decode('utf-8')
        if isinstance(value, (str, unicode)):
            pass


if __name__ == '__main__':
    s = StopWords(path = 'd:\\a.txt')
    print s.endswith('a')
    print s.startswith('a')
    print s.is_stop('aaaa')