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


class BaseColor(dict):

    def __init__(self, show_set, fore_color, back_color):
        self['SET'] = show_set if show_set else 0
        self['FORE'] = fore_color
        self['BACK'] = back_color

    def __str__(self):
        return '\033[%(SET)s;%(FORE)s;%(BACK)sm' % self if self['BACK'] else '\033[%(SET)s;%(FORE)sm' % self if self['FORE'] else '\033[%(SET)sm' % self


class FColor(object):

    def __init__(self, color_set,  fore_color, back_color, base_color):
        self.fore_color = fore_color
        self.color_set = color_set
        self.back_color = back_color
        self.__bc = base_color

    def __add__(self, value):
        if value and isinstance(value, FColor):
            if value.fore_color != None:
                self.__bc['FORE'] = value.fore_color
            if value.back_color != None:
                self.__bc['BACK'] = value.back_color
            if value.color_set != None:
                self.__bc['BACK'] = value.color_set
            return self
        elif value and isinstance(value, (basestring)):
            self.__bc['FORE'] = self.fore_color if self.fore_color != None else self.__bc[
                'FORE']
            self.__bc['BACK'] = self.back_color if self.back_color != None else self.__bc[
                'BACK']
            self.__bc[
                'SET'] = self.color_set if self.color_set != None else self.__bc['SET']
            return '%s%s' % (str(self.__bc), value)

    def __radd__(self, value):
        if value and isinstance(value, basestring):
            return '%s%s' % (value, str(self))

    def __str__(self):
        return str(self.__bc)


class ForeRed(FColor):

    def __init__(self, bc):
        FColor.__init__(self, None, 31, None, bc)


class BackRed(FColor):

    def __init__(self, bc):
        FColor.__init__(self, None, None, 31, bc)


class ForeBlack(FColor):

    def __init__(self, bc):
        FColor.__init__(self, None, 30, None, bc)


class BackBlack(FColor):

    def __init__(self, bc):
        FColor.__init__(self, None, None, 30, bc)


class ForeGreen(FColor):

    def __init__(self, bc):
        FColor.__init__(self, None, 42, None, bc)


class BackGreen(FColor):

    def __init__(self, bc):
        FColor.__init__(self, None, None, 42, bc)


class ForeYellow(FColor):

    def __init__(self, bc):
        FColor.__init__(self, None, 33, None, bc)


class BackYellow(FColor):

    def __init__(self, bc):
        FColor.__init__(self, None, None, 33, bc)


class ForeBlue(FColor):

    def __init__(self, bc):
        FColor.__init__(self, None, 34, None, bc)


class BackBlue(FColor):

    def __init__(self, bc):
        FColor.__init__(self, None, None, 34, bc)


class ForeFuchsia(FColor):

    def __init__(self, bc):
        FColor.__init__(self, None, 35, None, bc)


class BackFuchsia(FColor):

    def __init__(self, bc):
        FColor.__init__(self, None, None, 35, bc)


class ForeCyan(FColor):

    def __init__(self, bc):
        FColor.__init__(self, None, 36, None, bc)


class BackCyan(FColor):

    def __init__(self, bc):
        FColor.__init__(self, None, None, 36, bc)


class ForeWhite(FColor):

    def __init__(self, bc):
        FColor.__init__(self, None, 37, None, bc)


class BackWhite(FColor):

    def __init__(self, bc):
        FColor.__init__(self, None, 37, None, bc)


class DefaultSet(FColor):

    def __init__(self, bc):
        FColor.__init__(self, 0, None, None, bc)


class HgSet(FColor):

    def __init__(self, bc):
        FColor.__init__(self, 1, None, None, bc)


class UnderscoreSet(FColor):

    def __init__(self, bc):
        FColor.__init__(self, 4, None, None, bc)


class BlinkSet(FColor):

    def __init__(self, bc):
        FColor.__init__(self, 5, None, None, bc)


class UnWhiteSet(FColor):

    def __init__(self, bc):
        FColor.__init__(self, 7, None, None, bc)


class HideSet(FColor):

    def __init__(self, bc):
        FColor.__init__(self, 8, None, None, bc)


class Default(FColor):

    def __init__(self, bc):
        FColor.__init__(self, 0, '', '', bc)

    def __str__(self):
        return str(BaseColor(self.color_set, self.fore_color, self.back_color))


class ColorText(object):

    '''
    linux 终端输出有色字体 
    使用方式 ：
            t = ColorText()
            print t.ForeRed + t.BackGreen + 'fore red  back green'
            print  t.ForeRed + t.BackGreen + 'fore red  back green' + t.Default
            print t.Default #清空输出
    '''

    def __init__(self):
        self.__bc = BaseColor(0, '', '')
        self.ForeRed = ForeRed(self.__bc)
        self.BackRed = BackRed(self.__bc)
        self.ForeBlack = ForeBlack(self.__bc)
        self.BackBlack = BackBlack(self.__bc)
        self.ForeGreen = ForeGreen(self.__bc)
        self.BackGreen = BackGreen(self.__bc)
        self.ForeFuchsia = ForeFuchsia(self.__bc)
        self.BackFuchsia = BackFuchsia(self.__bc)
        self.ForeCyan = ForeCyan(self.__bc)
        self.BackCyan = BackCyan(self.__bc)
        self.ForeWhite = ForeWhite(self.__bc)
        self.BackWhite = BackWhite(self.__bc)
        self.DefaultSet = DefaultSet(self.__bc)
        self.HgSet = HgSet(self.__bc)
        self.UnderscoreSet = UnderscoreSet(self.__bc)
        self.BlinkSet = BlinkSet(self.__bc)
        self.UnWhiteSet = UnWhiteSet(self.__bc)
        self.HideSet = HideSet(self.__bc)
        self.Default = Default(self.__bc)
        self.BackGreen = BackGreen(self.__bc)

    def __getitem__(self, name):
        if name and isinstance(name, str):
            return getattr(self, name)
        raise KeyError, 'ColorText hasn\'t attr %s' % name


def get_system_info():
    return sys.platform


def get_python_version():
    '''
    获得python执行环境
    '''
    return '%s.%s.%s.%s.%s' % (sys.version_info.major, sys.version_info.minor, sys.version_info.micro, sys.version_info.serial, sys.version_info.releaselevel)