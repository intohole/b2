# coding=utf-8




import os
from exceptions2 import judge_str, judge_null, judge_type
from system2 import reload_utf8


def isdir(path):
    judge_str(path, 0, (str))
    return os.path.isdir(path)


def mkdir_m(path):
    if path:
        if os.path.exists(path):
            if os.path.isdir(path):
                return True
            else:
                raise ValueError, "path [%s] has been create , but isn't dir !" % path
        else:
            return os.mkdir(path)
    raise ValueError, "path is empty , please check !"


def mkdir_p(path):
    if path:
        _paths = os.path.split(path)
        if len(_paths) == 0:
            return True
        mkdir_path = _paths[0]
        for _path in _paths[1:]:
            mkdir_m(mkdir_path)
            mkdir_path = os.path.join(mkdir_path, _path)
        mkdir_m(mkdir_path)
        return True
    else:
        raise ValueError, "path is none or empty , please check !"


def mkdir_p_child(path, child_path):
    return mkdir_p(os.path.join(path, child_path))


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


def walk_folder(root_path, file_filter=lambda x: true, current_level=0):
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
            current_level += 1
            files.extend(walk_folder(cur_path, file_filter, current_level))
    return files


def _create_folder_map(root_path, file_filter=lambda x: True, cur_level=0, limit_level=None):
    '''
    遍历文件夹文件：
    root_path 遍历文件夹
    file_filter 判断文件是否要收录函数 ， 返回 boolean
    '''
    if limit_level != None:
        if cur_level >= limit_level:
            return
    judge_str(root_path, 1, (str))
    file_map = {}
    for f in os.listdir(root_path):
        cur_path = os.path.join(root_path, f)
        if os.path.isfile(cur_path):
            if file_filter and callable(file_filter):
                if file_filter(cur_path):
                    file_map[f] = 'f'
            else:
                file_map[f] = 'f'
        elif os.path.isdir(cur_path):
            cur_level = cur_level + 1
            file_map[cur_path] = _create_folder_map(
                cur_path, file_filter, cur_level=cur_level)
    return file_map


def create_folder_map(root_path, file_filter=lambda x: True, limit_level=None):
    return {root_path: _create_folder_map(root_path, file_filter, limit_level=limit_level)}


class Files(object):

    '''
    多文件读取文件 ， 生成迭代器  ， 只需要next就可以读入文件夹下的所有文件
    '''

    def __init__(self, **kw):
        if kw.has_key('dirpath'):
            file_filter = lambda x:  True
            if file_filter in kw:
                file_filter = kw['file_filter']
                if not callable(file_filter):
                    raise ValueError, 'file_filter is function judge file accept!'
            self.files = walk_folder(kw['dirpath'], file_filter)
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
            if not os.path.isfile(self.__cur_file_path):
                continue
            self.change_file(self.__cur_file_path)
            self.__filehandle = open(self.__cur_file_path)
            line = self.__filehandle.readline()
        return line

    def change_file(self, file_path):
        pass

    def is_readall(self, files):
        if not files:
            return False
        for f in files:
            if f and isinstance(f, str) and (not os.path.isfile(f)):
                return False
        return True

    def get_current_file(self):
        return self.__cur_file_path
