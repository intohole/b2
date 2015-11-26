# coding=utf-8


from os import path
from os.path import dirname
from urlparse import urlparse
import os 

def _max_string_starts(*argv):
    return path.commonprefix(argv)


def get_hdfs_dir(hdfs):
    return os.path.dirname(urlparse(hdfs).path)


def get_hdfs_path(hdfs):
    return get_hdfs_dir( urlparse(hdfs).path) 


def get_max_common_prefix(*argv):
    return os.path.commonprefix(argv) if len(argv) > 1 and argv != None else 0

def get_sign( input_file, main_data, sec_data ):
     '''
     找出最大公共前缀作为标志区分位 
     '''
     main_common_len = len(get_max_common_prefix(
         get_hdfs_path(input_file),
         get_hdfs_path(main_data)
     ))
     sec_common_len = len(get_max_common_prefix(
         get_hdfs_path(input_file),
         get_hdfs_path(sec_data)
     ))     
     if main_common_len == 0 or sec_common_len == 0:
         log('main data [%s] is wrong or    second data [%s] is wrong' % (
             main_data, sec_data))
     elif main_common_len > sec_common_len:
         return 'main'
     elif sec_common_len > main_common_len:
         return 'sec'
     elif main_common_len == sec_common_len:
         '''
         '''
         if input_file.startswith(main_data):
             return 'main'
         elif input_file.startswith(sec_data):
             return 'sec'
         else:
             log('input file [%s]  main data [%s]   second data [%s] is samepath' % (
                 input_file, main_data, sec_data))
             sys.exit(1)
     else:
         log('input file [%s]  main data [%s]   second data [%s] is wrong !!! check !' % (
             input_file, main_data, sec_data))
     return sign
def log( msg):
    sys.stderr.write(msg)
    sys.stderr.flush()
