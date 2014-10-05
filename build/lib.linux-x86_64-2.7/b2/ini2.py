#coding=utf-8
#!/usr/bin/env python

import os
import re
'''
python ini 文件解析
作者 ; 李
'''
class NoFilePathORNotExist(Exception):
    pass

class NoOpinionName(Exception):
    pass

class SectionPatternException(Exception):
    pass

class PatternException(Exception):
    pass

class NoSectionNameException(Exception):
    pass

class NoValueNameException(Exception):
    pass

class opinion():
    
    def __init__(self , key , value , comment = ''):
        self._opinion = key
        self._value = value
        self._comment = comment 
        
    def __str__(self):
        return '%s=%s' % (self._opinion , self._value)

class comment():
    
    def __init__(self , comment):
        self.comment = comment
        
    def __str__(self):
        return self.comment
        

class Section():
    __opinions = {}
    __name = ''
    
    
    def get_sections(self):
        return self.__name
    
    def get_opinion(self , key):
        if self.__data.has_key(key):
            return self.__data['key']
        else:
            raise NoOpinionName,key
    
            

class Ini2():
    __data = {}
    
    def add_opinion(self,sectionname , key , value):
        if not self.__data.has_key(sectionname):
            self.__data[sectionname] = {}
        self.__data[sectionname][key] = value
    
    def get_value(self,sectionname , key):
        if sectionname or key:
            raise  TypeError,'sectionname = %s , key = %s' % (sectionname , key)
        sectionname = '%s' % sectionname
        key = '%s' % key
        if self.__data.has_key(sectionname):
            if self.__data[sectionname].has_key(key):
                return self.__data[sectionname][key]._value
            else:
                raise NoValueNameException,key
        else:
            raise NoSectionNameException,sectionname
    
    def get_sections(self):
        return self.__data.keys()
    
    def get_section_opinion(self ,section):
        if self.__data.has_key(section):
            return self.__data[section].keys()
        raise NoSectionNameException,section
    
    def get_default_value(self , sectionname,value,default = None):
        _value = default 
        try:
            _value = self.get_value(sectionname,value)
        except Exception,_:
            pass
        return _value
    
    def get_boolean_value(self ,  key , sectionname = ''):
        value = self.get_value(sectionname, key)
        if value.lower() == 'false':
            return False
        elif value.lower() == 'true':
            return True
        else:
            raise TypeError,value
    
    def get_long_value(self ,  key , sectionname= ''):
        return long(self.get_value(sectionname, key))
    
    
    def get_int_value(self, key  ,sectionname = ''):
        return int(self.get_value(sectionname, key))
    
    
    
    def get_string_value(self , key ,sectionname = '' ):
        return self.get_value(sectionname, key)
           
    
    def __str__(self):
        _msg = ''
        for _sec,_opi in self.__data.items():
            _msg = '%s[%s]\n' % (_msg,_sec)
            for _key,_val in _opi.items():
                if _val != '' :
                    _msg = _msg + '%s=%s ; %s\n' % (_val._opinion,_val._value , _val._comment)
                else:
                    _msg = _msg + '%s=%s\n' % (_val._opinion,_val._value )
        return _msg
    

class PyIni(object):
    
    __path = None
    __content = []
    _config = Config()
    __load = False
    __comments = []
    __section_pattern = re.compile('\\[[\u4e00-\u9fa5a-zA-Z0-9_ ]+\\]', re.IGNORECASE)
    
    
    
    def __init__(self , filepath ,comment = '#' , config_split = '='):
        if not (filepath and os.path.exists(filepath) and os.path.isfile(filepath)):
            raise NoFilePathORNotExist,filepath
        self.__path = filepath
        self.__read()
        self.__parser()
        
        
    
    
    def __read(self):
        if self.__load:
            return 
        with open(self.__path) as f:
            self.__content.extend([line.strip() for line in f.readlines()])
    
    
    def __parser(self):
        _sectionname = ''
        for line in self.__content:
            if not self.__empty(line):
                if line.startswith(';'):
                    self.__comments.append(line)
                elif line.startswith('[') and line.endswith(']'):
                    section_match = self.__section_pattern.match(line)
                    if section_match:
                        _sectionname = section_match.group()[1:-1]
                    else:
                        raise SectionPatternException,line
                else:
                    lineArry = line.split(';')
                    comment = ''
                    if len(lineArry) > 1:
                        comment = ''.join(lineArry[1:])
                    lineArry[0] = lineArry[0].strip()
                    opinionArry = lineArry[0].split('=')
                    op = opinion(opinionArry[0].strip(), opinionArry[1].strip(),comment)
                    self._config.add_opinion(_sectionname,opinionArry[0], op)
        return self._config
                            
    
    def __empty(self ,  line):
        if not line or line.strip() == '':
            return True
        return False
if __name__ == "__main__":
    ini = PyIni('/home/lixuze/config.ini')
    print ini._config.get_string_value(9,'avc')