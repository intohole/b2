b2　
======================
* num2.py 数字处理工具
* str2.py 字符串处理工具
* time2.py 时间处理工具
* ini2.py 配置文件处理工具
* exceptions.py 判断异常处理工具
* buffer2.py 实现stringbuilder工具
* md2.py markdown　，　将语法转换为python函数



```python  
     
    from b2 import md2
    if __name__ == '__main__':
        md2 = MD2()
        print md2.get_title('xxx00')
        print md2.child_title('child')
        print md2.get_link_str('test' , 'www.baidu.com')
```



```python   

     from b2.str2 import *
     print get_sign_repeat('#' , 6)
     print dict_to_string(data)
     print reverse('123')    
```

```python   
    
     from b2.time2 import *
     if __name__ == '__main__':
        print get_time_ms()
        print get_time_string()
```


```python   

     from b2 import buffer2
     if __name__ == '__main__':
        buf = Buffer2()
        buf += '03355112'
        print buf # 03355112
        print buf.find_first('1') # 5
        print buf.reverse() #21155330
        print buf.to_str('\n') #
        print len(buf) # 8
```

```python   
   
     from b2 import num2
     if __name__ == '__main__':
         print get_random_seq1(6) #067693
```

```python
     from b2 import trie2 
     if __name__ == "__main__":
        t = Trie()
        t.add("我爱天安门", 1)
        print t.find("我爱天安")
```

计划
---------
-  实现一些工具　，　方便工作使用　　
-  实现网络　，　将buffer2工具具体细化功能　，　方便自己　，　也方便使用它的人
