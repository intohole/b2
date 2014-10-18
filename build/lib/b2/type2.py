#coding=utf-8








def is_none(value):
    if value == None:
        return True
    return False

def is_type(value , value_type):
    if isinstance(value , value_type):
        return True
    return False


def is_int(value):
    if is_none(value):
        return False
    return is_type(value , int)



def is_str(value):
    if is_none(value):
        return False
    return is_type(value , str)


def is_empty(value):
    if is_none(value):
        return True
    if len(value) > 0 :
        return False
    return True

def is_str_empty(value):
    if is_str(value):
        return False
    return is_empty(value)
    

