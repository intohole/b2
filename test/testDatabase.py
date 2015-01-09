#coding=utf-8




class Cache(dict ):
    

    def __setitem__(self , key , value ):
        if value and isinstance(value , (basestring,int , long , float)):
            super.__setitem__(key , value)
        else:
            raise TypeError , 'cache value must be int or long , float , string !'


    




class PD(object):



    def __init__(self , data_path = '' , sysnc = 0.0001):
        pass


