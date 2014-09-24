#coding=utf-8

from exceptions2 import judge_str , judge_null , judge_type
import os
from system2 import reload_utf8
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


def walk_folder(root_path  ,fun = lambda x : true):
    '''
    遍历文件夹文件：
    root_path 遍历文件夹
    fun 判断文件是否要收录函数 ， 返回 boolean
    '''
    judge_str(root_path , 1 , (str))
    files = []
    for f in os.listdir(root_path):
        cur_path = os.path.join(root_path , f)
        if os.path.isfile(cur_path):
            if fun and callable(fun) :
                if fun(cur_path):
                    files.append(cur_path)
            else:
                files.append(cur_path)
        elif os.path.isdir(cur_path):
            files.extend(walk_folder(cur_path , fun ) )
    return files


def _create_folder_map(root_path  ,fun = lambda x : True):
    '''
    遍历文件夹文件：
    root_path 遍历文件夹
    fun 判断文件是否要收录函数 ， 返回 boolean
    '''
    judge_str(root_path , 1 , (str))
    file_map = {}
    # file_map[root_path] = dict()
    for f in os.listdir(root_path):
        cur_path = os.path.join(root_path , f)
        if os.path.isfile(cur_path):
            if fun and callable(fun) :
                if fun(cur_path):
                    file_map[f] = 'f'
            else:
                file_map[f] = 'f'
        elif os.path.isdir(cur_path):
            file_map[cur_path] = _create_folder_map(cur_path , fun ) 
    return file_map

def create_folder_map(root_path , fun = lambda x : true):
    return {root_path : _create_folder_map(root_path , fun)}


class Files(object):
    '''
    多文件读取文件 ， 生成迭代器  ， 只需要next就可以读入文件夹下的所有文件
    '''

    def __init__(self , **kw):
         

         pass
        



    def __iter__(self):
        return self 



if __name__ == '__main__':
    # mkdir_p('d:/work_space/p2')
    # reload_utf8()
    print walk_folder('D:\\workspace\\b2' ,  lambda x :  x.endswith('py') )
    print create_folder_map('d:\\workspace\\b2' , lambda x :  x.endswith('py'))
    # a = lambda x : x.endswith('bb')

    # print a('aa')
    # print a('bb')
    print 'D:\\workspace\\b2\\.git\\COMMIT_EDITMSG'.endswith('py')

