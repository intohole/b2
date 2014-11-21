#coding=utf-8

#!/usr/bin/env python


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
            self.__bc['FORE'] = self.fore_color if self.fore_color != None else self.__bc['FORE']
            self.__bc['BACK'] = self.back_color if self.back_color != None else self.__bc['BACK']
            self.__bc['SET'] = self.color_set if self.color_set != None else self.__bc['SET']
            return '%s%s' % (str(self.__bc), value)
    def __radd__(self , value):
        if value and isinstance(value , basestring):
            return '%s%s' % ( value , str(self))

    # def __or__(self , value):
    #     if value  and isinstance(value , FColor):

    #         return BaseColor( if self.__bc['Set']  ,  )

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



if __name__ == '__main__':
    t = ColorText()
    a = [10 , 11 ,4 , 6 ,  21 , 15 , 77]
    high = max(a)
    for i in range(high):
        buf = []
        for j in range(len(a)):
            if (high - i )   >= a[j]:
                buf.append(  ' ' + t.Default )
                continue
            buf.append( t.ForeRed + t.BackGreen + ' ' + t.Default)
        buf.append( ' ' + t.Default )
        print ''.join(buf)
    a = [1 , 11 ,4 , 6 ,  21 , 15 , 21]
    high = max(a)
    for i in range(high):
        buf = []
        for j in range(len(a)):
            if (high - i ) > a[j]:
                buf.append(  '  ' + t.Default )
                continue
            buf.append( t.ForeRed + t.BackGreen + '  ' + t.Default)
        buf.append( '  ' + t.Default )
        print ''.join(buf)
