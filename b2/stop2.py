# coding=utf-8


from collections import defaultdict
import bisect

__ALL__ = [ "StopWords"]

class StopWords(object):
    """停用词工具类 ，为了最大限度的判断字符串存在于词典的工具
        test:
            >>> from stop2 import StopWords
            >>> st = StopWords(words = ["a" ,"c"]) ; 
            >>> print st._stop_words
            >>> print st.startswith("ab") , st.endswith("cb")
    """
    def __init__(self, **kw):
        """初始化词典
            path                词典文件，文件按照
            words               词典list ， 可选
        """
        self._stop_words = defaultdict(set)
        if "path" in kw:
            self.__load(kw['path'])
        if "words" in kw:
            if self.add(kw["words"]) is False:
                raise ValueError , "params words is not right value ! please check"
        self.len_arrys = sorted(self._stop_words.keys())

    def __load(self, path):
        with open(kw['path']) as f:
            for line in f.readlines():
                line = line.strip()
                if len(line) == 0:
                    continue
                self._stop_words[len(line)].add(line)
        
    def add(self , words ):
        if words and isinstance(words , basestring):
            self._stop_words[len(words)].add(words)
        elif words and isinstance(words , (tuple , list)):
            for word in words:
                self.add(word)
            return True
        else:
            return False

    def endswith(self, words):
        """判断字符串words否以词典中的字符串结尾
            params
                words               需要判断的字符串
            return 
                value , msg         value如果不为None ，表示已经找到，匹配上的词典中字符串长度
            raise 
                None
        """
        if words and isinstance(words, basestring):
            wordk_len = len(words)
            for stop_words_len in self._stop_words.keys():
                if wordk_len < stop_words_len:
                    continue
                if words[stop_words_len:] in self._stop_words[stop_words_len]:
                    return stop_words_len , words[stop_words_len:]
            return None , "not found"
        return None , "value error" 

    def startswith(self, words):
        """判断字符串words否以词典中的字符串开头
            params
                words               需要判断的字符串
            return 
                value , msg         value如果不为None ，表示已经找到，匹配上的词典中字符串长度 
            raise 
                None
        """
        if words and isinstance(words, basestring):
            word_len = len(words)
            for stop_words_len in self._stop_words.keys():
                if word_len < stop_words_len:
                    continue
                if words[:stop_words_len] in self._stop_words[stop_words_len]:
                    return stop_words_len , words[:stop_words_len]
            return None , "not find"
        return None , "type error"

    def is_stop(self, word):
        """判断字符串是否存在于类中
            params:
                words               需要判断的字符串
            return 
                True                words存在于词典中
                False               words不存在词典中
            raise
                None
        """
        if word and isinstance(word, basestring):
            word_len = len(word)
            if word_len in self._stop_words.keys():
                return word in self._stop_words[word_len]
            return False
        raise ValueError

    def __getitem__(self, value):
        return self.is_stop(value)
