# -*- coding: utf-8 -*-
"""
公有属性
"""

class Fly:
    price = 123  # 公有的类属性
    def __init__(self):
        self.direction = '开往北京的火车'   # 公有的实例属性
        zIng = '候车厅中，人很多'           # 局部变量

if __name__ =="__main__":
    print Fly.price
    fly = Fly()                    # 实例化Fly类
    Fly.price = fly.price+10
    print '候车厅怎么样'
    print '火车票的价格上涨后的结果是：'+ str(fly.price)
    myfly = Fly()
    print '我的理想价格是：' + str(myfly.price-20)