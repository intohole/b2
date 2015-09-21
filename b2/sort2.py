#coding=utf-8

from exceptions2 import judge_len
from exceptions2 import judge_type
from exceptions2 import judge_null
from exceptions2 import judge_callable





def sort_map_key(d , get_key_fn = lambda x :x[0] ,desc = False):
    judge_null(d)
    judge_len(d,0)
    judge_callable(get_key_fn)
    judge_type(d , 'must be dict' , (dict))
    return sorted(d.items(), key = get_key_fn , reverse = desc)


def sort_map_value(d , get_key_fn = lambda x :x[1] ,desc = False):
    judge_null(d)
    judge_len(d,0)
    judge_type(d , 'must be dict' , (dict))
    return sorted(d.items() , key = get_key_fn , reverse = desc)

def sort_list_object( l , attr = None , desc = True):
    '''
    对输入的list object 对象进行排序 ， 根据对象属性排序
    '''
    judge_null(l)
    judge_type(l , 'type must be list' , (list))
    judge_null(attr)
    judge_type(attr  , 'attr type must be  str' , (str))
    return sorted(l , lambda x : getattr(x , attr) ,  reverse = desc) 