#coding=utf-8


from collections import defaultdict

class Test(object):



    def __init__(self):
        self.a = defaultdict(float)
        self.a[1] += 1.0




from copy import copy



t = Test()

t1 = copy(t)
t.a[1] += 1.0

print t1.a
print t.a