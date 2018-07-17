# -*- coding: utf-8 -*-
'''
    1、添加学员
    2、修改学员
    3、查询学员
    4、删除学员
    0、退出程序
'''
student_list = []
while True:
    print ('1.添加学员')
    print ('2.修改学员')
    print ('3.查询学员')
    print ('4.删除学员')
    print ('0.退出程序')
    sel_num = raw_input("请输入您要进行的操作：")
    sel_num = int(sel_num)
    #如果选择的数字不在0~5 继续选择
    while sel_num not in range(0,5):
        sel_num = raw_input('您的选择不在范围之内，请重新选择：')
        sel_num = int(sel_num)
    if sel_num ==1:
        name = raw_input('请输入姓名：')
        age = raw_input('请输入年龄：')
        sex = raw_input('请输入性别：')
        person_list = [name,age,sex]
        student_list.append(person_list)
        print ('添加成功！')
    elif sel_num ==2:
        for x in range(0,len(student_list)):
            person = student_list[x]
            print ('序号：%s 姓名：%s 年龄：%s 性别：%s '%(x,person[0],person[1],person[2]))
        index = raw_input('请输入要修改的序号：')
        index = int(index)
        while index not in range(0,len(student_list)):
            index = raw_input("您选择的序号无效，请重新选择：")
            index = int(index)
        person = student_list[index]
        name = person[0]
        age = person[1]
        sex = person[2]
        student_list[index][0] = raw_input('请输入修改后的姓名：(%s):'%name)
        student_list[index][1] = raw_input('请输入修改后的年龄：(%s):'%age)
        student_list[index][2] = raw_input('请输入修改后的性别：(%s):'%sex)
        print ('修改成功')
    elif sel_num==3:
        for x in range(0,len(student_list)):
            person = student_list[x]
            name = person[0]
            age = person[1]
            sex = person[2]
            print ('序号：%s 姓名：%s 年龄：%s 性别：%s'%(x,name,age,sex))
    elif sel_num==4:
        for x in range(0,len(student_list)):
            person = student_list[x]
            print ('序号：%s 姓名：%s 年龄：%s 性别：%s'%(x,person[0],person[1],person[2]))
        print ('1.删除所有学员')
        print ('2.删除选择的学员')
        num = raw_input('请输入您的选择：')
        num = int(num)
        while num not in range(1,3):
            num = raw_input("您的选择无效，请重新选择：")
            num = int(num)
        if num ==1:
            student_list.clear()
        else:
            index = raw_input('请输入您要删除的学员序号：')
            index = int(index)
            while index not in range(0,len(student_list)):
                index = raw_input("您选择的序号无效，请重新选择：")
                index = int(index)

            del student_list[index]
    else:
        break























