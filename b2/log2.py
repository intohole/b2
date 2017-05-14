#coding=utf-8



import logging

__ALL__ = ["get_stream_logger"]

def get_stream_logger(  log_level , log_name = None , format = "[%(levelname)s] [%(asctime)s] [%(filename)s] [line : %(lineno)d] [function:%(funcName)s] %(message)s" , date_format = "%Y-%m-%d %H:%M:%S"  ):
    """得到终端log日志
        param:log_level:basestring:log打印等级
        param:log_name:bastring:log名称
        param:format:bastring:日志打印格式
        param:date_format:basestring:日期打印格式
        return:log:logging:日志句柄 
        Test:
            >>> log = get_stream_logger("info","test")
            >>> log.debug("this is debug")
    """
    fomatter = logging.Formatter(format , date_format )
    logger = logging.getLogger() if log_name is None else logging.getLogger(log_name)
    print log_level.upper()
    log_level =getattr(logging ,log_level.upper()) if isinstance(log_level , basestring) else log_level
    logger.setLevel(log_level) 
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(fomatter)
    logger.addHandler(stream_handler)
    return logger



if __name__ == "__main__":
    log = get_stream_logger("info")
    print log.level
    print logging.INFO
    log.debug("this is debug")
    log.warn("this is warn") 
    log.error("this is error")
 
