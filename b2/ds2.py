# coding=utf-8
#!/usr/bin/env python

'''
主要是一些数据结构的python类 ， 将这些基础类 ， 添加到这个文件中
'''
from exceptions2 import judge_str
import json
import os


class DTNode(dict):

    '''
    trie树Node ，继承词典类别

    '''

    def __init__(self, key=None, value=None):
        if not key == None:
            self[key] = value
        self.value = None

        
    def add(self, key, node):
        if self.has_key(key):
            self[key] = node
        else:
            raise ValueError, 'key not exist!'


class DTrie2(object):

    '''
    一个可以保存状态的trie树 ， 可以从文件或者字符串加载内容 ，
    方便保存任何你想保存的内容 ， 不过只限于字符串
    '''

    def __init__(self, *arg, **kw):
        has_create = False
        if kw.has_key('file'):
            has_create = self.__load_from_file(kw['file'])
            self.__file = kw['file']
        elif kw.has_key('json_string'):
            has_create = self.__load_from_string(kw['json_string'])
        if kw.has_key('fun'):
            if callable(kw['fun']):
                self.fun = kw['fun']
        if has_create == False:
            self.root_node = DTNode()


    def add(self, word , value = None ):
        '''
        添加word字符串到trie树中：
        exception :
               word == None || len(word) < 1 || type(word ) not in [str , unicode]
        如果没有报异常 ， 则添加成功 ， 否则失败
        '''
        judge_str(word, 1, (str, unicode))
        cur_node = self.root_node
        for w in self.to_element(word):
            if not cur_node.has_key(w):
                cur_node[w] = DTNode(w, 0)
                cur_node = cur_node[w]
            else:
                cur_node = cur_node[w]
        if  value:
            cur_node[word[-1]] = value
        else:
            cur_node[word[-1]] +=  self.fun(cur_node[word[-1]])
        

    def search(self, word):
        '''
        查找字符串是否存在word字符串
        exceptions :
                  word == None || len(word) == 0 || type(word) not in [str , unicode]
        如果tree树含有word ， 则返回一个非零值 ， 否则返回false ， 非零值 ， 代表add（word） 次数
        '''
        judge_str(word, 1, (str, unicode))
        cur_node = self.root_node
        for item in self.to_element(word):
            if cur_node.has_key(item):
                cur_node = cur_node[item]
            else:
                return None
        return cur_node[word[-1]] if cur_node[word[-1]] != None else 0

    def get_child_num_level(self , element ):

        cur_node = self.root_node
        level = 0
        for item in self.to_element(element):
            if not cur_node.has_key(item):
                break
            level += 1    
            cur_node = cur_node[item]
        return (0 , 0) if cur_node == root_node else (len(cur_node) , level)


    def __str__(self):
        return str(json.dumps(self.root_node))

    def __getitem__(self, key):
        return self.search(key)

    def __eq__(self, key):
        value = self.search(key)
        return value != None

    def __ne__(self, key):
        return not self.__eq__(key)

    def __load_from_file(self, path):
        judge_str(path, l=2)
        try:
            json_string = open(path).readline().strip()
            self.__load_from_string(json_string)
        except Exception:
            return False
        return True

    def __load_from_string(self, json_string):
        judge_str(json_string, 0)
        try:
            self.root_node = json.loads(json_string)
        except Exception:
            print 'exception'
            return False
        return True

    def to_element(self , element):
        '''
        功能： 将任何一个字符串或者不是字符串转换为list 或者string 结构 ， 方便你将任何字符串类型转换为 ，trie树的node
        子类可以继承
        return   [ list  , tuple , str , unicode ]  __iter__ 
        '''
        return element

    def save(self, path=None):
        save_file = None
        if self.path == None:
            if self.__file == None:
                raise ValueError, 'path not set and class file attr not init !'
            else:
                save_file = self.path
        else:
            save_file = self.path
        judge_str(save_file, 2)
        with open(save_file) as f:
            f.write(str(self))


if __name__ == "__main__":
    t = DTrie2(fun = lambda x :  0 if  x == None else x + 1 )
    # for i in map(123):
    #     print i

    t.add("abcde" , 1000)
    t.add('abca')
    t.add('abca')
    t.add('bcda')


    print t

    a = DTrie2(json_string=str(t))
    t.add('abca')
    print a.search('abca')
    print a.search('abcde')

    print a == 'abca'
    print a.search('a')
    print a.search('c')
    # print a.search('abca')
    # print t.search('abca')
    # print t.search('a')
    # print t
    # print t.find("我爱天安门")
    #
