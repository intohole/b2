# coding=utf-8


class InsertOrderDict(dict):

    def __init__(self, *argv, **kw):
        super(InsertOrderDict, self).__init__(*argv, **kw)
        self.__order_list = []

    def __setitem__(self, key, value):
        if key is not None and key not in self:
            self.__order_list.append(key)
        super(InsertOrderDict, self).__setitem__(key, value)


    def items(self):
        for key in self.__order_list:
            yield key , self[key]


    def __delitem__(self , key):
        if key is not None and key in self:
            self.__order_list.remove(key)
            super(InsertOrderDict , self).__delitem__(key)

    def clear(self):
        del self.__order_list[:]
        super(InsertOrderDict , self).clear()
    


if __name__ == '__main__':
    t = InsertOrderDict()
    t[1] = 1
    t[-1] = 0
    del t[1]
    t[5] = 7
    for key , value in t.items():
        print key , value 
    t.clear()
    t[3] = 4
    for key , value in t.items():
        print key , value 

