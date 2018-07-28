# -*- coding:utf-8 -*-
author = 'haibo'
time = '2018-7-28'
"""
内置方法：__init__

创建一个新类实例时，参数被包括在圆括号内跟在类名后面，从而被传递给__init__方法
"""

class Person:
    def __init__(self,name):
        self.name = name
    def sayHi(self):
        print 'Hello,myname is',self.name

P = Person("haibo")
P.sayHi()




