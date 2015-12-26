#coding=utf-8




import subprocess
from thread2 import ThreadPool





def run_command_order(commands):
    sorted(commands.items() , lambda x:x[0])


    
pie1 = subprocess.Popen(["ls" , "-lht"]  , stdout = subprocess.PIPE)
pie2 = subprocess.Popen(["grep" , "py"] ,stdin = pie1.stdout , stdout = subprocess.PIPE )
out = pie2.communicate()
