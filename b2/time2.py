#coding=utf-8
import time


from exceptions2 import judge_str

def get_time_ms():
    return long(time.time() * 1000)


def get_time_string():
    return time.strftime('%Y-%m-%d %H:%M:%S')


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
    year = ''
    mounth = '01'
    day = '1'
    hour = '00'
    minute = '00'
    sec = '00'

    print time_str.split('[\\/:]')








if __name__ == '__main__':
    timestr_to_time('2013年5月16日12时58分')
    print get_time_ms()
    print get_time_string()