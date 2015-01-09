#coding=utf-8



def deco(func):
    def _deco():
        print("before myfunc() called.")
        func()
        print("after myfunc() called.")
        # 不需要返回func，实际上应返回原函数的返回值
    return _deco



@deco
def fun():
    print 'fun called'
    return 'ok'



if __name__ == '__main__':
    fun()