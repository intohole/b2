#coding=utf-8


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


class ConsoleString(object):
    """consle string color format
    """
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

    def __add__(self, value):
        return self.append_string(value)

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
    import tty
    import termios


    """linux终端下，上下左右键信息类
        摘自https://github.com/bfontaine/term2048/blob/master/term2048/keypress.py
    """
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


class BaseColor(dict):

    def __init__(self, show_set, fore_color, back_color):
        self['SET'] = show_set if show_set else 0
        self['FORE'] = fore_color
        self['BACK'] = back_color

    def __str__(self):
        if self['FORE'] is not None and self['BACK'] is not None:
            return '\033[%(SET)s;%(FORE)s;%(BACK)sm' % self
        elif self['FORE'] is not None:
            return  '\033[%(SET)s;%(FORE)sm' % self
        else:
            return '\033[%(SET)sm' % self 

class FColor(object):
    DEFAULT = "\033[0m"
    def __init__(self, base_color, color_set = None,  fore_color = None, back_color = None):
        self.fore_color = fore_color
        self.color_set = color_set
        self.back_color = back_color
        self._bc = base_color

    def __add__(self, value):
        if value and isinstance(value, FColor):
            if value.fore_color is not None:
                self._bc['FORE'] = value.fore_color
            if value.back_color is not None:
                self._bc['BACK'] = value.back_color
            if value.color_set is not None:
                self._bc['SET'] = value.color_set
            return self
        elif value and isinstance(value, (basestring)):
#            self._bc['FORE'] = self.fore_color if self.fore_color != None else self._bc[
#                'FORE']
#            self._bc['BACK'] = self.back_color if self.back_color != None else self._bc[
#                'BACK']
#            self._bc[
#                'SET'] = self.color_set if self.color_set != None else self._bc['SET']
            return '%s%s%s' % (str(self._bc), value,str(self.DEFAULT))

    def __radd__(self, value):
        if value and isinstance(value, basestring):
            return '%s%s' % (value, str(self))

    def __str__(self):
        return str(self._bc)




class ColorText(object):
    
    """consle colorful string format
        test:
            >>> t = ColorText()
            >>> print t.ForeRed + t.BackGreen + 'fore red  back green'
            >>> print t + "this is test"
            >>> t + t.BackRed
            >>> print t + "fore red and back yellow"
    """
    def __init__(self):
        self._bc = BaseColor(0, '', '')
        self.ForeRed = FColor(self._bc, fore_color = 31) 
        self.BackRed = FColor(self._bc, back_color = 41) 
        self.ForeBlack = FColor(self._bc, fore_color = 30) 
        self.BackBlack = FColor(self._bc, back_color = 40)
        self.ForeGreen = FColor(self._bc, fore_color = 32)
        self.BackGreen = FColor(self._bc, back_color = 42)
        self.ForeYellow = FColor(self._bc, fore_color = 33)
        self.BackYellow = FColor(self._bc, back_color = 43)
        self.ForeBlue = FColor(self._bc, fore_color = 34)
        self.BackBlue = FColor(self._bc, back_color = 44)
        self.ForeFuchusia = FColor(self._bc, fore_color = 35)
        self.BackFuchusia = FColor(self._bc, back_color = 45)
        self.ForeCyan = FColor(self._bc, fore_color = 36)
        self.BackCyan = FColor(self._bc, back_color = 46)
        self.ForeWhite = FColor(self._bc, fore_color = 37)
        self.ForeWhite = FColor(self._bc, back_color = 47)
        self.DefaultSet = FColor(self._bc, color_set = 0)
        self.HgSet = FColor(self._bc, color_set = 1)
        self.UnderscoreSet = FColor(self._bc, color_set = 4)
        self.BlinkSet = FColor(self._bc, color_set = 5)
        self.HideSet = FColor(self._bc, color_set = 8)
        self.Default = FColor(self._bc, color_set = 0)
    
    def __getitem__(self, name):
        if name and isinstance(name, str):
            return getattr(self, name)
        raise KeyError, 'ColorText hasn\'t attr %s' % name

    def __add__(self, value):
        if value is None:
            raise ValueError("can't add none type")
        if isinstance(value, (basestring)):
            return '%s%s%s' % (str(self._bc), value,str(FColor.DEFAULT))
        elif isinstance(value,(FColor)):
            if value.fore_color is not None:
                self._bc['FORE'] = value.fore_color
            if value.back_color is not None:
                self._bc['BACK'] = value.back_color
            if value.color_set is not None:
                self._bc['SET'] = value.color_set
    

    def __radd__(self, value):
        if value and isinstance(value, basestring):
            return '%s%s' % (value, str(self))

def get_system_info():
    return sys.platform


def get_python_version():
    """
        test:
            >>> get_python_version()
    """
    return '%s.%s.%s.%s.%s' % (sys.version_info.major, sys.version_info.minor, sys.version_info.micro, sys.version_info.serial, sys.version_info.releaselevel)
