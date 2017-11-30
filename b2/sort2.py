#coding=utf-8

from exceptions2 import judge_type
from exceptions2 import judge_null
from exceptions2 import judge_callable





def sort_map_key(d , get_key_fn = lambda x :x[0] ,desc = False):
    judge_null(d)
    judge_callable(get_key_fn)
    judge_type(d , (dict))
    return sorted(d.items(), key = get_key_fn , reverse = desc)


def sort_map_value(d , get_key_fn = lambda x :x[1] ,desc = False):
    judge_null(d)
    judge_type(d , (dict))
    return sorted(d.items() , key = get_key_fn , reverse = desc)

def sort_list_object( l , attr = None , desc = True):
    judge_null(l)
    judge_type(l , (list))
    judge_null(attr)
    judge_type(attr, (str))
    return  sorted(l,reverse = desc) if attr is None else sorted(l , key = lambda x : getattr(x , attr) ,  reverse = desc)
