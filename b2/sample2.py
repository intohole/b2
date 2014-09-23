# coding=utf-8
from random import randint



def get_rand(min_value , max_value , limit =10000):
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

        def __init__(self , min_value , max_value  , limit ):
            self.min_value = min_value 
            self.max_value = max_value
            self.limit = limit
            self.__index = 0


        def __iter__(self):
            return RandInt(self.min_value , self.max_value , self.limit)


        def next(self):
            if self.__index == self.limit :
                raise StopIteration , 'iter bigger than limit! limit = %s'  % self.limit
            self.__index += 1
            return randint(self.min_value , max_value)

        def has_next(self):
            if self.__index < self.limit:
                return True
            return False

    return RandInt(min_value , max_value , limit)


def reservoir(datas, k):
    '''
    蓄水池抽样 ： 先注满水 ， 通过剩余数据
    datas 待抽样数据
    k 随机抽取数据数目
    '''
    if not (k and isinstance(k, (int)) and k > 0 ) :
        raise TypeError, 'k must be integer and bigger than zero!'
    if not ( datas and isinstance(datas, (list, tuple)) ) :
        raise TypeError, 'datas must be list and not None'
    if len(datas) <= k:
        return datas
    else:
        data_len = len(datas)
        data = [datas[d] for d in range(0, k)]
        for i in range(k, data_len):
            swap = randint(0, i)
            if swap < k:
                data[swap] = datas[i]
        return data

if __name__ == '__main__':
    datas = [ i  for i in range(100000)]
    # print reservoir(datas , 1000)
    a = iter(get_rand(1, 10))
    for i in a:
        print i


    print a.next()
    print a.next()
    print a.next()
