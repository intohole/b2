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
            if limit and self.__index == self.limit :
                raise StopIteration , 'iter bigger than limit! limit = %s'  % self.limit
            self.__index += 1
            return randint(self.min_value , max_value)

        def has_next(self):
            if self.limit and self.__index < self.limit:
                return False
            return True

    return RandInt(min_value , max_value , limit)

def rand_string(l  ,lower_str = True  , higher_str = True , num_str = True ,limit =1000000):

    class  __RandString(object):
        def __init__(self , string_len , limit , lower_str = True  , higher_str = True , num_str = True):
            self.__char = []
            if lower_str:
                self.__char.extend([ chr(ord('a')+ i) for i in range(ord('z') - ord('a') + 1)])
            if higher_str:
                self.__char.extend([chr(ord('A')+ i) for i in range(ord('Z') - ord('A') + 1)])
            if num_str:
                self.__char.extend([str(i) for i in range(10)])
            if len(self.__char) == 0:
                raise ValueError , 'must set lower_str / higher_str /num_str more than one True'
            self.__rand = get_rand(0 , len(self.__char) - 1  , None)
            self.__index = 0
            self.limit = limit
            self.string_len = string_len

        def next(self):
            if limit and self.__index == self.limit :
                raise StopIteration , 'iter bigger than limit! limit = %s'  % self.limit
            self.__index += 1
            return ''.join([self.__char[self.__rand.next()] for i in range(self.string_len)])

        def has_next(self):
            if self.limit and self.__index < self.limit:
                return False
            return True
    return __RandString(l , limit)



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
    # datas = [ i  for i in range(100000)]
    # # print reservoir(datas , 1000)
    # a = iter(get_rand(1, 1000))
    # for i in a:
    #     print i
    a = rand_string(10 , 1000)
    print a.next()


    # print a.next()
    # print a.next()
    # print a.next()
