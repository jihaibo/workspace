#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-28 14:33:35
# @Author  : jhb (jhbnanyou@163.com)
# @Link    : 
# @Version : $Id$

'''
两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。
已抽签决定比赛名单。有人向队员打听比赛的名单。
a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。

ord()函数主要用来返回对应字符的ascii码
chr()主要用来表示ascii码对应的字符他的输入时数字，可以用十进制，也可以用十六进制
'''
for i in range(ord('x'),ord('z')+1):
	for j in range(ord('x'),ord('z')+1):
		if i !=j:
			for k in range(ord('x'),ord('z')+1):
				if ( i != k ) and  (j != k):
					if (i != ord('x')) and (k != ord('x')) and (k != ord('z')):
						print 'order is a--%s\t b--%s\tc--%s' % (chr(i),chr(j),chr(k))