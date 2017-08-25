#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-28 15:48:12
# @Author  : jhb (jhbnanyou@163.com)
# @Link    : 
# @Version : $Id$

'''
题目：画图，学用circle画圆形。　
'''
if __name__ == '__main__':
	from Tkinter import *

	canvas = Canvas(width=800,height=800,bg='blue')
	canvas.pack(expand = YES,fill= BOTH)
	k = 1
	j = 1
	for i in range(0,20):
		canvas.create_oval(400 - k,400-k,400+k,400+k,width=1)
		k +=j 
		j += 1

	mainloop()