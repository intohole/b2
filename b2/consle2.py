# coding=utf-8


# import tty
# import termios
import sys
from optparse import OptionParser
from subprocess import call


class SimpleProgressBar():

    def __init__(self, width=50):
        self.last_x = -1
        self.width = width

    def update(self, x):
        assert 0 <= x <= 100  # `x`: progress in percent ( between 0 and 100)
        if self.last_x == int(x):
            return
        self.last_x = int(x)
        pointer = int(self.width * (x / 100.0))
        sys.stdout.write('\r%d%% [%s]' %
                         (int(x), '#' * pointer + '.' * (self.width - pointer)))
        sys.stdout.flush()
        if x == 100:
            print ''


class ConsleString(object):

    '''
    终端颜色字体输出
    主要运用方式为
    cmd = ConsleString()
    cmd.red.black.append_string('hello word!')
    ConsleString.consle_show(cmd)
    但是每写一行要清空字符串的ｂｕｆｆｅｒ
    cmd.clear()
    ConsleString.consle_clear() #清除终端 clear 
    原理 : echo -e 
    特殊字符的颜色字体
    '''
    __strbuffer = []  # 字符串储存　
    __fore_color = False
    __append = False

    def append_string(self, value):
        if self.__strbuffer and not self.__fore_color:
            if self.__strbuffer[len(self.__strbuffer) - 1] != '1m' and self.__strbuffer[len(self.__strbuffer) - 1] != '0m':
                self.__strbuffer.append('1m')
            self.__append = False
            self.__strbuffer.append(value)
        return self

    def clear(self):
        if self.__strbuffer and len(self.__strbuffer) > 0:
            del self.__strbuffer[:]
            self.__append = False
            self.__fore_color = False

    def __getattr__(self, key):
        if not self.__strbuffer:
            self.__strbuffer = list()
        if len(self.__strbuffer) == 0 or not self.__append:
            self.__strbuffer.append('\e[')
            self.__append = True
        self.__color(key, 'black', 30, 40)
        self.__color(key, 'red', 31, 41)
        self.__color(key, 'green', 32, 42)
        self.__color(key, 'yellow', 33, 43)
        self.__color(key, 'blue', 34, 44)
        self.__color(key, 'purple', 35, 45)
        self.__color(key, 'darkgreen', 36, 46)
        self.__color(key, 'white', 37, 47)
        self.__color(key, 'default', 49, 49)
        if key == 'consle':
            self.__strbuffer.append('0m')
        if key == 'hg':
            self.__strbuffer.append('1m')
        if key == 'low':
            self.__strbuffer.append('0m')
        return self

    def __color(self, key, color, fore_gruod, back_ground):
        if key == color:
            if not self.__fore_color:
                self.__strbuffer.append('%d;' % fore_gruod)
                self.__fore_color = True
            else:
                self.__strbuffer.append('%d;' % back_ground)
                self.__fore_color = False

    def __str__(self):
        if self.__strbuffer and isinstance(self.__strbuffer, list):
            if len(self.__strbuffer) > 0 and self.__strbuffer[-1] != '\e[0m':
                self.__strbuffer.append('\e[0m')
            return ''.join(self.__strbuffer)
        else:
            return ''

    def toshow(self):
        ConsleString.consle_show(str(self))

    @staticmethod
    def consle_show(sentence):
        call(['echo', '-e', '%s' % sentence])

    @staticmethod
    def consle_clear():
        call(['clear'])

    @staticmethod
    def consle_move(line):
        call(['echo', '-e', '\33[%dC' % (line)])


class Control(object):

    '''
    这个是网络上抄的　，　摘自https://github.com/bfontaine/term2048/blob/master/term2048/keypress.py
    但是其它部分都是原创　，　打小抄了　．．．
    '''
    UP, DOWN, RIGHT, LEFT = 65, 66, 67, 68

    # Vim keys
    K, J, L, H = 107, 106, 108, 104

    __key_aliases = {
        K: UP,
        J: DOWN,
        L: RIGHT,
        H: LEFT,
    }

    __key_map = {65: 'UP',
                 66: 'DOWN',
                 67: 'RIGHT',
                 68: 'LEFT'
                 }

    def __init__(self):
        self.__fd = sys.stdin.fileno()
        self.__old = termios.tcgetattr(self.__fd)

    def __getKey(self):
        """Return a key pressed by the user"""
        try:
            tty.setcbreak(sys.stdin.fileno())
            termios.tcflush(sys.stdin, termios.TCIOFLUSH)
            ch = sys.stdin.read(1)
            return ord(ch) if ch else None
        finally:
            termios.tcsetattr(self.__fd, termios.TCSADRAIN, self.__old)

    def getKey(self):
        """
        same as __getKey, but handle arrow keys
        """
        k = self.__getKey()
        if k == 27:
            k = self.__getKey()
            if k == 91:
                k = self.__getKey()

        return self.__key_map.get(self.__key_aliases.get(k, k))


def get_system_info():
    return sys.platform


def get_python_version():
    '''
    获得python执行环境
    '''
    return '%s.%s.%s.%s.%s' % (sys.version_info.major, sys.version_info.minor, sys.version_info.micro, sys.version_info.serial, sys.version_info.releaselevel)


if __name__ == '__main__':
    # s = SimpleProgressBar()
    # for i in range(101):
    #     s.update(i)

    # print get_system_info()
    # print get_python_version()[:3]
    print 'hello world!'
    today = '奇怪'
    
    if today == '天晴':
        print '我们出去溜达!'
    elif today == '阴':
        print '我们不出去了!'
    else:
        print '我们也不知道干嘛了！'
