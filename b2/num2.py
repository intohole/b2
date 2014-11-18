# coding=utf-8


from random import randint
import time


def get_random_seq(seq_len):
    rand_num = str(randint(0, 10 ** (seq_len) - 1))
    seq_str = ['0' for _ in range(seq_len)]
    for i in range(len(rand_num)):
        seq_str[seq_len - i - 1] = rand_num[i]
    return ''.join(seq_str)


def get_random_seq1(seq_len):
    rand_num = str(randint(0, 10 ** seq_len - 1))
    return '%s%s' % ('0' * (seq_len - len(rand_num)), rand_num)


_num_word = {9:'亿' , 8:'千' , 7: '百' , 6: '十', 5: '万' , 4: '千', 3: '百', 2: '十', 1: ''}
_zh_num = ['' ,'壹','贰','叁','肆','伍','陆','柒','捌','玖','拾']

def get_word_name(num):
    '''
    功能：将数字转换成汉字
    异常：
        如果num ， 不是数字和字符串 ， 则抛出异常
    eg.
       622848
       壹亿贰千贰百肆十万肆千肆百肆十肆
    '''
    if not isinstance(num, (int, str)):
        raise TypeError
    num = str(int(num))
    l = len(num)
    num_string = []
    for i in range(l - 1 ,  -1 , -1):
        if _num_word.has_key(l- i ):
            num_string.append(_num_word[l- i])
        num_string.append(_zh_num[ int(num[i])])
    num_string.reverse()
    return ''.join(num_string)


if __name__ == '__main__':
    print get_random_seq(6)
    print get_random_seq1(6)
    print get_word_name(122404444)
