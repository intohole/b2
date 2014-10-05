#coding

import sys
import os


def reload_utf8():
    reload(sys)
    sys.getdefaultencoding()


def split_path(p):
    if p and len(p) > 0 and isinstance( p ,  str):
        return os.path.split(p)




if __name__ == '__main__':
    print split_path("d:\\windows\\a.txt")
    