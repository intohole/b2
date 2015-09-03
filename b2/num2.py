# coding=utf-8


from random import randint
import time
from math import log
from math import e


_num_word = {9: '亿', 8: '千', 7: '百', 6: '十',
             5: '万', 4: '千', 3: '百', 2: '十', 1: ''}
_zh_num = ['', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖', '拾']


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
    for i in range(l - 1,  -1, -1):
        if _num_word.has_key(l - i):
            num_string.append(_num_word[l - i])
        num_string.append(_zh_num[int(num[i])])
    num_string.reverse()
    return ''.join(num_string)


def getLn(num):
    return math.log(num, e)


def isdigit(num):
    if isinstance(num, (float, int, long)):
        return True
    if isinstance(num, str) and (num.isdigit() or num.startswith('0.') and num[2:].isdigit()):
        return True
    return False