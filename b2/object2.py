# coding=utf-8


from exceptions2 import judge_str
import inspect
import threading 




class Singleton(object):

    """python单例实现方式
    """
    @classmethod
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
    """单例修饰符
        params:
            cls             类
            args            类初始化序列话参数
            kw              类初始化使用的词典参数
        return 
            object          类的实例
        raise 
            None 
    """
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
    """python版本自实现枚举功能
        params
            args                枚举名称
            start               枚举类型初始值，后续不断累加1
            split_char          为了更好的使用枚举类型，出现需要设定为新值时的功能
        return
            Enum                枚举实体类
        raise 
            None
        eg:
            DEFINE=enum("a b c")
            DEFINE.a = 0 
            DEFINE.b = 1 
            DEFINE.c = 2 
            DEFINE1 = enum("a b#3 c" , split_char="#")
            DEFINE1.a = 0
            DEFINE1.b = 3
            DEFINE1.c = 4
    """
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
            and inspect.isclass(obj):
        return obj(*arg, **kw)
    return None


def create_obj_by_str(model, *arg, **kw):
    model = model.split('.')
    return create_obj('.'.join(model[:-1]),  model[-1], *arg, **kw)



class AutoID(object):

    """实现自增长id
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



class Byte2(object):

    def __init__(self , datas):
        self.byte_objects = {}
        self.byte_len = None
        if isinstance(datas , (list , tuple)):
            self.byte_objects = { i : (datas[i] , 1 << i) for i in range(len(datas))}
            self.reverse_byte_objects = {datas[i] : (i , 1<<i) for i in range(len(datas))}
            self.byte_len = len(datas)
        elif isinstance(datas , dict):
            self.byte_objects = { i : (name , 1 << i) for i , name in datas.items()}
            self.reverse_byte_objects = { name : (i , 1<<i) for i , name in datas.items()}
            self.byte_len =  max( int(key) for key in datas.keys())
        else:
            raise TypeError

    def __and__(self , val):
        if val is None:
            raise TypeError
        if isinstance(val  , int):
            _means = []
            for i in range(self.byte_len):
                if val & self.byte_objects[i][1]:
                    _means.append(self.byte_objects[i][0])
            return ' '.join(_means)
        elif isinstance(val , (list , tuple)):
            _val = 0
            for i in range(len(val)):
                if val[i] in self.reverse_byte_objects:
                    _val |= self.reverse_byte_objects[val[i]][1]
                else:
                    raise ValueError , "%s not right params " % val[i]
            return  _val

        
    

class LList(object):
    """统计list 使用 
        
    """    
    def __init__(self , names):
        if isinstance(names , basestring):
            names = names.replace("," , " ").split()
        elif isinstance(names , (list , tuple)) is False:
           raise TypeError
        self.names = names 
        self._name_list = {} # 名称对应词典
        if len(names) > len(set(names)):
            raise ValueError , "duplicate key exist , please check"
        for index , name in enumerate(self.names):
            if name in ["clear" , "incr"]:
                raise ValueError , "key must not in [clear , incr]!"
            self._name_list[name] = index
            setattr(self , name , 0)
    
    def clear(self):
        for name in self.names:
            setattr(self , name , 0)
    
    def incr(self , name , value = 1):
        if name in self.names:
            count = getattr(self , name)
            setattr(self , name , count + value)
        else:
            return None
    def incrs(self , values):
        if len(self.names) == len(values):
            for index , name in enumerate(self.names):
                self.incr(name , values[index])
            return True
        return False  
    
    def get_index(self , name ):
        if name in self._name_list:
            return self._name_list[name]
        else:
            raise ValueError , "%s not in namelist" % (name)
                 
    def __str__(self):
        return "\t".join(str(getattr(self , name)) for name in self.names)
    
    def __len__(self):
        return len(self.names)

