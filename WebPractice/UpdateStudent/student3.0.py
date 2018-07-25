# -*- coding:utf-8 -*-
'''
管理系统
将学员信息存入文件中
'''
def is_in_range():
    index = int(raw_input('请选择要（修改）删除的学生序号：'))
    while index not in range(0,len(student_list)):
        index = int(raw_input('您输入的序号不在范围内，请重新输入：'))
    return index

def add_stu():
    name = raw_input('请输入姓名：')
    age = raw_input('请输入年龄：')
    sex = raw_input('请输入性别：')
    person_list = [name,age,sex]
    student_list.append(person_list)
    print ('添加成功！')

def alter_stu():
    index = is_in_range()
    person = student_list[index]
    name = person[0]
    age = person[1]
    sex = person[2]
    student_list[index][0] = raw_input('请输入修改后的姓名（%s）:' % name)
    student_list[index][1] = raw_input('请输入修改后的年龄（%s）:' % age)
    student_list[index][2] = raw_input('请输入修改后的性别（%s）:' % sex)
    print ('修改成功！')

def see_stu():
    for x in range(0,len(student_list)):
        person = student_list[x]
        name = person[0]
        age = person[1]
        sex = person[2]
        print ('序号：%s 姓名：%s 年龄：%s 性别：%s ' % (x,name,age,sex))

def del_stu():
    print('1.删除所有学生')
    print('2.删除选择的学生')
    num = int(raw_input('请选择您的删除方式：'))
    if num ==1:
        del student_list[:]
    else:
        index = is_in_range()
        del student_list[index]

#声明一个保存数据的函数
def save_data():
    #1.打开文件
    file_handle = open('student_v3.txt',mode='w')
    #2.循环遍历大列表
    for student in student_list:
        #把列表中的数据用空格分开拼成一个字符串
        s = ' '.join(student)
        #写入
        file_handle.write(s)
        file_handle.write('\n')
    #3.关闭文件
    file_handle.close()

import os

def read_data():
    #判断文件是否存在
    rs = os.path.exists('student_v3.txt')
    if rs == True:
        #打开文件
        file_handle = open('student_v3.txt',mode='r')
        #取出信息
        contents = file_handle.readlines()
        for content in contents:
            #去除/n
            content = content.strip('\n')
            #使用空格分割字符串，得到列表
            list_1 = content.split(' ')
            student_list.append(list_1)
        #关闭文件
        file_handle.close()


#声明一个列表，存放学生信息
student_list = []
read_data()
while True:
    print ('1.添加学生')
    print ('2.修改学生')
    print ('3.查询学生')
    print ('4.删除学生')
    print ('0.退出程序')
    sel_num  = int(raw_input('请输入您要进行的操作：'))
    while sel_num not in range(0,5):
        sel_num = int(raw_input('您的选择无效，请重新选择：'))
    if sel_num ==1:
        add_stu()
        save_data()
    elif sel_num ==2:
        see_stu()

        alter_stu()
        save_data()
    elif sel_num ==3:
        see_stu()
    elif sel_num ==4:
        see_stu()

        del_stu()
        save_data()
    else:
        break
































