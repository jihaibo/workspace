# -*- coding:utf-8 -*-
author = 'haibo'
time = '2018-7-23'
"""
小明今年5岁，父亲26岁，当小明7岁的时候，请输入父亲多大？
"""

def countAge(sonAge,setAge,fatherAge):
    # 计算时间差
    diffAge = int(setAge-sonAge)
    # 计算父亲实际年纪
    yfatherAge = fatherAge + diffAge
    # 返回父亲实际的年纪
    print ('将来父亲的年龄为：%s' % yfatherAge)



son =int(raw_input('请输入儿子当前年纪：'))
fson= int(raw_input('请输入将来儿子年纪：'))
father = int(raw_input('请输入父亲当前的年纪：'))
countAge(son,fson,father)