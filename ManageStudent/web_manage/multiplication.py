# -*- coding:utf-8 -*-
author = 'haibo'
time = '2018-7-23'
"""
打印久久乘法表
"""
for i in range(1,10):
    for j in range(1,i+1):
        print ('%s*%s=%s' %(j,i,i*j)), # ","表示取消换行
    i += 1
    print ('\n')  # 换行