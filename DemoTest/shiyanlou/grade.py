# -*- coding:utf-8 -*-

'''
    author = haibo
'''

def getGrade(num):
    if 90 < num <=100:
        print "A"
    elif 80 < num <= 90:
        print "B"
    elif 70 < num <= 80:
        print "C"
    elif 60 <= num <= 70:
        print "D"
    else:
        print "F"

try:
    num = int(raw_input("Input a num:"))
    getGrade(num)
except ValueError, e:
    print "You must input digits "