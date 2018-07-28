# -*- coding: utf-8 -*-
"""
类方法和类实例方法
"""

class MySl(object):
    def myfoo(self,myself):
    # 类实例方法
        print "执行类实例方法 foo(%s,%s)"%(self,myself )
    @classmethod
    def class_foo(cls,mycls):
    # 类方法
        print '执行方法 class_foo(%s,%s)'%(cls,mycls)

if __name__=="__main__":
    mysl = MySl()
    mysl.myfoo('jhb')
    mysl.class_foo('jhb')
    MySl.class_foo('jhb')       #允许类直接调用自己的类方法
    # MySl.myfoo("hgi")          不允许类直接调用类实例方法

"""
对类实例方法myfoo来说，只能使用类实例调用，否则会出现异常
"""
