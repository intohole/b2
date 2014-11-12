# coding=utf-8

import re
from datetime import timedelta
from datetime import datetime
import time


def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


class Time2(object):
    __num_pattern = re.compile('^\d+$').match

    def __init__(self):
        pass

    def __sub__(self, value):
        if value is None:
            raise ValueError, 'value is nothing!'
        if isinstance(value, (str, unicode)):
            params = value.strip().split()
            if len(params) == 0:
                raise ValueError, 'sub value is can\'t split  , split char [whitespace ' ', table \\t]'
            index = 0
            params_len = len(params)
            while index < params_len:
                if self.__num_pattern(params[index]):
                    if (index + 1) < params_len:
                        if params[index + 1] == 'years':
                            pass
                        if params[index + 1] == 'days':
                            pass
                        if params[index + 1] == 'months':
                            pass
                        if params[index + 1] == 's':
                            pass
                        if params[index + 1] == 'hours':
                            pass
                        if params[index + 1] == 'mintues':
                            pass


class Years(object):

    def __init__(self, years=time.localtime(time.time()).tm_year):
        self.months = time.localtime(time.time()).tm_month
        self.years = time.localtime(time.time()).tm_year


    @staticmethod
    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


    def __sub__(self , value):
        if not value:
           raise ValueError 
        if isinstance(value , int) and value <= 100 and value > 0 :
            days = 0 
            for i in range(1 , value + 1 ):
                if Years.is_leap_year(self.years - i ):
                    days += 366
                else:
                    days += 365
            return days
                 






if __name__ == '__main__':
    t = Time2()
    # print t - '1 years 10 days'

    date_now = datetime.now()
    print date_now
    print date_now - timedelta(152)
    print Years.is_leap_year(2020)
    y = Years()
    print y - 100
