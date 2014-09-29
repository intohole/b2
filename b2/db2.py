#coding=utf-8
#!/usr/bin/env python



from num2 import get_random_seq1
import os




def is_lock(file_path , delay = 0.0001  ):
    if file_path == None:
        raise ValueError , 'file_path is empty!'
    if not sinstance(file_path , str ) :
        raise TypeError , 'file_path must be string!'
    if not ( delay and isinstance(delay , int ) and delay > 0  ):
        raise TypeError , 'delay is int and bigger than 0'
    while os.path.exists(file_path):
        time.sleep(delay)


def create_lock(lock_path):
    if is_exist_lock(path):


def __file_filter(path  , fun):
    if path and  os.path.isdir(path):
        for f in os.listdir(path):
            if  fun(f):
                return True
    return False



def is_exist_lock(path = '' ):
    os.listdir(path)
    line = open(path ).readline()
    