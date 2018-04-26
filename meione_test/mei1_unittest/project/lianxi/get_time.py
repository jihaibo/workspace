# -*- coding:utf-8 -*-

import time

class GetTime(object):

    def get_system_time(self):
        print (time.time())  #获取的是从1970年到现在的时间间隔，单位是秒
        print (time.localtime())  #获取的是当前时间
        new_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()) #格式化时间，按照2018-04-26 14:47:30的格式打印出来
        new_time01 = time.strftime('%Y%m%d %H:%M:%S',time.localtime())
        print (new_time)
        print (new_time01)

gettime = GetTime()
gettime.get_system_time()