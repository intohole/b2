#coding=utf-8




def dict_to_string(data):
    if data and len(data) >  0 and isinstance(data , dict):
        return ' '.join(["%s:%s" % (__key , __val) for __key , __val in data.items()])
    return ''


if __name__ == '__main__':
    data = {}
    data[0] = 1
    data[2] = 2

    print dict_to_string(data)