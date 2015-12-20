b2　
======================
* num2.py 数字处理工具
* str2.py 字符串处理工具
* time2.py 时间处理工具
* ini2.py 配置文件处理工具
* exceptions.py 判断异常处理工具
* buffer2.py 实现stringbuilder工具
* md2.py markdown　，　将语法转换为python函数

## 2014年写的代码 ， 一直没有更新README.md 所以你看到的这个内容很旧 ， 后续有时间 我更新功能api##  

```python  
     
    mkdir_p('d:/work_space/p2')
    reload_utf8()
    print walk_folder('D:\\workspace\\b2', lambda x:  x.endswith('py'))
    print create_folder_map('d:\\workspace\\b2', lambda x:  x.endswith('py') , limit_level = 1)
    a = lambda x : x.endswith('bb')
    print a('aa')
    print a('bb')
    print 'D:\\workspace\\b2\\.git\\COMMIT_EDITMSG'.endswith('py')
    for line  in Files(dirpath='D:\\workspace\\b2', file_filter=lambda x:  x.endswith('py')):
        print line 
```



```python   
from b2.stop2 import StopWords
    s = StopWords(path='d:\\a.txt')
    print s.endswith('a')
    print s.startswith('a')
    print s.is_stop('aaaa')
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
