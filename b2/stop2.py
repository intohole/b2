# coding=utf-8


from object2 import Singleton
from collections import defaultdict



class StopWords(object):

    def __init__(self, **kw):
        self.stop_words = defaultdict(set)
        self.words = set()
        if kw.has_key('path'):
            with open(kw['path']) as f:
                for line in f.readlines():
                    line = line.strip()
                    if len(line) > 0:
                        self.stop_words[len(line)].add(line)
                        self.words(line)

    def endswith(self, words):

        wordk_len = len(words)
        for stop_words_len in self.stop_words.keys():
            if wordk_len > stop_words_len:
                continue
            if words[stop_words_len:] in self.stop_words[stop_words_len]:
                return True
        return False

    def startswith(self, words):
        if word and isinstance(word, (str, unicode)):
            word_len = len(words)
            for stop_words_len in self.stop_words.keys():
                if word_len > stop_words_len:
                    continue
                if words[:stop_words_len] in self.stop_words[stop_words_len]:
                    return True
        return False

    def is_stop(self, word):
        if word and isinstance(word, (str, unicode)):
            word_len = len(word)
            if word_len in self.stop_words.keys():
                return self.stop_words[word_len].has_key(word)
        raise TypeError


    def __getitem__(self , value):
        return self.is_stop(value)

if __name__ == '__main__':
    s = StopWords(path='d:\\a.txt')
    print s.endswith('a')
    print s.startswith('a')
    print s.is_stop('aaaa')
