# -*- coding: utf-8 -*-
"""
数据属性
"""

class Datattribue:
    pass

if __name__=="__main__":
    data = Datattribue()
    data.name = "我是没有被预先定义的数据属性"
    print data.name
