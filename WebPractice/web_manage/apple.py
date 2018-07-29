# -*- coding:utf-8 -*-
author = 'haibo'
time = '2018-7-28'
"""
模拟水果成熟的过程
"""

class Fruit:
    def __init__(self,*args):
        for arg in args:
            arg(self)
    def config(self,*args):
        for arg in args:
            arg(self)

#是否成熟
def has_harvest(self):
    self.harvest = '是'
def has_not_harvest(self):
    self.harvest = '否'

#水果的颜色
def setColor(color):
    def method(self):
        self.color = color
    return method

    #水果是否能吃
def can_eat(self):
    self.eat = "可以"
def can_notEat(self):
    self.eat = "不可以"

if __name__=="__main__":
    apple = Fruit(has_not_harvest,setColor('green'))
    print '苹果是否成熟：%s;目前苹果的颜色是：%s' % (apple.harvest,apple.color)
    apple.config(has_harvest,setColor('red'),can_notEat)
    print '苹果是否成熟：%s;目前苹果的颜色是：%s;可以吃吗：%s' % (apple.harvest,apple.color,apple.eat)
    apple.config(has_harvest,setColor('red'),can_eat)
    print '苹果是否成熟：%s;目前苹果的颜色是：%s;可以吃吗：%s' % (apple.harvest,apple.color,apple.eat)

