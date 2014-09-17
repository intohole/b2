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






if __name__ == '__main__':
    data = {}
    data[0] = 1
    data[2] = 2
    print get_sign_repeat('#' , 6)
    print dict_to_string(data)
    print reverse('123')