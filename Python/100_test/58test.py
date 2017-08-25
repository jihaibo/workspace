#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-28 16:15:56
# @Author  : jhb (jhbnanyou@163.com)
# @Link    : 
# @Version : $Id$

'''
画图，学用rectangle画方形。
'''
if __name__ == '__main__':
	from Tkinter import *
	root = Tk()
	root.title('Canvas')
	canvas = Canvas(root,width=400,height = 400,bg='yellow')
	x0 = 263
	y0 = 263
	x1 = 275
	y1 = 275
	for i in range(19):
		canvas.create_rectangle(x0,y0,x1,y1)
		x0 -= 5
		y0 -= 5
		x1 += 5
		y1 += 5
	canvas.pack()
	root.mainloop()
