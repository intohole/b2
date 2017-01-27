#!/bin/sh




echo > function.md
cd `dirname $0`
CWD=`pwd`
for function_file in `ls ${CWD}/b2/*.py`;do
    echo "+ `basename ${function_file}`" >>function.md
    cat ${function_file} | grep -E "(^class|def )" | grep -v "__" | sed  's/class /    + /' | sed 's/def /    + /' | sed 's/:$//' >> function.md 
done
