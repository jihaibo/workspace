#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-06 18:15:54
# @Author  : jhb (jhbnanyou@163.com)
# @Link    : 
# @Version : $Id$

'''
求1+2!+3!+...+20!的和。
'''
n = 0
s = 0
t = 1
for n in range(1,21):
    t *= n
    s += t
print '1! + 2! + 3! + ... + 20! = %d' % s