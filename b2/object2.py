# coding=utf-8


from exceptions2 import judge_str
import inspect
import threading 




class Singleton(object):

    """python单例实现方式
    """
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            mutex = threading.Lock()
            mutex.acquire()
            if not hasattr(cls, '_instance'):
                orig = super(Singleton, cls)
                cls._instance = orig.__new__(cls, *args, **kw)
            mutex.release()
        return cls._instance



def singleton(cls, *args, **kw):
    instances = {}
    def singleton_instance():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return singleton_instance


def enum(args, start=0, split_char=None):
    '''
    enum 枚举实现　－　＞　使用方式　　enmu('ENUM1 ... Enum2 .. EnumN')

    '''
    class Enum(object):

        def __init__(self, args, start=0, split_char=None):
            key_split = args.split()
            last = 0
            for i, key in enumerate(key_split, start):
                if split_char != None:
                    key_value = key.split(split_char)
                    if len(key_value) >= 2:
                        last = int(key_value[1]) - 1
                    last += 1
                    setattr(self, key_value[0], last)
                else:
                    setattr(self, key, i)
    return Enum(args, start, split_char)


def enum2(**enums):
    return type('Enum', (), enums)


def create_obj(model_name, class_name, *arg, **kw):
    judge_str(model_name, 1, (str))
    judge_str(class_name, 1, (str))
    model = __import__(model_name)
    obj =  getattr(model , class_name , None )
    if obj is not None  \
        and inspect.isclass(obj)
        return obj(*arg , **kw)
    return None 


def create_obj_by_str(model, *arg, **kw):
    model = model.split('.')
    return create_obj('.'.join(model[:-1]),  model[-1], *arg, **kw)



