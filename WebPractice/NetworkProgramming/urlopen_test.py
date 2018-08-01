# -*- coding:utf-8 -*-
author = 'haibo'
time = '2018-8-1'
"""
网络编程,打开远程文件
read 读取文件内容
"""

import urllib2
response = urllib2.urlopen('http://www.itzcn.com')
#方法打开远程文件
html = response.read()
print html