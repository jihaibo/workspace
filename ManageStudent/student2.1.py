# -*- coding:utf-8 -*-
'''
学生管理系统
函数版--用字典存放学员信息
'''
def add_student():
    name = raw_input('请输入学生姓名：')
    age = raw_input('请输入学生年龄：')
    phone = raw_input('请输入学生电话：')
    #把name、age、phone放在小字典中
    student = {'name':name,'age':age,'phone':phone}
    #把小字典添加到所有学生的大列表中
    student_list.append(student)
    print ('添加学生成功！')


def query_student():
    print ('1.查询所有学生')
    print ('2.查询部分学生')
    num = int(raw_input('请选择查询方式：'))
    while num not in range(1,3):
        num = int(raw_input('选择无效，请重新选择查询方式：'))
    if num ==1:
        print ('********学生信息表*********')
        for x in range(0,len(student_list)):
            student = student_list[x]
            name = student['name']
            age = student['age']
            phone = student['phone']
            print ('序号：%s 姓名：%s 年龄：%s 电话：%s'%(x,name,age,phone))
    else:
        name = raw_input('请输入您要查询的学生姓名：')
        while 1:
            a = False
            for student in student_list:
                if student['name'] == name:
                    index = student_list.index(student,0,8)
                    print ('序号：%s 姓名：%s 年龄：%s 电话：%s'%(index,student_list[index]['name'],student_list[index]['age'],student_list[index]['phone']))
                    a = True
            if a ==False:
                name = raw_input('该学生没有找到，请输入正确的学生姓名：')
            else:
                break


def update_student():
    if len(student_list) == 0:
        print ('没有学生信息，无法进行修改!')
        return
    query_student()
    num = int(raw_input('请选择要修改的学生序号：'))
    while num not in range(0,len(student_list)):
        num =int(raw_input('没有该序号，请重新输入：'))
    #根据选择的序号取出对应的小字典
    student = student_list[num]
    new_name = raw_input('请输入修改后的姓名（%s）:'%student['name'])
    new_age = raw_input('请输入修改后的年龄（%s）:'%student['age'])
    new_phone = raw_input('请输入修改后的电话（%s）:'%student['phone'])
    #修改小字典中的数据
    student['name'] = new_name
    student['age'] = new_age
    student['phone'] = new_phone
    print ('修改数据成功！')


def delete_student():
    if len(student_list)==0:
        print ('无学生信息，无法进行删除操作！')
        return
    print ('1.根据序号删除')
    print ('2.删除所有的学生')
    print ('3.根据学生姓名删除学生')

    num = int(raw_input('请选择您的删除方式：'))
    while num not in range(1,4):
        num = int(raw_input('请选择正确的删除方式：'))
    if num ==1:
        query_student()
        num = int(raw_input('请输入您要删除的序号：'))
        while num not in range(0,len(student_list)):
            num = int(raw_input('请输入正确的学生序号进行删除：'))
        is_del = raw_input('您确定要删除(%s)学生的信息吗？（y/n）：'%student_list[num]['name'])
        if is_del=='y':
            student_name = student_list[num]['name']
            del student_list[num]
            print ('%s学生信息删除成功！'%student_name)
        else:
            print ('已取消删除学生信息操作！')

    elif num ==2:
        is_del = raw_input('您确定要删除所有学生信息吗？y(确认)/n（取消）：')
        if is_del =='y':
            del student_list[:]
            print ('已删除所有学生信息！')
        else:
            print ('删除所有学生操作已取消！')

    else:
        name = raw_input('请输入您要删除的学生姓名：')
        while 1:
            list = []
            for student in student_list:
                if student['name'] !=name:
                    #找出与name不等于的小字典所在的索引
                    index = student_list.index(student)
                    #将符合的小字典添加到list列表中
                    list.append(student_list[index])
            # 判断两个列表长度是否相等  相等说明大列表中不存在名字为name的小列表
            if len(student_list) ==len(list):
                name = raw_input('学生姓名不存在，请重新输入：')
            # 存在符合的小字典
            else:
                del student_list[:]
                for dict in list:
                    student_list.append(dict)
                break


# 声明一个列表，存放学生信息
student_list = []

while True:
    print ('************学生管理系统***************')
    print ('1.添加学生')
    print ('2.查询学生')
    print ('3.修改学生')
    print ('4.删除学生')
    print ('0.退出系统')
    print ('***************************************')

    num = int(raw_input('请选择您的操作：'))
    while num not in range(0,5):
        num = int(raw_input('没有该选项，请重新选择：'))

    if num ==1:
        add_student()
    elif num ==2:
        query_student()
    elif num ==3:
        update_student()
    elif num ==4:
        delete_student()
    else:
        print('程序已结束')
        break





























