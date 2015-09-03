#!/usr/bin/env python
#coding=utf-8

import pymongo

class DBObject(dict):
    
    def __init__(self):
        dict.__init__(self)
        
    def put(self,key,val):
        self[key] = val
    
    def containsField(self,key):
        return self.containsField(key)
         
    def get(self,key,default=None):
        if self.containsField(key) == True:
            return self[key]
        else:
            return default
    
    def putAll(self,d):
        if isinstance(d, dict):
            for _key,_value in d.items():
                self[_key] = _value   
             
    
class MongoDB():
    
    def __init__(self ,database , db_col ,  host = 'localhost' ,port = 27017 ):
        self.conn = pymongo.MongoClient('mongodb://%s:%s' % ( host ,port))
        self.db = self.conn[database]
        self.table = self.db[db_col]
    
    def find(self,condition=None):
        if condition == None:
            return self.table.find()
        return self.table.find(condition)
    def findLimit(self,count=500,condition=None):
        if condition == None:
            return self.table.find().limit(count)
        return self.table.find(condition).limit(count)
    def getcount(self,condition=None):
        if condition == None:
            return self.table.find().count()
        return self.table.find(condition).count()  
    def insert(self,query):
        return self.table.insert(query)
    
    def findone(self,contidon=None):
        if contidon == None:
            return self.table.find_one()
        return self.table.find_one(contidon)
        
    def remove(self,contidon=None):
        if contidon == None:
            return self.table.remove()
        return self.table.remove(contidon)
    
    def update(self,contidon,updatevalue):
        setDBObj = DBObject()
        setDBObj.put('$set',updatevalue)
        return self.table.update(contidon,setDBObj)
    
    def upsert(self,contidon,updatevalue):
        setDBObj = DBObject()
        setDBObj.put('$set',updatevalue)
        return self.table.update(contidon,setDBObj,upsert=True)
    
    def updateMulti(self,contidon,updatevalue):
        setDBObj = DBObject()
        setDBObj.put('$set',updatevalue)
        return self.table.update(contidon,setDBObj,multi=True)
    
    def upsertMulti(self,contidon,updatevalue):
        setDBObj = DBObject()
        setDBObj.put('$set',updatevalue)
        return self.table.update(contidon,setDBObj,upsert=True,multi=True)
             
    
    def closeDB(self):
        if self.conn:
            self.conn.close()
