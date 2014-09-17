#coding

import sys



def reload_utf8():
    reload(sys)
    sys.getdefaultencoding()
    