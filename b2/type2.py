# coding=utf-8


def is_none(value):
    if value == None:
        return True
    return False


def is_type(value, value_type):
    if isinstance(value, value_type):
        return True
    return False


def is_int(value):
    if is_none(value):
        return False
    return is_type(value, int)


def is_str(value):
    if is_none(value):
        return False
    return is_type(value, str)


def is_empty(value):
    if is_none(value):
        return True
    if len(value) > 0:
        return False
    return True


def is_str_empty(value):
    if is_str(value):
        return False
    return is_empty(value)


def is_collection(value):
    '''
    判断是否collection
    返回：
       如果 非None and 有属性 __iter__ ,且不是字符串 ， 返回True
       否则 ， False
    '''
    if value:
        if hasattr(value, '__iter__') and not isinstance(value, basestring):
            return True
    return False


def _get_default(self, data, default=0, *argv):
    '''
    得到一个词典中
    eg. a = {1:{2:3}}
    _get_default(a , 0 , 1 , 2) # 3
    _get_default(a , 'a' , 1, 2) # 0  
    '''
    node = data
    for name in argv:
        if node.has_key(name):
            node = data[name]
        else:
            return default
    return node if node and isinstance(node, type(default)) else default


def update_config(d, **kw):
    '''
    更新词典或者类内部属性
    参数:
        d 
            需要更新的数据项
        kw  
            需要更新数据项的{名称 : val }
    异常：
        如果为none ， 抛出异常
    返回：
        return None 
    '''
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


if __name__ == '__main__':
    print range(-5)
