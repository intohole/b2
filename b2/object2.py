# coding=utf-8


class Singleton(object):

    '''
    设计模式单例 
    '''

    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance


def enum(args, start=0):
    '''
    enum 枚举实现　－　＞　使用方式　　enmu('ENUM1 ... Enum2 .. EnumN')

    '''
    class Enum(object):
        __slots__ = args.split()

        def __init__(self):
            for i, key in enumerate(Enum.__slots__, start):
                setattr(self, key, i)

    return Enum()





def is_contain_function(f, fun):
    if f:
        if hasattr(f, fun):
            if callable(f.fun):
                return True
    return False









if __name__ == '__main__':

    class Test(Singleton):
        a = 1
    t = Test()
    t.a = 2

    t1 = Test()
    print t1.a

    print id(t)
    print id(t1)

    Item = Enum('a b c')
    print Item.a
