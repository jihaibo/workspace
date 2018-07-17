# -*- coding:utf-8 -*-

try:
    year = int(raw_input("plear input a year:"))
    if year%4 ==0 and year%100 !=0:
        print "%d is a leap year." % year
    elif year % 4 ==0 and year % 100 ==0:
        print "%d is a leap year." % year
    else:
        print "%d is not a leap year." % year

except ValueError,e:
    print "you must input a digits. "
