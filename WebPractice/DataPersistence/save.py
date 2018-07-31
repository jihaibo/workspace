# -*- coding:utf-8 -*-
author = 'haibo'
time = '2018-7-28'
"""
打开后永久保存数据

制作一个永久保存的磁盘
"""
import shelve
class Person:
    def __init__(self,title,content):
        self.title = title
        self.content = content
    def say(self):
        print '您输入的标题是：%s \t 您输入的内容是：%s' %(self.title,self.content)
temppath = 'MyGood'
def init():
    m = {}
    f = shelve.open(temppath,'c')
    f["init"] = "--------欢迎使用您的万能记事本----------"
    f.close()
init()
print "请选择您的下一步：\n(add) 添加永久保存的内容\t(del)删除永久保存的内容\t(quit)关闭记事本\n(show) 展示永久保存的内容"
while True:
    check = raw_input('选择您下一步的操作：')
    if check =='quit':
        break
    if check =='add':
        print '------欢迎使用添加主题功能------'
        titleSave = raw_input('请输入您想永久保存的标题：')
        contentSave = raw_input('请输入您要永久保存的内容：')
        f = shelve.open(temppath,'w')
        f["title"] = titleSave
        f['content'] = contentSave
        print '我添加的标题是：'+f["title"],'我添加的内容时：'+f["content"]
    if check == 'del':
        print '------欢迎使用删除主题功能-------'
        titleDel = raw_input('请输入您想删除标题的键值：')
        f = shelve.open(temppath,'w')
        if f.has_key(titleDel):
            del f[titleDel]
        print '删除成功！'
    if check =='say':
        titleSave = raw_input('请输入您想永久保存的标题：')
        contentSave = raw_input('请输入您要永久保存的内容：')
        Person(raw_input(titleSave,contentSave))
        Person(raw_input(titleSave,contentSave)).say()
        print "仔细看清楚，没有保存"
    if check =='show':
        f = shelve.open(temppath,'w')
        print '---------下面是您要永久保存的内容--------------'
        for key,value in f.iteritems():
            print key,value
        print '----------over-------------'
        f.close()
