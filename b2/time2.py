# coding=utf-8
import time
from datetime import datetime
import object2

TIME_ENUM = object2.enum(
    'MS:1 S:1000 MINUTE:60000 HOUR:360000 DAY:86400000', split_char=":")

TIME_PATTERN = object2.enum2(
    TIME_PATTERN = "%Y-%m-%d %H:%M:%S" ,
    TIME_PATTERN_SHORT = "%d/%m/%y %H:%M",
    DATE_FMT_0 = "%Y%m%d",
    DATE_FMT_1 = "%Y/%m/%d",
    DATE_FMT_2 = "%Y/%m/%d %H:%M:%S",
    DATE_FMT_3 = "%Y-%m-%d"
)

def get_timestamp_by_string(time_string , time_pattern):
    return time.mktime(time.strptime(time_string, time_pattern))

def timestamp_2_string(time_stamp , time_pattern):
    return time.strftime(time_pattern,time.localtime(time_stamp))

def get_timestamp():
    return time.time()


if __name__ == "__main__":
    print get_timestamp_by_string("20160830",TIME_PATTERN.DATE_FMT_0)
    print timestamp_2_string(time.time() , TIME_PATTERN.DATE_FMT_0)
