#coding=utf-8

import math



def log2(num):
    return math.log(num , 2)



def entropy(props):
    if isinstance(props , (list , type)):
        return sum(-prop * log2(prop) for prop in props)
    elif isinstance(prop , (float , long , int ,double)):
        return -props * log(props)
    raise Exception 

