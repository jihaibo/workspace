# -*- coding: utf-8 -*-
"""
内置属性
"""

class BuiltAttribute:
    def __init__(self):
        self.built = 'wo shi fangfa"__init__"gou zao fangfa de shu xing'

class AttendBuilt(BuiltAttribute):
    def accept(self):
        self.acceptAttend = '我是方法 accept中的属性'

if __name__=="__main__":
    buildattribut = BuiltAttribute()
    attendbuilt = AttendBuilt()
    print '我是继承BuiltAttribute的属性',attendbuilt.built
    print '我是使用__bases__内置属性的基类组成的元祖',AttendBuilt.__bases__
    print '我是使用__dict__内置属性输出的属性组成字典',AttendBuilt.__dict__
    print '我是使用__module__内置属性输出类所在的模块名',AttendBuilt.__module__
    print '我是使用__doc__内置属性输出的doc文档',AttendBuilt.__doc__
    print '我是使用__name__内置属性输出的类名',AttendBuilt.__name__
