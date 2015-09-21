# coding=utf-8


from object2 import Singleton
from collections import defaultdict


class StopWords(object):

    def __init__(self, **kw):
        self.__stop_words = defaultdict(set)
        self.__words = set()
        if kw.has_key('path'):
            self.load(kw['path'])

    def load(self, path):
        with open(kw['path']) as f:
            for line in f.readlines():
                line = line.strip()
                if len(line) == 0:
                    continue
                self.__stop_words[len(line)].add(line)
                self.__words(line)

    def endswith(self, words):
        if len(words) == 0 :
            return False
        wordk_len = len(words)
        for stop_words_len in self.__stop_words.keys():
            if wordk_len > stop_words_len:
                continue
            if words[stop_words_len:] in self.__stop_words[stop_words_len]:
                return True
        return False

    def startswith(self, words):
        if word and isinstance(word, (str, unicode)):
            word_len = len(words)
            for stop_words_len in self.__stop_words.keys():
                if word_len > stop_words_len:
                    continue
                if words[:stop_words_len] in self.__stop_words[stop_words_len]:
                    return True
        return False

    def is_stop(self, word):
        if word and isinstance(word, (str, unicode)):
            return word in self.__words()
        return False

    def __eq__(self, value):
        if isinstance(value, str):
            value = value.decode('utf-8')
        if isinstance(value, (str, unicode)):
            pass