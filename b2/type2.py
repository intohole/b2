# coding=utf-8




from exceptions2 import judge_null

def is_none(value):
    """judge value is None
        param:value:judge value
        return:boolean:object is None
    """
    return value is None


def is_class(obj):
    """judge obj is class
        param:obj:judge value
    """
    if is_none(obj):
        return False
    return type(obj) in (types.InstanceType, types.ClassType)


def is_type(value, value_type):
    if is_none(value):
        return False
    if is_none(value_type):
        return False
    return isinstance(value, value_type)


def is_int(value):
    if is_none(value):
        return False
    return is_type(value, int)


def is_str(value):
    if is_none(value):
        return False
    return is_type(value, basestring)


def is_empty(value):
    if is_none(value):
        return True
    return len(value) > 0


def is_str_empty(value):
    if is_str(value):
        return False
    return is_empty(value)

def is_has_attr(value,attr):
    if is_none(value):
        return False
    if is_str(attr) is False:
        return False
    return hasattr(value,attr)

def is_iter(value):
    """judge value implmenttion of iter
        param:value:judge value
        return:is iter object
    """
    if is_none(value):
        return False
    return is_has_attr(value,"__iter__") and is_str(value) is False

def get_map_value(self, data, default=None, *argv):
    node = data
    for name in argv:
        if node.has_key(name):
            node = data[name]
        else:
            return default
    return node if node and isinstance(node, type(default)) else default


def update_config(d, **kw):
    judge_null(d)
    if d is None:
        raise ValueError, 'd is none !'
    if isinstance(d, dict):
        for key, val in kw.items():
            if d.has_key(key):
                d[key] = val
    elif isinstance(d, object):
        for key, val in kw.items():
            if hasattr(key):
                setattr(d, key, val)
    return True



def split_array(array,sub_len):
    """切割一个array-> array[0][]
        param:array:list:需要切割的数组
        param:sub_len:int:需要切割的大小
        return:[[]]:list:返回双维数组
        test:
            >>> split_array([0,1,2,3,4,5,6,7,8,9],3)
            [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
            >>> split_array("abcddd",3)
            [['a', 'b', 'c'], ['d', 'd', 'd']]
    """
    if is_type(array,(list,tuple,basestring)) is False:
        raise TypeError("Unsupported type: {}".format(type(array).__name__))
    if is_int(sub_len) is False:
        raise TypeError("Unsupported type: {}".format(type(sub_len).__name__))
    items = []
    iter_count = len(array) / sub_len +( 0 if len(array) % sub_len == 0 else 1) 
    for i in range(iter_count):
        items.append([])
        for item in array[i*sub_len:(i+1)*sub_len]: 
           items[i].append(item)
    return items
