python
=================



+  \*arg , \**kw区别
:::python    
        

        def p(*arg , **kw):
        '''
         词典转换为 **kw  必须将词典变量 前面添加 **kw ,
         否则作为 arg参数
        '''
           if kw.has_key('a'):
               print kw['a']
           if len(arg) > 0:
               print arg[0]
        if __name__ == '__main__':
            p(1 ,2 ,3 , a = 5 , b = 6)
            # 5
            # 1
            d = {'a' : 6  , 'c' : 7}
            p(**d)
        # 6

