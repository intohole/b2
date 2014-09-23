#coding=utf-8

from exceptions2 import judge_str , judge_null , judge_type
import os

def isdir(path):
    judge_str(path , 0 , (str))
    return os.path.isdir(path)


def mkdir_p(path , path_pattern = '/'):
    paths = path_pattern.split(path_pattern)
    print paths


def write(lines ,  path , overwrite = True ,join_str = '\n'):
    judge_str(line  , 1 , (str))
    judge_str(path , 1 , (str))
    judge_null(lines)
    judge_type(lines , 'lines type [list , tuple , str , unicode]' , (list , tuple , str , unicode))
    if os.path.exists(path) and overwrite  ==  False:
        raise ValueError , 'path is exists! %s' % path
    with open(path , 'w') as f:
        if isinstance(lines , (str , unicode)):
            f.write(lines)
        else:
            f.write(join_str.join([line for line in lines]))



if __name__ == '__main__':
    mkdir_p('d:/work_space/p2')

