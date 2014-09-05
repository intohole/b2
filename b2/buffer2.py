#coding=utf-8

from exceptions2 import *

class Buffer2(object):
    '''
    编写类似java stringbuilder 工具类 ，
    将字符串扩展变的容易简单
    '''


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
        return self


    def find_first(self , value):
        judge_str(value)
        if len(value) > len(self.__buf):
            return -1
        return self.__buf.index(value)
        # __buf_index = 0
        # while __buf_index < (len(self.__buf) - len(value)):
        #     __value_index = 0
        #     __buf_tmp = __buf_index 
        #     while __value_index < len(value):
        #         if value[__value_index] != self.__buf[__buf_tmp]:
        #             break
        #         __value_index += 1
        #         __buf_tmp += 1
        #     if __value_index == (len(value) - 1):
        #         return __buf_index
        #     __buf_index += 1
        # return -1
    
    def __len__(self):
        return len(self.__buf)
    
    def sort(self):
        self.__buf.sort()

    def reverse(self):
        return str(''.join(self.__buf))[::-1]

    def charat(self , index):
        judge_null(index)
        judge_type(index , (int))
        judge_ge_value(index , 0)
        judge_le_value(index , len(self.__buf))
        return self.__buf(index)

    def __getitem__(self , key):
        return self.charat(index)

    def __setitem__(self , index , value):
        judge_null(index)
        judge_type(index , (int))


    def __str__(self):
        return self.to_str('')

    def to_str(self , join_str = ''):
        judge_str(join_str)
        return join_str.join(self.__buf)

if __name__ == '__main__':
    buf = Buffer2()
    buf += '03355112'
    print buf
    print buf.find_first('1')
    print buf.reverse()
    print buf.to_str('\n')
    print len(buf)
