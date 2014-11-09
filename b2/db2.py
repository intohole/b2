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
        return ValueError , 'file lock %s exists '  % lock_path
    


def _file_filter(path  , fun):
    if path and  os.path.isdir(path):
        for f in os.listdir(path):
            if  fun(f):
                return True
    return False



def is_exist_lock(path):
    return _file_filter(path , lambda x : os.path.split(path)[1].startswith('.lock_'))




if __name__ == '__main__':
    create_lock('.')
    
    