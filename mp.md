shell 编写mapreduce
====================


:::shell  

    awk -v OFS="\t" 'BEGIN{
         #全局变量初始化
    }{
        if (NR == 1) #第一行数据作为初始化这个reduce全局变量
        {
        }
        else ... #开始处理其它行号
    }END{
        #这个程序执行到最后时 ， 会调用这个方法 
        #一般为打印数据 
        #print
    }'

awk 关于使用数组，词典
-----------------
+ 数组无初始化 eg. example[1]=1 #example 任意命名 ， 键可以任意设置 ， 数组值也可以 
+ 数组循环 ， for(i in example){ example[i] ; #里面的元素}
+ 清空数组 , for(i in example) { delete example[i] ; #循环删除数组元素}
+ 判断数组是否含有这个元素 , if( example[3] ) {} else {}

字符串相加
-----------------
+ 变量名称3=变量名称1\"\"变量名称2




