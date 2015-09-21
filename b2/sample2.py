# coding=utf-8


from random import randint
import sys


class SampleDatas(object):

    def __init__(self, sample):
        self.data = []
        self.__idx = 0
        self.__sample = sample

    def reset(self, sample):
        del self.data[:]
        self.__idx = 0
        self.__sample = sample

    def __add__(self, line):
        self.add(line)
        return self

    def add(self, line):
        if len(self.data) < self.__sample:
            self.data.append(line)
        else:
            _sample = randint(0, self.__idx)
            if _sample < self.__sample:
                self.data[_sample] = line
        self.__idx += 1


class Reservoir(object):

    def __init__(self, samples_info, use_make_key=False, split_char=None):
        '''
        '''
        self.datas = {}
        self.make_keys = []
        self.use_make_key = use_make_key
        for sample_info in samples_info:
            self.datas[sample_info['key']] = SampleDatas(sample_info['sample'])
            # 将数据make_key  function 存放在self.make_keys
            if sample_info.has_key('make_key'):
                self.make_keys.append(
                    (sample_info['key'], sample_info['make_key']))
            else:
                self.make_keys.append((sample_info['key'], None))
        self.__split_char = split_char

    def add_line(self, line):
        items = self._split(line)
        if len(items) != 0:
            if self.use_make_key:
                key = self.make_key(items)
            else:
                key = self.get_key_from_items(items)
            if key != None:
                self.datas[key] += items

    def get_key_from_items(self, items):
        '''
        功能：
            从items中 ， 提取出所需要的字段组合
        参数:
            items
                list -> item
        return 如果存在key ， 返回key ； 否则返回 ， None
        '''
        for key, make_key in self.make_keys:
            if make_key == None:
                make_key = self.make_key
            try:
                key = make_key(items)
            except Exception, e:
                sys.stderr.write(
                    'items : [ %s ]  function : %s  \n ' % ('\t'.join(items), key))
                continue
            if key:
                return key
        return None

    def make_key(self, items):
        pass

    def _make_key(self, items, keys):
        '''
        已经废弃掉
        '''
        return ' '.join([items[key] for key in keys])

    def _split(self, line):
        '''
        function:
            split string to items
        params:
            line : input line
        return [] split items
        '''
        if line:
            if self.__split_char:
                return line.split(self.__split_char)
            else:
                return line.split()
        else:
            return []

    def output(self):
        '''
        function：
            输出蓄水池抽样结果
        params:
            self
        return
            ( key , line )
        '''
        for key, datas in self.datas.items():
            for line in datas.data:
                yield key, line


class ReservoirKey(object):

    def __init__(self, keys=(0, ), sample = 100000, split_char = None, *argv, **kw):
        '''
        function :
            init class 
        params:
            keys：
                将keys转换成组合key ， eg : 1 2 3  (1,3) key= "1 3"
            sample:
                蓄水池抽样算法 ， 随机选择出来数据量 
            split_char：
                将输入切分成item，分隔符
        return null
        '''
        self.__keys = keys
        self.__split_char = split_char
        self.__sample = sample
        self.datas = {}

    def add_line(self, line):
        items = self._split(line)
        if len(items) != 0:
            key = self._make_key(items, self.__keys)
            if not self.datas.has_key(key):
                self.datas[key] = SampleDatas(self.__sample)
            self.datas[key] += items

    def _make_key(self, items, keys):
        return ' '.join([items[key] for key in keys])

    def _split(self, line):
        '''
        function:
            split string to items
        params:
            line : input line
        return [] split items
        '''
        if line:
            if self.__split_char:
                return line.split(self.__split_char)
            else:
                return line.split()
        else:
            return []

    def output(self):
        '''
        function：
            输出蓄水池抽样结果
        params:
            self
        return 
            ( key , line ) 
        '''
        for key, datas in self.datas.items():
            for line in datas.data:
                yield key, line
