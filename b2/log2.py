#coding=utf-8



import logging
from object2 import enum2
import time2


__ALL__ = ["get_stream_logger"]

LOG_FORMAT = enum2(DEFAULT="[%(levelname)s] [%(asctime)s] [%(filename)s] [line : %(lineno)d] [function:%(funcName)s] %(message)s")




def get_stream_logger(  log_level , log_name = None , format = LOG_FORMAT.DEFAULT , date_format = time2.TIME_PATTERN.TIME_PATTERN):
    """得到终端log日志
        param:log_level:basestring:log打印等级
        param:log_name:bastring:log名称
        param:format:bastring:日志打印格式
        param:date_format:basestring:日期打印格式
        return:log:logging:日志句柄 
        Test:
            >>> log = get_stream_logger("debug","test")
            >>> log.debug("this is debug")
    """
    fomatter = logging.Formatter(format , date_format )
    logger = logging.getLogger() if log_name is None else logging.getLogger(log_name)
    log_level =getattr(logging ,log_level.upper()) if isinstance(log_level , basestring) else log_level
    logger.setLevel(log_level) 
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(fomatter)
    logger.addHandler(stream_handler)
    return logger
