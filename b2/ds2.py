# coding=utf-8
#!/usr/bin/env python

'''
主要是一些数据结构的python类 ， 将这些基础类 ， 添加到这个文件中
'''
from exceptions2 import judge_str
import json
import os

__ALL__ = ["DTrie2"]

class DTNode(dict):

    def __init__(self , *argv , **kw):
        super(DTNode , self).__init__(*argv , **kw)
        self.weight = None 


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
        self.path = None
        if kw.has_key('path'):
            self.path = kw['path']

    def add(self, word, value=None):
        """添加word到词典树中
            params:
                word                添加字符串
                value               添加的数值
            return
        """
        judge_str(word, 1, (str, unicode))
        cur_node = self.root_node
        elements = self.to_element(word)
        for w in elements:
            if w not in cur_node:
                cur_node[w] = DTNode()
                cur_node = cur_node[w]
            else:
                cur_node = cur_node[w]
        cur_node.value = value 
        return value 

    def search(self, word):
        judge_str(word, 1, (str, unicode))
        cur_node = self.root_node
        elements = self.to_element(word)
        for item in elements:
            if item not in  cur_node:
                return None
            cur_node = cur_node[item]
        return cur_node 

    def get_child_num_level(self, element):
        cur_node = self.root_node
        level = 0
        for item in self.to_element(element):
            if not cur_node.has_key(item):
                break
            level += 1
            cur_node = cur_node[item]
        return (0, 0) if cur_node == root_node else (len(cur_node), level)

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
            return False
        return True

    def to_element(self, element):
        return element

    def save(self, path=None):
        save_file = None
        if self.path == None:
            if self.path == None:
                raise ValueError, 'path not set and class file attr not init !'
            else:
                save_file = self.path
        else:
            save_file = self.path
        judge_str(save_file, 2)
        with open(save_file) as f:
            f.write(str(self))
