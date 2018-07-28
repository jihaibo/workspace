# -*- coding:utf-8 -*-
author = 'haibo'
time = '2018-7-28'
"""
内置方法：__del__

主要作用是释放被占用的资源，在Python中是析构函数
"""
class Room:
    count = 0
    def __init__(self,name):
        self.name = name
        print "初始化，传入的名称是%s" % self.name
        Room.count+=1
    def __del__(self):
        print '%s 说byebye' % self.name
        Room.count-=1
        if Room.count ==0:
            print '我是这个房间里的最后一个了'
        else:
            print '这个房间里有 %d 个人还未离开' % Room.count
    def sayHi(self):
        print "大家好，我的名字是 %s " % self.name
    def howMany(self):
        if Room.count == 1:
            print '这个房间里就只剩下我一个人了'
        else:
            print '这个房间里还有 %d 个人' % Room.count

if __name__=="__main__":
    room = Room('haibo')
    room.sayHi()
    room.howMany()
    room1 = Room('dingding')
    room1.sayHi()
    room1.howMany()
    room.__del__()