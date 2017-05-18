#coding=utf-8

import math
import exceptions2

__all__ = ["log2","log10","entropy","ln"]

def log2(num):
    return math.log(num , 2)

def log10(num):
    """log10
        Test:
            >>> log10(None)
            >>> log10(-1.0)
            >>> log10(1.0)
    """
    return math.log(num, 10)

def entropy(props):
    if isinstance(props , (list , type)):
        return sum(-prop * log2(prop) for prop in props)
    elif isinstance(prop , (float , long , int ,double)):
        return -props * log(props)
    raise Exception 
    
def ln(num):
    return math.log(num, math.e)

