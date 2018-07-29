# -*- coding:utf-8 -*-
author = 'haibo'
time = '2018-7-28'
"""
方法的动态特性

class_name.method_name = exist_name
将exist_name 追加到类class_name 中，并取名叫：method_name
"""

def among():
    print '衣带渐宽终不悔，为伊消得人憔悴。'

def endinig():
    print '众里寻他千百度，蓦然回首，那人却在，灯火阑珊处。'

class Person:
    def began(self):
        print '昨夜西风凋碧树。独上高楼，望尽天涯路。'

if __name__ == "__main__":
    print '人生的三个境界，第一个是：'
    person = Person()
    person.began()
    print '第二个境界是：'
    person.began = among()
    person.began
    print '第三个境界是：'
    person.newmethod = endinig()
    person.newmethod