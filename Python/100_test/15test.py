#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-23 16:01:53
# @Author  : jhb (jhbnanyou@163.com)
# @Link    : 
# @Version : $Id$

"""
题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，
60-89分之间的用B表示，60分以下的用C表示。
"""
score = int(raw_input("please enter student's score:\n"))

if score >=90:
	grate = "A"
elif score>=60:
	grate = "B"
else:
	grate = "C"
print '%d is %s' % (score,grate)