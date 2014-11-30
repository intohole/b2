===================



判断是否为root
----------

if [ $UID -eq 0 ] ; then  
fi   

prepend() {[ -d "$2" ]  && eval $1=\"$2':'\$$1\" && export $1;}  



数学运算
---------------------

:::shell
    
     let result = 1 + 1
     echo $result 
     #secound 
     result=$[$1 + $2]
     #third 
     result=$(( no1 + 50 ))
     result=`expr 3+4`
     retult=$(expr $no1 + 5)


字符串转换为大小写
-----------------------

:::shell
     
     echo "Hello world !" | tr 'A-Z' 'a-z' #大写转换为小写



sed
----------------
:::shell     
      
      sed 's/pattern/repleacepattern/' file 
      or:
      cat file | sed 's/pattern/repleacepattern/' 
      #上述为替换每一行第一处匹配内容替换 ， 想全部替换
      sed -i 's/pattern/repleacepattern/g' file



ls 文件通配符
-------------------



:::shell     
     
     ls abc@(.txt|.php)  #第一次出现后缀情况下  abc.txt.txt 会显示 abc.txt
     ls abc* #
     ls abc!(.txt|.php) #后面字符不出现匹配 
     ls abc?(.)txt #后面字符出现与否不关系匹配

特定变量说明
-----------------
:::shell     
     
     $RANDOM #一个随机变量
     $HOME #home主目录
     $
