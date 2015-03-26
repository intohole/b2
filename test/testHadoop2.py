#coding=utf-8


import os





class Utils(object):



    @staticmethod
    def file_filter(filter = None ,filter = None , path = os.path.dirname(__file__)  ):
        for f in os.listdir(path):
            






class Command(dict):
    pass



class FSCommand(Command):


    






class HadoopCommand(object):



    def __init__(self , hadoop_home = os.getenv('HADOOP_HOME')):
        if not ( hadoop_home and os.path.isdir(hadoop_home)):
            raise ValueError , 'HADOOP_HOME path does\'nt exist ! %s ' % hadoop_home
        self.hadoop_home = hadoop_home


