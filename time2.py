#coding=utf-8
import time



def get_time_ms():
    return long(time.time() * 1000)


def get_time_string():
    return time.strftime(time.time())



if __name__ == '__main__':
    print get_time_string()