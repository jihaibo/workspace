# -*- coding: utf-8 -*-
"""
静态方法
"""

class Methods:
    @staticmethod
    def mymethod ():
        print '我是被定义的静态方法'
    def __mymethod ():
        print '我是私有方法'
    def getMymethod ():
        print '测试转换为静态的方法'

    conversion = staticmethod(getMymethod)
    conPrivate = staticmethod(__mymethod)

if __name__ =="__main__":
    methods = Methods()         # 实例化对象
    methods.mymethod()          # 实例对象访问普通方法
    Methods.mymethod()          # 类访问普通方法
    Methods.conversion()        # 类访问转换为静态后的普通方法
    methods.conversion()        # 类实体对象访问转换为静态后的普通方法
    Methods.conPrivate()        # 类访问转换为静态的私有方法
    methods.conPrivate()        # 类实体对象访问转换为静态的私有方法
