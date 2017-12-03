# coding=utf-8




__all__ = ["raiseTypeError","judge_type"]

class MsgException(Exception):


    def __init__(self , msg):
        self._msg = msg 

    def __str__(self):
        return msg 

def _judge_bigger(value, min_num):
    if value < min_num:
        raise ValueError, 'value must be bigger than %s' % min_num

def _judge_min_len(value, l):
    if len(value) < l:
        raise ValueError, "value length must be bigger than %s" % l

def _judge_attr(value , attr_name):
    if hasattr(value , attr_name) is False:
        raise TypeError , "value doesn't have attr [%s]" % attr_name

def judge_type(value , types):
    if isinstance(value, types) is False:
        types_string = ",".join( _t.__name__ for _t in types)  if isinstance(types,(tuple,list)) else types.__name__
        raise TypeError, "value is not right type , type must be [%s]" % types_string 

def judge_value_types(value,types):
    """判断传过来的类型，都是types类型（包括继承）
        param:value:[object]:需要判断的数据
        param:types:class或者class list/tuple:判断类型
        return:None:None
        exception:TypeError
    """
    judge_null(value)
    judge_null(types)
    [judge_type(v,types) for v in value]


def _judge_le_value(value , le_value):
    if value <= le_value:
        raise ValueError , 'value must be less or eaqual %s' % le_value


def _judge_ge_value(value , ge_value = 0):
    if type(value) == type(ge_value) and value < ge_value:
        raise ValueError , 'value must be greate or eaqual %s' % ge_value


def judge_null(value):
    """判断value是否为None或者长度为0;
        params: 
            value             需要判断的value 
        return:
            None 
        raise:
            ValueError        value为None或者长度为空时，抛出异常 
    """
    if value is None:
        raise ValueError, 'value is null!'
    if hasattr(value , "__len__"):
        _judge_le_value(value , 0)


def judge_str(content, l=0, types=(basestring)):
    """判断content为字符串类型 ，长度
    """
    judge_null(content)
    judge_type(content , types)
    judge_min_len(content, l)


def judge_num(num, min_num = None, max_num = None):
    """判断num是否为数字
        params:
            num                 需要判断的数字
            min_num             判断数字最小值
            max_num             判断数字最大区间
        return 
            None
        exception:
            TypeError           如果不是整数类型，抛出异常

    """
    judge_null(num)
    judge_type(num , (int, long))
    if max_num:
        _judge_min(num ,"" , min_num )
    if min_num:
        _judge_bigger(num , "" , max_num )



def judge_smaller(value, max_num):
    judge_null(value)
    judge_null(max_num)
    if value > max_num:
        raise ValueError("value must be smaller than %s" % max_num)



def judge_list(value):
    judge_null(value)
    judge_type(value, (list , tuple))


def judge_callable(value):
    judge_null(value)
    if not callable(value):
        raise ValueError("value must be callable")

def judge_min_len(value , l):
    judge_null(value) 
    judge_num(l , 0)
    _judge_attr(value , "__len__")
    judge_num(len(value) , min_num = l)


def raiseTypeError(value):
    raise TypeError("Unsupport type {}".format(type(value).__name__))
