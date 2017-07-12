#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-12 15:15:52
# @Author  : jhb (jhbnanyou@163.com)
# @Link    : 
# @Version : $Id$

'''
按逗号分隔列表。
'''
L = [1,2,3,4,5]

sl = ','.join(str(n) for n in L)
print sl