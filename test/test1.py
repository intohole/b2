



class N(int):


    def __init__(self , * arg , ** kw):
        int.__init__( arg , kw)





class BaseColor(dict):
        def __init__(self , show_set , fore_color , back_color ):
            self['SET'] = show_set
            self['FORE'] = fore_color
            self['BACK'] = back_color
        def __str__(self):
            return '\033[%(SET)s;%(FORE)s;%(BACK)sm' % self


import sys



class TestColor(object):
    


    def __init__(self , color):
        bc = BaseColor(0,'','')
        print bc
    def __add__(self , value ):
        buf = []


if __name__ == '__main__':
    t = TestColor(1)