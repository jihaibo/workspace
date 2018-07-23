# -*- coding:utf-8 -*-
author = 'haibo'
time = '2018-7-23'
"""
迭代工具
"""

# 1.0并行迭代
names = ['xiaomi','jingdong','tianmao','yamaxun']
ages = [23,22,21,25,26]
for i in range(len(names)):
    print names[i],'的年龄是',ages[i]
# zip迭代是两个列表压缩在一起
for name,age in zip(names,ages):
    print name, '的年龄是：',age


# 2.0编号迭代
hypos = ['活着','彷徨之刃','解忧杂货铺','三体']
for index,hypo in enumerate(hypos):      # enumerate函数进行编号迭代，主要是提供索引的地方迭代索引值对
    if "三体" in hypo:
        hypos[index] = '平凡的世界'       # 用平凡的世界替换三体
        print index,hypo
        for i in hypos:
            print i


# 3.0关键字搜索
book_name = raw_input('请输入您要查询书的名字：')
books = ['时间简史','麦田守望者','放风筝的人','异乡人','白夜行','史记','横向时间']
for index,book in enumerate(books):
    if book_name in book:
        print book






















