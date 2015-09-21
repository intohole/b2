# coding=utf-8


from exceptions2 import judge_str
import inspect
<<<<<<< HEAD
import threading

=======
import threading 
>>>>>>> cb824139036a2c1a25884d5a10934b0fd13c2eda


<<<<<<< HEAD
    '''单例模式
    '''
=======
>>>>>>> cb824139036a2c1a25884d5a10934b0fd13c2eda


class Singleton(object):

    """python单例实现方式
    """
    @classmethod
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            mutex = threading.Lock()
            mutex.acquire()
            if not hasattr(cls, '_instance'):
<<<<<<< HEAD
                orig = super(Singleton, cls)
                cls._instance = orig.__new__(cls, *args, **kw)
=======
                print 'create'
                cls._instance = super(Singleton, cls).__new__(cls, *args, **kw)
>>>>>>> cb824139036a2c1a25884d5a10934b0fd13c2eda
            mutex.release()
        return cls._instance
    





def singleton(cls, *args, **kw):
<<<<<<< HEAD
    '''
    将一个类转换为单例模式：
    @singleton
    class Test(object):
        a = 'c'
    c = Test()
    b = Test()
    b.a = 'a'
    print b.a 

    '''
=======
>>>>>>> cb824139036a2c1a25884d5a10934b0fd13c2eda
    instances = {}
    def _singleton(*args,**kw):
        if cls not in instances:
            mutex = threading.Lock()
            mutex.acquire()
            if cls not in instances:
                instances[cls] = cls(*args, **kw)
            mutex.release()
        return instances[cls]
    return _singleton


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
    obj = getattr(model, class_name, None)
    if obj is not None  \
<<<<<<< HEAD
        and inspect.isclass(obj)
        return obj(*arg, **kw)
    return None
=======
        and inspect.isclass(obj):
        return obj(*arg , **kw)
    return None 
>>>>>>> cb824139036a2c1a25884d5a10934b0fd13c2eda


def create_obj_by_str(model, *arg, **kw):
    model = model.split('.')
    return create_obj('.'.join(model[:-1]),  model[-1], *arg, **kw)



class AutoID(object):

    """程序自增id
    """

    def __init__(self, *argv, **kw):
        start_id = 0
        if "start_id" in kw:
            start_id = kw["start_id"]
        self.__start_id = start_id
        self.__id = self.__start_id
        self.__map_id = {}
        self.__mutex = threading.Lock()

    def __getitem__(self, key):
        if key is not None:
            if key in self.__map_id:
                return self.__map_id[key]
            else:
                self.__mutex.acquire()
                self.__map_id[key] = self.__id
                self.__id += 1
                ret_id = self.__map_id[key]
                self.__mutex.release()
                return ret_id
        else:
            raise ValueError, "key is none ! please check"

    def clear(self):
        self.__mutex.acquire()
        self.__map_id.clear()
        self.__id = self.__start_id
        self.__mutex.release()
        return True

    def items(self):
        return self.__map_id.items()

    def __str__(self):
        str_buf = ["start_id\t%s" % (self.__start_id)]
        for name, _id in self.__map_id.items():
            str_buf.append("%s\t%s\n" % (name, _id))
        return '\n'.join(str_buf)

    def save_id_map(self, file_path, output="text"):
        if output in ["text", "json"]:
            if output == "text":
                with open(file_path, 'w') as f:
                    f.write(str(self))
            elif output == "json":
                with open(file_path, "w") as f:
                    f.write(
                        json.dumps(self.__map_id, ensure_assic=False) + "\n")
        else:
            raise ValueError, "[error]\toutput can only chooese [text , json]"

    def get(self, name):
        return self.__getitem__(name)