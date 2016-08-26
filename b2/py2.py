#coding=utf-8

from Queue import Queue
import threading
from datetime import datetime

class RateHourQueue(Queue):

    def __init__(self, *argv , **kw):
        Queue.__init__(self,*argv)
        self.__count = 0
        self.limit = kw.get("hour_rate",300)
        self.__time = self.get_current_hour()
        self.lock = threading.Lock()

    def get_current_hour(self):
        now = datetime.now()
        return now.hour

    def get(self):
        with self.lock:
            while True:
                cur_time = self.get_current_hour()
                if self.__time != cur_time:
                    self.__count = 1
                    return Queue.get(self)
                if self.__count >= self.limit:
                    time.sleep(5)
                    continue
                if self.__count < self.limit:
                    self.__count += 1
                    return Queue.get(self)


if __name__ == "__main__":
    t = RateHourQueue()
    t.put("1")
    t.put("2")
    print t.get()
