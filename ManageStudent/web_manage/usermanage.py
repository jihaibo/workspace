# -*- coding:utf-8 -*-
author = 'haibo'
time = '2018-7-23'
"""
用字典保存实现用户账号管理
"""
db = {'haibo':'123456'}

# 新用户，需要注册
def newuser():
    prompt = '请输入注册账号：'
    while True:
        name = raw_input(prompt)
        # 检查字典中是否已经存在键为用户注册账号的元素
        if db.has_key(name):
            prompt = '您注册的账号已经存在，请使用其他账号注册：'
            continue
        else:
            password = raw_input('请输入注册密码：')
            # 将用户注册的账号与密码作为字典的键-值对
            db[name] =password
            break

# 如果已经注册过，则需要登录
def olduser():
    name = raw_input("请输入登录的账号：")
    password = raw_input("请输入登录密码：")
    # 获取注册账号所对应的密码
    userpwd = db.get(name)
    if userpwd == password:
        print "欢迎登录：",name
    else:
        print "您的用户名或密码错误，请重新登录！"

# 显示系统界面
def showmenu():
    prompt = '请选择操作（n：注册 e :登录）：'
    con = False
    while not con:
        chosen = False
        while not chosen:
            try:
                # 将用户输入的字母小写格式化
                choice = raw_input(prompt).strip()[0].lower()
            except (EOFError,KeyboardInterrupt):
                choice = 'q'
            print '您按下了【%s】键' % choice
            if choice not in 'ne':
                print '您输入的内容不合法，请重新输入：'
            else:
                chosen = True
                con = True
            if choice =='n':
                newuser()
            elif choice == 'e':
                olduser()
            else:
                showmenu()

showmenu()










































