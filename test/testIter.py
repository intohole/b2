#coding=utf-8




def range(start , end , step = -1):
    class __Iter(object):
        __slots__('start' , 'end' , 'step')

        def __init__(self , start  , end , step):
            self.start = start
            self.end = end
            self.step = step



        def __iter__(self):
            pass


        def next(self):
            return self.__iter


        def __len__(self):
            pass


        

