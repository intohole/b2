#!/bin/sh




echo > function.md
cd `dirname $0`
CWD=`pwd`
for function_file in `ls ${CWD}/b2/*.py`;do
    echo "+ `basename ${function_file}`" >>function.md
    cat ${function_file} | grep -En "(^class|def )" | grep -v "__" | sed  's/class /    + /' | sed 's/def /    + /' | sed 's/:$//' | sed 's/\]/\\]/g' | sed 's/\[/\\[/g' | awk -F ":" '{
    line_number = $1;
    function_name  = ""
    for(i = 2 ;i <=NF ;i++){
        if(i != 2){
            function_name=function_name":"$i
        }else{
            function_name =$i 
        }
    }
    print function_name"](https://github.com/intohole/b2/blob/master/b2/'`basename ${function_file}`'#L"line_number")" 
}' | sed 's/+ /+ [/'>> function.md 
done
