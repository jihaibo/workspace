# -*- coding:utf-8 -*-
author = 'haibo'
time = '2018-7-23'
"""
模拟购物
"""

class Goods:
    """
    购买物品
    """
    def buyGoods(self):
        """
        函数
        :return:
        """
        if __name__ == '__main__':
            goods = raw_input('您是否购买商品？Y/N，请选择：')
            if goods == 'y':
                goodsName = raw_input('请输入商品名称:')
                num = int(raw_input('请输入商品数量：'))
                print ('您要购买的商品为：%s,数量为：%s'%(goodsName,num))
                print ('商品单价为：5元，总价格为：%s' %(5*num))
            else:
                print "不购买任何物品"
        else:
            print "放弃参加活动"

print Goods.__doc__
print Goods.buyGoods.__doc__

print Goods.buyGoods()



















