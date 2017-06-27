#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-23 10:10:07
# @Author  : jhb (jhbnanyou@163.com)
# @Link    : 
# @Version : $Id$
"""
题目：暂停五秒输出，并格式化当前时间。
"""
import time

print time.strftime('%Y-%m-%d  %H:%M:%S',time.localtime(time.time()))

#暂停一秒

time.sleep(5)

print time.strftime('%Y-%m-%d  %H:%M:%S',time.localtime(time.time()))
