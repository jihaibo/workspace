# -*- coding: utf-8 -*-
"""
私有属性
"""

class Fly:
    price = 123   # 公有的类属性
    def __init__(self):
        self.__direction = '开往北京的火车'       # 私有的实例属性
        zIng = '候车厅，人很多'                   # 局部变量

if __name__ == '__main__':
    print Fly.price
    fly = Fly()
    print fly._Fly__direction      # 实例化对象名._类名__私有属性（用于开发阶段的测试和调试，一般做法是用get方法）