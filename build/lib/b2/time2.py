#coding=utf-8
import time


from exceptions2 import judge_str
from object2 import enum





TIME_ENUM = enum('MS:1 S:1000 MINUTE:60000 HOUR:360000 DAY:86400000',split_char = ":")



def get_time_ms():
    return long(time.time() * 1000)


def get_time_string():
    return time.strftime('%Y-%m-%d %H:%M:%S')


def get_far_from_wee():
    __now = get_time_ms()
    return __now %  ( 24 * 60 * 1000 )



def get_time_from_now():
    pass



def is_time_string(time_str):
    


def timestr_to_time(time_str):
    judge_str(time_str)
    time_str = time_str.replace('-' , '/')
    time_str = time_str.replace('年' , '/')
    time_str = time_str.replace('月' , '/')
    time_str = time_str.replace('日' , ' ')
    time_str = time_str.replace('小时' , ':' )
    time_str = time_str.replace('时' , ':')
    time_str = time_str.replace('分' , ':')
    time_str = time_str.replace('秒' , '')
    print time_str.split('[\\/:]')








if __name__ == '__main__':
    timestr_to_time('2013年5月16日12时58分')
    print get_far_from_wee()
    print get_time_ms()
    print get_time_string()