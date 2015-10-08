
import logging
        

def get_stream_logger(  log_level , log_name = None , format = "[%(levelname)s] [%(asctime)s] [%(filename)s] [line : %(lineno)d] [function:%(funcName)s] %(message)s" , date_format = "%Y-%m-%d %H:%M:%S"  ):
    fomatter = logging.Formatter(format , date_format )
    logger = logging.getLogger() if log_name is None else logging.getLogger(log_name)
    log_level =getattr(logging , log_level.upper())   if isinstance(log_level , str) else log_level
    logger.setLevel(log_level) 
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(fomatter)
    logger.addHandler(stream_handler)
    return logger