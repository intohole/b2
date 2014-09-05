#coding=utf-8

from exceptions2 import *

class Buffer2(object):



    def __init__(self , content = None):
        self.__buf = []
        if content:
            judge_str(content)



    def append(self , line):
        '''
        字符串追加
        '''
        judge_str(line)
        self.__buf.extend(line)

    def __add__(self , line):
        self.append(line)


    def find_first(self , code):
        judge_str(code)



    def __str__(self):
        return ''.join(self.__buf)

if __name__ == '__main__':
    buf = Buffer2()
    buf += '12'
    print str(buf)