tr  # coding=utf-8

from exceptions2 import *
from str2 import *


class MD2(object):

    """help you write markdown by python"""

    def get_title(self, title):
        '''
        得到markdown文档的标题格式
        eg. 
        title
        =================
        '''
        judge_str(title)
        buf = []
        buf.append(title)
        buf.append(get_sign_repeat("=", 6))
        return join_str_list(buf, ' \n')

    def child_title(self, title):
        '''
        得到md文档中次要的标题 ， 主要是格式问题
        eg.
        title
        ---------------------
        '''
        judge_str(title)
        buf = []
        buf.append(title)
        buf.append(get_sign_repeat("-", 6))
        return join_str_list(buf, ' \n')

    def get_p(self, content):
        '''
        得到pargraph ， 
        eg.
        > content
        '''
        judge_str(content)
        return '>  %s' % content

    def get_link_str(self, msg, link):
        '''
        生成md文件link
        msg 是link说明文字
        link 是link 地址
        '''
        judge_str(msg)
        judge_str(link, l=4)
        return '[%s](%s)' % (msg, link)

    def get_pic_str(self, alt, pic_link):
        '''
        生成md文件pic连接文件
        alt pic 提示文字
        pic_link 是图片连接地址
        '''
        judge_str(alt)
        judge_str(link, l=4)
        return '![%s](%s)' % (alt, link)

    def get_h_n(self, content, n):
        '''
        生成md文档的H1~6字体
        '''
        judge_str(content)
        return '%s%s' % (get_sign_repeat('#', n), content)


if __name__ == '__main__':
    md2 = MD2()
    print md2.get_title('xxx00')
    print md2.child_title('child')
    print md2.get_link_str('test', 'www.baidu.com')
