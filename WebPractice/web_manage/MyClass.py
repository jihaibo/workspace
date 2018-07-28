# -*- coding: utf-8 -*-
'''
实例应用
'''

mystr = raw_input("请输入你想知道的对象：")
class MyWorld:
    # 定义人的对象
    def person(self):
        self.mytalk = '我可以讲话阐述'
        self.mylimbs = '也可以用动作来表示'
        self.myeyes ='你可以眉目传情吗'
        print '我是人，因此我可以%s,%s,%s' %(self.mytalk,self.mylimbs,self.myeyes)

    # 定义猪的对象
    def pig(self):
        self.mytalk = '哼哼哼哼'
        self.myspecialty = '吃饭，睡觉'
        self.mymaster = '谁喂食，谁就是我的主人'
        print '我是猪，我的特点是%s,%s,%s' % (self.mytalk,self.myspecialty,self.mymaster)

    # 定义公鸡的对象
    def rooster(self):
        self.mywork = '天亮了打鸣'
        self.mymotto = '闻鸡起舞，说的就是我'
        print '我是公鸡，我可以%s,%s' %(self.mywork,self.mymotto)

if __name__ == '__main__':
    myworld = MyWorld()
    if mystr == '人':
        myworld.person()
    elif mystr == '猪':
        myworld.pig()
    elif mystr == '公鸡':
        myworld.rooster()
    else:
        print '不好意思，没有您输入的选项'
