#coding=utf-8



import json 

class JsonXPath(object):
    """实现json xpath简单选择器
    """
    def __init__(self , _json ):
        self.json_object = None
        if isinstance(_json , string):
            self.json_object = json.loads(_json)
        if isinstance(self.json_object , dict) is False:
            raise TypeError

    


    def _parse_query(self , query):
        pass
