#coding=utf-8


import json


class JsonXpath(object):


    def __init__(self , obj ):
        if obj and isinstance(obj , basestring):
            obj = json.loads(obj)
        if obj is None or isinstance(obj , dict) is False:
            raise TypeError

    
    def extract(self , query ):
        """
        """
        if query and isinstance(query , basestring):
            pass 
        raise TypeError

    def _finds_name(self , tag , obj , container ):
        if isinstance(obj , list):
            for _obj in obj:
                self._finds_name(tag , _obj , container)
        elif isinstance(obj , dict):
            if tag in obj:
                container.append(obj[tag])
            for key , _obj in obj.items():
                self._finds_name( tag , _obj  , container)
        return 

    def _find_name(self , tag , obj ):
        if obj and isinstance(obj , dict):
            if tag in obj:
                return obj[tag]
        return None 
if __name__ == "__main__":

    x = JsonXpath('{"a":"c"}')
    obj = {"a" :[{"b":{"c":1}} , {"b":{"c" , 2}}]}
    container = []
    x._finds_name("b" , obj , container)
    print container
