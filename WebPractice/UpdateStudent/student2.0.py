# -*- coding:utf-8 -*-
'''
学生管理系统
函数版--用列表存放学员信息
'''

#添加学员函数
def add_student():
    #输入学员姓名、年龄、电话
    name = raw_input('请输入学生姓名：')
    age = raw_input('请输入学生年龄：')
    phone = raw_input('请输入学生电话：')
    #把name、age、phone放在小列表中
    student = [name,age,phone]
    #把小列表添加到所有学生的大列表中
    student_list.append(student)
    print ('添加学生成功！')

#查询学生函数
def query_student():
    #1、查询所有学生
    #2、输入学生姓名 查询学生
    print ('1.查询所有学生')
    print ('2.查询指定学生')
    num = int(raw_input('请输入查询学生条件：'))
    while num not in range(1,3):
        num = int(raw_input('选择查询学生条件无效，请重新输入：'))
    if num ==1:
        print ('***************学生信息列表******************')
        #遍历大列表
        for x in range(0,len(student_list)):
            #根据X的值从大列表中取出小列表
            student = student_list[x]
            #从小列表中取出姓名、年龄、电话
            name = student[0]
            age = student[1]
            phone = student[2]
            print ('序号：%s 姓名：%s 年龄：%s 电话：%s'%(x,name,age,phone))

    else:
        name = raw_input('请输入您要查询学生的姓名：')
        while 1:
            a = False
            for student in student_list:
                if student[0] == name:
                    index = student_list.index(student,0,8)
                    print ('序号：%s 姓名：%s 年龄：%s 电话：%s'%(index,student_list[index][0],student_list[index][1],student_list[index][2]))
                    a = True
            if a ==False:
                name = raw_input('该学生没有找到，请重新输入：')
            else:
                break

#修改学生的函数
def update_student():
    #判断是否有学生信息，如果没有，直接结束函数的执行
    if len(student_list)==0:
        print ('没有学生信息，无法进行修改操作！')
        #强制结束函数的执行 return 下面的代码都不会再执行
        return

    #1.查询学生信息
    query_student()
    #2.选择要修改的学生序号
    num = int(raw_input('请选择要修改的学生序号：'))
    #3.判断选择的学生序号是否在在范围之内
    while num not in range(0,len(student_list)):
        #不在范围，重新选择
        num = int(raw_input('没有该序号，重新选择：'))
    #4.根据选择的序号取出对应的小列表
    student = student_list[num]
    new_name = raw_input('请输入修改后的姓名(%s):'%student[0])
    new_age  = raw_input('请输入修改后的年龄(%s):'%student[1])
    new_phone = raw_input('请输入修改后的电话(%s):'%student[2])
    #5.修改小列表中的数据
    student[0] = new_name
    student[1] = new_age
    student[2] = new_phone
    print ('修改成功！')

#删除学生函数
#1.根据学生序号删除  2.删除所有学生  3.根据学生的姓名删除（有同名的）
def delete_student():
    if len(student_list)==0:
        print ('没有学生信息，无法执行删除功能！')
        return
    print('1.根据学生序号进行删除')
    print('2.删除所有学生')
    print('3.根据学生姓名进行删除')
    #获取输入的内容并转换为为整数类型
    num = int(raw_input('请输入您删除的类型：'))
    #判断选择的类型是否在范围之内
    while num not in range(1,4):
        num = int(raw_input('没有该类型，请重新选择：'))
    #判断选择的选项
    if num == 1:
        #1.查询学生信息
        query_student()
        #2.选择删除的序号
        num = int(raw_input('请输入您要删除的学生序号：'))
        #判断选择的序号是否在范围之内
        while num not in range(0,len(student_list)):
            num = int(raw_input('序号不在范围之内，请重新选择：'))
        is_del = raw_input('您确认要删除(%s)学生的信息吗？(y/n):'%student_list[num][0])
        if is_del =='y':
            #删除列表中的所有数据
            student_name = student_list[num][0]
            del student_list[num]
            print ('%s学生信息删除成功！'%student_name)
        else:
            print ('删除数据操作已取消！')

    elif num ==2:
        #确认删除
        is_del = raw_input('您确定要删除所有学生信息吗？y(确定)/n(取消)：')
        if is_del=='y':
            #删除列表中的所有数据
            del student_list[:]
            print ('删除所有学生成功！')
            return
        else:
            print ('删除数据操作已取消！')
    else:
        name = raw_input('请输入您要删除的学生姓名：')
        while 1:
            #定义列表放存不等于name的小列表
            list = []
            #遍历列表
            for student in student_list:
                #判断输入的name是否和小列表里的name相等
                if student[0] !=name:
                    #找出与name不等的小列表所在的索引
                    index = student_list.index(student,0,len(student_list))
                    #将符合的小列表添加到list列表中
                    list.append(student_list[index])
            #判断两个列表长度是否是相等  相等说明大列表中不存在名字为name的小列表
            if len(student_list) == len(list):
                name = raw_input('姓名不存在，请重新输入：')
            else:
                #清空大列表
                del student_list[:]
                #循环将list列表内的内容写入到大列表中
                for dict in list:
                    student_list.append(dict)
                break

#1. 声明一个大列表，存放所有学生信息
student_list = []

#2.while循环
while True:
    print ('****************学生管理系统V2.0*******************')
    print ('1.添加学生')
    print ('2.查询学生')
    print ('3.修改学生')
    print ('4.删除学生')
    print ('0.退出程序')
    print ('***************************************************')

    #选择操作：
    num = int(raw_input('请选择您的操作：'))
    #判断选择项是否在范围之内
    while num not in range(0,5):
        #重新选择
        num = int(raw_input('没有该选项，请重新选择：'))
    #根据选择执行对应的操作
    if num ==1:
        #调用添加学生函数
        add_student()
    elif num ==2:
        #调用查询学生函数
        query_student()
    elif num ==3:
        #调用修改学生函数
        update_student()
    elif num ==4:
        #调用删除学生函数
        delete_student()
    else:
        print('程序已结束！')
        break






















