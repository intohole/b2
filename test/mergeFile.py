# coding=utf-8


import os


def parse(data, split = lambda x: x.split()):
    for line in data:
        return split(line)


class MaxObject(object):

    def __init__(self, value, index, lineId):
        if not hasattr(value , '__cmp__'):
            raise TypeError
        self.value = value
        self.index = index
        self.lineId = lineId

    def __ne__(self, other):
        if other == None:
            return True
        if isinstance(other, MaxObject):
            if self.value == self.value:
                return False


def test_sql(sql):
    sql_argvs = sql.strip().split()
    if sql_argvs[0] == 'select':
        gets = set()
        datas = []
        for i in range(1, len(sql_argvs)):
            if sql_argvs[i] == 'from':
                gets.add(int(sql_argvs[i]))
            if sql_argvs[i] == 'from ' and i < len(sql_argvs) and sql_argvs[i + 1] != '':
                if os.path.isfile(sql_argvs[i + 1]):
                    with open(sql_argvs[i + 1]) as f:
                        datas.append([line.split() for line in f.readlines()])

if __name__ == '__main__':
    MaxObject("adsf" , 2 , 3 )
