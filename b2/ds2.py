# coding=utf-8
#!/usr/bin/env python


import exceptions2
import json
import os
import str2

__ALL__ = ["DTrie","Huffman"]

"""some base data struct implment by python
"""

class DTNode(dict):

    def __init__(self , *argv , **kw):
        super(DTNode , self).__init__(*argv , **kw)
        self.value = None 
        self.count = 0 

class DTrie(object):
    """dict trie implment
        Test:
            >>> tree = DTrie()
            >>> tree.add("abcdd")
            1
            >>> tree.add("abeca")
            1
            >>> tree.contain("abcdd")
            True
            >>> tree.contain("abc")
            False
            >>> tree.contain("abca")
            False
            >>> tree.get("abcdd")
            (True, 1, None, '')
            >>> "ab" in tree
            False
            >>> tree["ab"]
            (False, 0, None, '')
            >>> tree.getChildNum("ab")
            2
    """
    def __init__(self, *arg, **kw):
        self.root_node = DTNode()


    def add(self, word,value=None):
        """add string 2 dict tree
            param:word:basestring:add word
            param:value::value dict tree node save 
            return:(boolean,msg):if add success return true ,otherway return fasel,msg is error msg
        """
        if str2.isBlank(word):
            return -1 
        if isinstance(word,basestring):
            tmp_node = self.root_node 
            for w in self.to_element(word):
                if w not in tmp_node:
                    tmp_node[w] = DTNode() 
                tmp_node = tmp_node[w]
            tmp_node.value = value 
            tmp_node.count += 1
            return tmp_node.count
    
    def get(self,word):
        if str2.isBlank(word):
            return (False,None,None,"empty string or unsupport type , please check")
        if isinstance(word,basestring):
            tmp_node = self.root_node
            for item in self.to_element(word):
                if item not in tmp_node:
                    return (False,0,None,"")
                tmp_node = tmp_node[item]
            return (True,tmp_node.count,tmp_node.value,"") if tmp_node.count != 0 else (False,tmp_node.count,None,"")
        return (False,0,None,"word type is unsupport type")
            
         
    def contain(self, word):
        if str2.isBlank(word):
            return False
        if isinstance(word,basestring):
            tmp_node = self.root_node
            for item in self.to_element(word):
                if item not in tmp_node:
                    return False
                tmp_node = tmp_node[item]
            return tmp_node.count != 0
   
    def getChildNum(self,word):
        if str2.isBlank(word):
            return False 
        if isinstance(word,basestring):
            tmp_node = self.root_node
            for item in self.to_element(word):
                if item not in tmp_node:
                    break 
                tmp_node = tmp_node[item]
            return 0. if tmp_node == self.root_node else len(tmp_node) 
        
    def __setitem__(self,word,value):
        return self.add(word,value)
    
    def __str__(self):
        return str(json.dumps(self.root_node))

    def __getitem__(self, key):
        return self.get(key)
    
    def __contains__(self, key):
        return self.contain(key)

    def __eq__(self, key):
        return self.contain(key)

    def __ne__(self, key):
        return not self.contain(key)

    def to_element(self, element):
        return element



class Huffman(object):
    from collections import defaultdict

    def __init__(self):
        self._tree = None
        self._attr = defaultdict(int)

    def append(self,value):
        if value:
            for c in value:
                self._attr[c] += 1


    def get(self,value):
        pass

   def _restruct(self):
       pass
