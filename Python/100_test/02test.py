#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-17 16:57:05
# @Author  : jhb (jhbnanyou@163.com)
# @Link    : 
# @Version : $Id$
"""
企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，
从键盘输入当月利润I，求应发放奖金总数？
"""
i = int(raw_input('result:'))
arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
for inx in range(0,6):
	if i > arr[inx]:
		r += (i-arr[inx]) * rat[inx]
		print "(" +str(i) + "-" + str(arr[inx]) + ")" + "*" + str(rat[inx]) + "=" +  str((i-arr[inx]) * rat[inx])
		i = arr[inx]             #保证后面能够整数的乘以百分比

print r




