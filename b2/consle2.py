#coding=utf-8



import sys

class SimpleProgressBar():
    def __init__(self, width=50):
        self.last_x = -1
        self.width = width
 
    def update(self, x):
        assert 0 <= x <= 100 # `x`: progress in percent ( between 0 and 100)
        if self.last_x == int(x): return
        self.last_x = int(x)
        pointer = int(self.width * (x / 100.0))
        sys.stdout.write( '\r%d%% [%s]' % (int(x), '#' * pointer + '.' * (self.width - pointer)))
        sys.stdout.flush()
        if x == 100: print ''


def get_system_info():
    return sys.platform


def get_python_version():
    '''
    获得python执行环境
    '''
    return '%s.%s.%s.%s.%s' % ( sys.version_info.major , sys.version_info.minor , sys.version_info.micro  , sys.version_info.serial , sys.version_info.releaselevel)


if __name__ == '__main__':
    s = SimpleProgressBar()
    # for i in range(101):
    #     s.update(i)

    print get_system_info()
    print get_python_version()[:3]



