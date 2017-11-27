#coding=utf-8


import json
import re
import exceptions2

__ALL__ = ["QueryItem" , "JPath"]

class QueryItem(object):

    def __init__(self , argv ,root_path = False):
        self.tag = argv[0]
        self.sub_tag = argv[2]
        self.operator = argv[3]
        self.value = argv[4]
        self.root_path = root_path 
    
    def __str__(self):
        return "root_path={root_path} tag={tag} sub_tag={sub_tag} operator={operator} value={value}".format(tag = self.tag , sub_tag=self.sub_tag , operator = self.operator , value = self.value , root_path = self.root_path )




class JPath(object):

    _parser_regx = re.compile(ur"""^(
            [\w\d\.\*\+_]+
            )(
                \[
                @([\w_\d]+)
                (=|>=|<=|>|<|~){1}
                ([\d\w]+)\]
            )?""" ,re.VERBOSE)


    def __init__(self,query = None):
        self.split_char = "/"
        self.query = query 
        self.query_objs = self._extract_query_item(query) if query else None
    
    def _obj_2_json(self , obj):
        exceptions2.judge_null(obj)
        if isinstance(obj , basestring):
            return json.loads(obj )
        elif isinstance(obj , dict):
            return obj 
        else:
            raise TypeError

    def _extract_query_item(self , query):
        exceptions2.judge_null(query)
        if isinstance(query , basestring):
            return self._parse_query(query)
        elif isinstance(query ,list):
            for _obj in query:
                if isinstance(_obj , QueryItem) is False:
                    raise TypeError("query is QueryItem list , but contain the item isn't QueryItem!")
            return query     
        else:
            raise TypeError("query type is error , query type in [basestring , QueryItem]!")

    def extract(self ,obj ,  query = None):
        """extract dict value like xpath
            param:obj:dict:extract json object
            param:query:basestring:xpath query string
            return:objs:list:match value 
            Test:
               >>> obj = json.loads('{"a":{"b":1 , "c":1} , "d":[{"a":5}]}')
               >>> container = []
               >>> x = JPath()
               >>> x.extract(obj , "//a")
               [{u'c': 1, u'b': 1}, 5]
        """
        obj = self._obj_2_json(obj)
        if query is None and self.query_objs is None:
            raise ValueError("set right query")
        querys = self._extract_query_item(query) if query else self.query_objs
        objs = [obj]
        for query in querys:
            if query.root_path == True :
                objs = [self._find_name(query.tag , obj) for obj in objs]
            else:
                tmpobjs = [] 
                for obj in objs:
                    container = []
                    self._finds_name(query.tag , obj ,container)
                    tmpobjs.extend(container)
                objs = tmpobjs
            if len(objs) != 0 and query.operator and query.sub_tag and query.value:
                objs = [ obj  for obj in objs if self._has_attr(query.sub_tag , obj , query.value , query.operator) ]
            if len(objs) == 0:
                return []
        return objs 
                    
    def _parse_query(self , query):
        """parse query string to query item list
            param:query:basestring:json xpath query
            return:query_list:list:parse query object item list
        """
        query_list = [] 
        query_paths = query.split(self.split_char)
        root_path = True 
        del query_paths[0]
        for qp in query_paths:
            if qp == "" :
                root_path = False
                continue
            query_list.append(QueryItem(self._parser_regx.match(qp).groups() , root_path = root_path))
            root_path = True
        return query_list

    def _finds_name(self , tag , obj , container ):
        """find all object which key is equal to tag
            param:tag:basetring:extract json key
            param:obj:dict:match object
            param:container:list:match value container
            return:None:None:return nothing
        """
        if isinstance(obj , list):
            for _obj in obj:
                self._finds_name(tag , _obj , container)
        elif isinstance(obj , dict):
            self._regx_find_dict(tag , obj , container)
            for key , _obj in obj.items():
                self._finds_name( tag , _obj  , container)
        return 

    def _regx_find_dict(self , tag , obj , container):
        """_has_attr use this function implement ~ , like this
            param:tag:basestring:json dict key
            param:obj:dict:
            param:container:mathch value container
            return:None:None:return Nothing
        """
        tag_pattern = re.compile(tag)
        for name , value in obj.items(): 
            match = tag_pattern.match(name)
            if match:
                container.append(value)
    
    def _has_attr(self , tag , obj , value , operator ):
        """parse attr select functino , like this [@name=="abc"]
            param:tag:basesetring:
            param:obj:dict:
            param:value:object:attr feature value 
            param:operator:basestring:extract value match function operator
            return:match:blooean:if tag value match you want,return True else return False
        """
        if obj and tag in obj:
            extract_value = None
            if isinstance(obj,dict):
                extract_value = obj[tag] 
            elif hasattr(obj,"__getattr__"):
                extract_value = getattr(obj,tag)
            if operator == ">":
                    value = type(obj[tag])(value)
                    return obj[tag] > value 
            elif operator == "=":
                _value = (type(obj[tag])(value))
                return (obj[tag] == _value )
            elif operator == "<":
                value = type(obj[tag])(value)
                return obj[tag] < value 
            elif operator == ">=":
                value = type(obj[tag])(value)
                return obj[tag] >= value 
            elif operator == "<=":
                value = type(obj[tag])(value)
                return obj[tag] <= value 
            elif operator == "~":
                match = re.compile(value).match(str(obj[tag]))
                if match:
                    return True
        else:
            return False

    def _find_name(self , tag , obj ):
        if obj and isinstance(obj , dict):
            if tag in obj:
                return obj[tag]
        return None 
