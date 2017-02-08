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
