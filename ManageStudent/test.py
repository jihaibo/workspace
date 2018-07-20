# -*- coding:utf-8 -*-

"""
九九乘法表
"""
for i in range(1,10):
    for j in range(1,i+1):
        print ('%s*%s=%s' %(j,i,i*j)),  #加’，‘取消自动换行
    i+=1
    print ('\n')   #换行

