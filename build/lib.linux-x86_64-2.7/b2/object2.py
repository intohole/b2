# coding=utf-8


from exceptions2 import judge_str


class Singleton(object):

    '''
    设计模式单例 
    '''

    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance


def enum(args, start=0 , split_char = None):
    '''
    enum 枚举实现　－　＞　使用方式　　enmu('ENUM1 ... Enum2 .. EnumN')

    '''
    class Enum(object):
        

        def __init__(self , args , start = 0 , split_char = None):
            key_split = args.split()
            last = 0
            for i, key in enumerate(key_split, start):
                if split_char != None:
                    key_value = key.split(split_char)
                    if len(key_value) >= 2:
                        last = int(key_value[1]) - 1
                    last += 1
                    setattr(self , key_value[0] , last)
                else:
                    setattr(self, key, i)
    return Enum(args , start , split_char)


def enum2(**enums):
    return type('Enum', (), enums)



def create_obj(model_name, class_name, *arg, **kw):
    judge_str(model_name, 1, (str))
    judge_str(class_name, 1, (str))
    model = __import__(model_name)
    obj = getattr(model, class_name)
    return obj(*arg ,**kw)


def create_obj_by_str  (model , *arg , **kw):
    model = model.split('.')
    return create_obj( '.'.join(model[:-1] ),  model[-1] , *arg , **kw)


def is_contain_function(f, fun):
    if f:
        if hasattr(f, fun):
            if callable(f.fun):
                return True
    return False


class Test(Singleton):


    def __init__(self, *arg, **kw):
        print kw
        print arg

class Test2(object):

    """docstring for Test2"""

    def __init__(self):
        super(Test2, self).__init__()
        self.arg = arg


if __name__ == '__main__':
    d = {'a' :5 , 'b':0 , 'c' : 9 ,'d' :0}
    a = enum('a:12 b:15 c' , split_char = ':')
    print a.c
    print a.a
    c = Enum2()
    c.a = 7 
    c.a = 8
    print c.a 
    # print create_obj('object2', 'Test',  **d)
    # print create_obj_by_str('object2.Test')
    # def p(*arg , **kw):
    #     if kw.has_key('a'):
    #         print kw['a']
    #     if len(arg) > 0:
    #         print arg[0]
    # p(1 ,2 ,3 , a = 5 , b = 6)
    #     # 5
    #     # 1
    # d = {'a' : 6  , 'c' : 7}
    # p(**d)
    # print '.'.join('wenkr_spider.spiders.kr36.Kr36'.split('.')[:-1])
    # print 'wenkr_spider.spiders.kr36.Kr36'.split('.')[-1]
    # a = create_obj_by_str('collections.defaultdict' , int)
    # print a
        # 6