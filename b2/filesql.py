#coding=utf-8

from exceptions2 import judge_str






   
class FileSql(object):


    __head = ['select' , 'update' , 'delete']
    __keywords = ['from' , 'where' ]
    __function = ['count' , 'max' , 'min']



    def excute(self , sql):
        judge_str(sql)
        sql_params  = sql.lower().strip().split()
        if sql_params[0] in sel.__head:
            if sel_params[0] == self.__head[1]:



    def __from_file(self , data_source):
        with open(data_source) as f:
            




if __name__ == '__main__':
    f = FileSql()
    f.excute('select $1 From xx')





