#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-23 09:56:17
# @Author  : jhb (jhbnanyou@163.com)
# @Link    : 
# @Version : $Id$

"""
暂停一秒输出。
"""
import time

myD = {1:'a',2:'b'}
for key,value in dict.items(myD):        #dict.items 返回可遍历的（键，值）元组数组
	print key,value
	time.sleep(2)

