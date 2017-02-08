#!/bin/sh




echo > function.md
cd `dirname $0`
CWD=`pwd`
for function_file in `ls ${CWD}/b2/*.py`;do
    echo "+ `basename ${function_file}`" >>function.md
    cat ${function_file} | grep -En "(^class|def )" | grep -v "__" | sed  's/class /    + /' | sed 's/def /    + /' | sed 's/:$//' | awk -F ":" '{
    line_number = $1;
    function_name = $2;
    print function_name"](https://github.com/intohole/b2/blob/master/b2/cache2.py#L"line_number")" 
}' | sed 's/+ /+ [/'>> function.md 
done
