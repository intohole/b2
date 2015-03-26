# coding=utf-8


def get_datas_gather(*argv):
    gathers = []
    sorted_list = sort_list_by_len(*argv)
    for i in range(sorted_list[0][1]):
        _tmp = []
        for ll in sorted_list:
            if ll[1] > i:
                try:
                    _tmp.index(ll[0][i])
                except Exception, e:
                    _tmp.append(ll[0][i])
        gathers.extend(_tmp)
    return gathers


def sort_list_by_len(*argv):
    return sorted([(ll, len(ll)) for ll in argv if ll and hasattr(ll, '__len__')], key=lambda x: x[1], reverse=True)


if __name__ == '__main__':
    print get_datas_gather([1, 3,4,5] , [1,2,4])
