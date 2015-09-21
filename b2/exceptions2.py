# coding=utf-8


def judge_str(content, l=0, types=(str, unicode)):
    '''
    判断字符串
    1. 如果字符串为None ， 抛出异常 ValueError
    2. 如果字符串类型不为(str , unicode) , 抛出TypeError
    3. 如果字符串长度小于 l , 抛出异常ValueError
    '''
    judge_null(content)
    judge_type(content, 'content must be str or unicode ',types)
    judge_len(content, l)


def judge_num(num, min_num = None, max_num = None):
    '''
    判断数字
    '''
    judge_null(num)
    judge_type(num, 'value type isn\'t  int or long', (int, long))


def judge_bigger(self, value, min_num):
    if value <= min_num:
        raise ValueError, 'value must be bigger than %s' % min_num


def judge_smaller(self, value, max_num):
    if max_num and value > max_num:
        raise ValueError, 'value must be smaller than %s' % max_num


def judge_null(value):
    if value is None:
        raise ValueError, 'value is null!'


def judge_type(value, msg, types):
    if types:
        if not isinstance(value, types):
            raise TypeError, msg % type(value)

def judge_list(value):
    judge_type(value , 'type isn\'t list or tuple' , (list , tuple))

def judge_len(value, l):
    '''
    判断value长度 ， 是否小于l 
    如果小于长度 l , 抛出异常 ValueError
    '''
    if value:
        if len(value) < l:
            raise ValueError, 'value length must be bigger than %s' % l


def judge_ge_value(value , ge_value = 0):
    '''
    判断value是否小于
    '''
    if type(value) == type(ge_value) and value < ge_value:
        raise ValueError , 'value must be greate or eaqual %s' % ge_value


def judge_callable(value):
    judge_null(value)
    if not callable(value):
        raise ValueError , 'value must be callable'


def judge_le_value(value , le_value):
    if value > le_value:
        raise ValueError , 'value must be less or eaqual %s' % le_value

def judge_type_eq(value1, eq_value):
    pass



