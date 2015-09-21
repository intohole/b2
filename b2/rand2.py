# coding=utf-8
from random import randint
from exceptions2 import judge_num


def get_rand(min_value, max_value, limit=10000):
    '''
    生成一个自动产生的随机数返回生成器
    使用方法:
        a  =  get_rand(1 , 10 , 1000)
        a.next()

        或者生成一个新的迭代器
        b = iter(a)
        b.next()
        或者 for循环使用
        for i in a:
            print i 
    '''
    class RandInt(object):

        def __init__(self, min_value, max_value, limit):
            self.min_value = min_value
            self.max_value = max_value
            self.limit = limit
            self.__index = 0

        def __iter__(self):
            return RandInt(self.min_value, self.max_value, self.limit)

        def next(self):
            if limit and self.__index == self.limit:
                raise StopIteration, 'iter bigger than limit! limit = %s' % self.limit
            self.__index += 1
            return randint(self.min_value, max_value)

        def has_next(self):
            if self.limit and self.__index < self.limit:
                return False
            return True

    return RandInt(min_value, max_value, limit)


def rand_string(l, lower_str=True, higher_str=True, num_str=True, limit=1000000):
    '''
    随机生成字符串 （数字、小写字母 、 大写字母 速记组合大于一种字符串）
    参数:
         l 生成字符串的长度
         lower_str 是否含有小写字母
         higher_str 随机字符串是否含有大写字母
         num_str 随机字符串是否含有数字字母
         limit 随机生成字符串数量限制 ， 如果为None ， 没有限制 ， 但是for in 情况慎用（会无限循环）
    exception:
         无
    return 随机字符串


    example:
         a = rand_string(10 , 1000)
         print a.next()
         or :
         for i in rand_string(10 , limit = 10)：
             print i 
    '''
    class RandString(object):

        def __init__(self, string_len, limit, lower_str=True, higher_str=True, num_str=True):
            self.__char = []
            self.lower_str = lower_str
            self.higher_str = higher_str
            self.num_str = num_str
            if lower_str:
                self.__char.extend([chr(ord('a') + i)
                                    for i in range(ord('z') - ord('a') + 1)])
            if higher_str:
                self.__char.extend([chr(ord('A') + i)
                                    for i in range(ord('Z') - ord('A') + 1)])
            if num_str:
                self.__char.extend([str(i) for i in range(10)])
            if len(self.__char) == 0:
                raise ValueError, 'must set lower_str / higher_str /num_str more than one True'
            self.__rand = get_rand(0, len(self.__char) - 1, None)
            self.__index = 0
            self.limit = limit
            self.string_len = string_len

        def __iter__(self):
            return RandString(self.string_len, self.limit, self.lower_str, self.higher_str, self.num_str)

        def next(self):
            if limit and self.__index == self.limit:
                raise StopIteration, 'iter bigger than limit! limit = %s' % self.limit
            self.__index += 1
            return ''.join([self.__char[self.__rand.next()] for i in range(self.string_len)])

        def has_next(self):
            if self.limit and self.__index < self.limit:
                return False
            return True
    return RandString(l, limit)



def rand_int_range(range_num=1):
    range_num = 10 ** (range_num - 1)
    return randint(range_num, range_num * 10 - 1)


def get_random_seq(seq_len):
    rand_num = str(randint(0, 10 ** seq_len - 1))
    return '%s%s' % ('0' * (seq_len - len(rand_num)), rand_num)