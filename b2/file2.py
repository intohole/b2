# coding=utf-8

from exceptions2 import judge_str, judge_null, judge_type
import os
from system2 import reload_utf8


def isdir(path):
    judge_str(path, 0, (str))
    return os.path.isdir(path)


def mkdir_p(path, path_pattern='/'):
    paths = path_pattern.split(path_pattern)
    print paths


def write(lines,  path, overwrite=True, join_str='\n'):
    judge_str(line, 1, (str))
    judge_str(path, 1, (str))
    judge_null(lines)
    judge_type(
        lines, 'lines type [list , tuple , str , unicode]', (list, tuple, str, unicode))
    if os.path.exists(path) and overwrite == False:
        raise ValueError, 'path is exists! %s' % path
    with open(path, 'w') as f:
        if isinstance(lines, (str, unicode)):
            f.write(lines)
        else:
            f.write(join_str.join([line for line in lines]))


def walk_folder(root_path, file_filter=lambda x: true):
    '''
    遍历文件夹文件：
    root_path 遍历文件夹
    file_filter 判断文件是否要收录函数 ， 返回 boolean
    '''
    judge_str(root_path, 1, (str))
    files = []
    for f in os.listdir(root_path):
        cur_path = os.path.join(root_path, f)
        if os.path.isfile(cur_path):
            if file_filter and callable(file_filter):
                if file_filter(cur_path):
                    files.append(cur_path)
            else:
                files.append(cur_path)
        elif os.path.isdir(cur_path):
            files.extend(walk_folder(cur_path, file_filter))
    return files


def _create_folder_map(root_path, file_filter=lambda x: True):
    '''
    遍历文件夹文件：
    root_path 遍历文件夹
    file_filter 判断文件是否要收录函数 ， 返回 boolean
    '''
    judge_str(root_path, 1, (str))
    file_map = {}
    # file_map[root_path] = dict()
    for f in os.listdir(root_path):
        cur_path = os.path.join(root_path, f)
        if os.path.isfile(cur_path):
            if file_filter and callable(file_filter):
                if file_filter(cur_path):
                    file_map[f] = 'f'
            else:
                file_map[f] = 'f'
        elif os.path.isdir(cur_path):
            file_map[cur_path] = _create_folder_map(cur_path, file_filter)
    return file_map


def create_folder_map(root_path, file_filter=lambda x: True):
    return {root_path: _create_folder_map(root_path, file_filter)}


class Files(object):

    '''
    多文件读取文件 ， 生成迭代器  ， 只需要next就可以读入文件夹下的所有文件
    '''

    def __init__(self, **kw):
        if kw.has_key('dirpath'):
            if kw.has_key('file_filter'):
                file_filter = lambda x:  True
                if not (kw['file_filter'] and callable(kw['file_filter'])):
                    raise ValueError, 'file_filter is function judge file accept!'
                else:
                    file_filter = kw['file_filter']
            self.files = walk_folder(kw['dirpath'], kw['file_filter'])
        elif kw.has_key('files'):
            if self.is_readall(kw['files']):
                self.files = kw['files']
            else:
                raise ValueError, 'files is list and all is file path which exists!'
        self.__filehandle = None
        self.__file_index = -1
        self.__line_cache = []
        self.__cur_file_path = None

    def __iter__(self):
        return Files(files=self.files)

    def next(self):
        line = self.get_line()
        if not line:
            raise StopIteration, 'files has no content to read!'
        return line.strip('\n')

    def __get_cur_line(self):
        if self.__filehandle:
            return self.__filehandle.readline()
        return None

    def get_line(self):
        line = self.__get_cur_line()
        while not line and self.__file_index < (len(self.files) - 1):
            self.__file_index += 1
            if self.__filehandle:
                self.__filehandle.close()
            self.__cur_file_path = self.files[self.__file_index]
            self.__filehandle = open(self.files[self.__file_index])
            line = self.__filehandle.readline()
        return line

    def is_readall(self, files):
        if files:
            for f in files:
                if f and isinstance(f, str):
                    if not os.path.isfile(f):
                        return True
            return True
        return False


    def get_current_file(self):
        return self.__cur_file_path


if __name__ == '__main__':
    # mkdir_p('d:/work_space/p2')
    # reload_utf8()
    # print walk_folder('D:\\workspace\\b2', lambda x:  x.endswith('py'))
    # print create_folder_map('d:\\workspace\\b2', lambda x:  x.endswith('py'))
    # a = lambda x : x.endswith('bb')

    # print a('aa')
    # print a('bb')
    # print 'D:\\workspace\\b2\\.git\\COMMIT_EDITMSG'.endswith('py')
    for line  in Files(dirpath='D:\\workspace\\b2', file_filter=lambda x:  x.endswith('py')):
        print line 