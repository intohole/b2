#coding=utf-8


from exceptions2 import *



def dict_to_string(data):
    if data and len(data) >  0 and isinstance(data , dict):
        return ' '.join(["%s:%s" % (__key , __val) for __key , __val in data.items()])
    return ''


def get_sign_repeat(sign , n):
    judge_str(sign)
    judge_num(n)
    return sign * n 

def join_str_list(buf , join_str ):
    judge_list(buf)
    judge_str(join_str)
    return join_str.join(buf)



def reverse(words):
    judge_str(words)
    return words[::-1]


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
        if line == None:
            raise ValueError , 'append value is None !'
        if isinstance(line , (str , unicode , list , tuple)):
            self.__buf.extend(line)
            return 
        raise TypeError , 'append function can accept value\'s is list str unicode tuple ' 

    def __add__(self , line):
        self.append(line)
        return self


    def find_first(self , value):
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


    def __eq__(self , val):
        if val == None:
            return False
        if isinstance(val , list):
            return self.__buf == val
        elif isinstance(val , Buffer2):
            return  self.__buf == val.__buf
        elif isinstance(val , str ) :
            return self.to_str() == val
        return False




if __name__ == '__main__':
    data = {}
    data[0] = 1
    data[2] = 2
    print get_sign_repeat('#' , 6)
    print dict_to_string(data)
    print reverse('123')
    buf = Buffer2()
    buf += '03355112'
    print buf
    print buf.find_first('1')
    print buf.reverse()
    print buf.to_str('\n')
    print len(buf)
    buf1 = Buffer2()
    buf1 += '03355112'

    print buf1 == buf

    buf1+= '122'
    print buf1
    print buf1 == buf
    print buf == '03355112' 
    print buf1.reverse()