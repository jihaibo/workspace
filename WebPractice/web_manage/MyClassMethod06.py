# -*- coding:utf-8 -*-
author = 'haibo'
time = '2018-7-28'
"""
内置方法：__getitem__

重定向到字典，返回的是字段的值
"""

class MyGetitem:
    def __getitem__(self, key):
        if key == 'haibo':
            return '90'
        elif key == 'dingli':
            return '85'
        elif key == 'jianguang':
            return '99'
        else:
            return 'goodbye'

if __name__=="__main__":
    mygetitem = MyGetitem()
    print mygetitem['haibo']
    print mygetitem['dingli']
    print mygetitem['jianguang']
    print mygetitem['xianwei']
    print mygetitem[' ']

