# coding=utf-8

import re
from datetime import timedelta
from datetime import datetime
from collections import defaultdict


class Date2(object):

    _time_names = [
        'years', 'months', 'days', 'hours', 'minutes', 'seconds', 'weeks']

    def __sub__(self, value):
        if isinstance(value, (str, datetime)):
            now_time = datetime.now()
            if isinstance(value, str):
                time_items = self.parser(value, now_time)
                return now_time - timedelta(**time_items)
            else:
                return now_time - value
        else:
            raise TypeError

    def parser(self, value, base_date):
        items = value.strip().split()
        time_items = defaultdict(int)
        base_date_timetuple = base_date.timetuple()
        for i in range(0, len(items), 2):
            if items[i + 1] not in self._time_names:
                raise ValueError
            time_items[items[i + 1].lower()] = int(items[i])
        for name in self._time_names:
            if name == 'years' and name in time_items.keys():
                base_year = base_date_timetuple.tm_year
                for i in range(time_items['years']):
                    if base_date_timetuple.tm_mon > 2:
                        if Date2.is_leap_year(base_year):
                            base_year -= 1
                            time_items['days']+= 366 
                            continue
                    else:
                        if Date2.is_leap_year(base_year - 1): 
                            base_year -= 1
                            time_items['days'] +=366
                            continue
                    time_items['days'] += 365
                del time_items[name]
            if name == 'months' and name in time_items.keys():
                pass
        return time_items

    @staticmethod
    def is_leap_year(year):
        return ((year % 4 == 0) and (year % 100 != 0)) or year % 400 == 0


if __name__ == '__main__':
    d2 = Date2()
    print(d2 - '1 years 1 days 2 hours').timetuple()
