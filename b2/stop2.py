# coding=utf-8


from object2 import Singleton
from collections import defaultdict
import bisect


class StopWords(object):

    def __init__(self, **kw):
        self.stop_words = defaultdict(set)
        if kw.has_key('path'):
            with open(kw['path']) as f:
                for line in f.readlines():
                    line = line.strip()
                    if len(line) > 0:
                        self.stop_words[len(line)].add(line)
        else:
            raise ValueError
        self.word_len_keys = sorted(self.stop_words.keys())

    def endswith(self, words):
        word_len = len(words)
        word_len_index = bisect.bisect(self.word_len_keys, word_len)
        if word_len_index == len(self.word_len_keys):
            return False
        for stop_words_len in self.word_len_keys[:word_len_index]:
            if words[-stop_words_len:] in self.stop_words[stop_words_len]:
                return True
        return False

    def startswith(self, words):
        if words and isinstance(words, (str, unicode)):
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
            return False
        raise ValueError

    def __getitem__(self, value):
        return self.is_stop(value)

if __name__ == '__main__':
    s = StopWords(path='e:\\a.txt')
    print s.endswith('aaaaaaaaaaaaaaa')
    print s.endswith('a')
    print s.is_stop('aaaa')
