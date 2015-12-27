#coding=utf-8


import json
import re

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
            self.regx_find_dict(tag , obj , container)
            for key , _obj in obj.items():
                self._finds_name( tag , _obj  , container)
        return 

    def regx_find_dict(self , tag , obj , container):
        tag_pattern = re.compile(tag)
        for name , value in obj.items(): 
            match = tag_pattern.match(name)
            if match:
                container.append(value)
        return 

    def _find_name(self , tag , obj ):
        if obj and isinstance(obj , dict):
            if tag in obj:
                return obj[tag]
        return None 
if __name__ == "__main__":

    x = JsonXpath('{"a":"c"}')
    obj = {"a" :[{"b":{"c":1}} , {"b":{"c" , 2}}]}
    obj = json.loads('''{
    "store": {
        "book": [
            {
                "category": "reference",
                "author": "Nigel Rees",
                "title": "Sayings of the Century",
                "price": 8.95
            },
            {
                "category": "fiction",
                "author": "Evelyn Waugh",
                "title": "Sword of Honour",
                "price": 12.99
            },
            {
                "category": "fiction",
                "author": "Herman Melville",
                "title": "Moby Dick",
                "isbn": "0-553-21311-3",
                "price": 8.99
            },
            {
                "category": "fiction",
                "author": "J. R. R. Tolkien",
                "title": "The Lord of the Rings",
                "isbn": "0-395-19395-8",
                "price": 22.99
            }
        ],
        "bicycle": {
            "color": "red",
            "price": 19.95
        }
        },
    "expensive": 10
    }''')
    container = []

    x._finds_name("author" , obj , container)
    print container
