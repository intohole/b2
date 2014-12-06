#coding=utf-8


import os
import hashlib 

from ftplib import FTP 
from b2.object2 import Singleton


class Md5(Singleton):

    def __init__(self):
        self.md5 = hashlib.md5()


def getFileMd5(path):
    if path and os.path.isfile(path):
        with open(path) as f:
            return Md5.md5(''.join(f.readlines()))
    return ''



 

def ftpLogin(ip , port = 21 , debug = 2 , user_name  = '' , passwd = ''  ):
    ftp=FTP() 
    ftp.set_debuglevel(2) 
    ftp.connect(ip,str(port))
    ftp.login(user_name,passwd)
    return ftp 

 
def ftp_up(filename ,  ip, port = 21 , user_name = '' , passwd = '' , bufsize = 1024 ): 
    ftp=FTP() 
    ftp.set_debuglevel(2) 
    ftp.connect(ip,str(port))
    ftp.login(user_name,passwd)
    bufsize = 1024
    file_handler = open(filename,'rb')
    ftp.storbinary('STOR %s' % os.path.basename(filename),file_handler,bufsize)
    ftp.set_debuglevel(0) 
    file_handler.close() 
    ftp.quit() 
    return True


def ftp_down(filename ,  ip, port = 21 , user_name = '' , passwd = '' , bufsize = 1024): 
    ftp=FTP() 
    ftp.set_debuglevel(2) 
    ftp.connect(ip,'21') 
    ftp.login(user_name,passwd)
    bufsize = 1024 
    filename = "20120904.rar" 
    file_handler = open(filename,'wb').write #以写模式在本地打开文件 
    ftp.retrbinary('RETR %s' % os.path.basename(filename),file_handler,bufsize)#接收服务器上文件并写入本地文件 
    ftp.set_debuglevel(0) 
    file_handler.close() 
    ftp.quit() 
    