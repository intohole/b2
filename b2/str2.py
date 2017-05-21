# coding=utf-8


import exceptions2
import re
import object2



__ALL__ = ["emptyString","isEmpty","isBlank","repeats","reverse","upper","iconvft","splits","Buffer2"]
_escape_char = set([".","[","]","(",")","\\","|"])
_split_pattern_cache = {}

def emptyString():
    return ""



def isEmpty(words):
    if words is None:
        return True
    if isinstance(words,basestring):
        if len(words) == 0:
            return True
        return False
    exceptions2.raiseTypeError(words)        

def isBlank(words):
    return True if isEmpty(words) else len(words.strip()) == 0

def repeats(sign, n):
    judge_str(sign)
    judge_num(n)
    return sign * n

def reverse(words):
    judge_str(words)
    return words[::-1]

def upper(words, upper_len):
    if len(words) < upper_len:
        upper_len = len(words)
    return "".join([chr(ord(words[i]) - 32) if i < upper_len and ord(words[i]) <= 122 and ord(words[i]) >= 97 else words[i] for i in range(len(words))])

def splits(words,split_chars,escape=True):
    """use re.split function 
        param:words:basestring:split string
        param:split_chars:split char array
        param:escape:boolean:split char is need escape
        return:split words:list:words split by split_chars list 
        Test:
            >>> splits(None,[",","."])
            >>> splits("1,2,3.5,6",[",","."])
    """
    if escape:
        split_chars = [ "\%s" % split_char if split_char in _escape_char else split_char for split_char in split_chars]
    if isEmpty(words):
        return []
    split_pattern = "%s" % "|".join(split_chars)
    if split_pattern not in _split_pattern_cache: 
        _split_pattern_cache[split_pattern] = re.compile(split_pattern)
    return _split_pattern_cache[split_pattern].split(words)
    
    

def iconvft(content , code1 = "gbk",code2 = "utf-8",ignore = False):
    if content is None:
        return content
    return content.decode(code1).encode(code2) if ignore is False else content.decode(code1,"ignore").encode(code2)

class Buffer2(object):

    '''
    编写类似java stringbuilder 工具类 ，
    将字符串扩展变的容易简单
    '''

    def __init__(self, content=None):
        self.__buf = []
        if content:
            judge_str(content)

    def append(self, line):
        '''
        字符串追加
        '''
        if line == None:
            raise ValueError, 'append value is None !'
        if isinstance(line, (str, unicode, list, tuple)):
            self.__buf.extend(line)
            return
        raise TypeError, 'append function can accept value\'s is list str unicode tuple '

    def __add__(self, line):
        self.append(line)
        return self

    def find_first(self, value):
        judge_str(value)
        if len(value) > len(self.__buf):
            return -1
        return self.__buf.index(value)

    def __len__(self):
        return len(self.__buf)

    def sort(self):
        self.__buf.sort()

    def reverse(self):
        return str(''.join(self.__buf))[::-1]

    def char_at(self, index):
        judge_null(index)
        judge_type(index, (int))
        judge_ge_value(index, 0)
        judge_le_value(index, len(self.__buf))
        return self.__buf(index)

    def __getitem__(self, key):
        return self.charat(index)

    def __setitem__(self, index, value):
        judge_null(index)
        judge_type(index, (int))

    def __str__(self):
        return self.to_str('')

    def to_str(self, join_str=''):
        judge_str(join_str)
        return join_str.join(self.__buf)

    def __eq__(self, val):
        if val == None:
            return False
        if isinstance(val, list):
            return self.__buf == val
        elif isinstance(val, Buffer2):
            return self.__buf == val.__buf
        elif isinstance(val, str):
            return self.to_str() == val
        return False


