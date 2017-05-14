# coding=utf-8


from random import randint
import time
from math import log
from math import e
import exceptions2

_num_word = {10:'拾',9: '亿', 8: '仟', 7: '百', 6: '拾',
             5: '万', 4: '仟', 3: '百', 2: '拾', 1: ''}
_zh_num = ['', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖', '拾']

__all__ = ["num_2_chinese","ln","isdigit"]

def num_2_chinese(num):
    """将数字转换为汉字
        param:num:(int|basestring):需要转换的数字
        return:numstring:basestring:转换后的大写汉字
        exception:TypeError:抛出参数num类型异常
        Test:
            >>> print num_2_chinese(1234567890)
    """
    if not isinstance(num, (int, str)):
        exceptions2.raiseTypeError(num)
    num = str(int(num))
    l = len(num)
    num_string = []
    for i in range(l - 1,  -1, -1):
        if _num_word.has_key(l - i):
            num_string.append(_num_word[l - i])
        num_string.append(_zh_num[int(num[i])])
    num_string.reverse()
    return ''.join(num_string)


def ln(num):
    return math.log(num, e)


def isdigit(num):
    if isinstance(num, (float, int, long)):
        return True
    if isinstance(num, str) and (num.isdigit() or num.startswith('0.') and num[2:].isdigit()):
        return True
    return False
