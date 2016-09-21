#！-*- coding:utf-8 -*-

shoping = [
    ('苹果手机',6400),
    ('笔记本电脑',8600),
    ('手表',3000),
    ('机票',5000),
    ('汽车',9990),
    ('书',400)
]

shoping1 = [] #存放已买商品
salary = input("输入你的工资>:")
if salary.isdigit():#判断是不是整数
    salary = int(salary)
    while True:
        for index,item in enumerate(shoping):#index获取商品下标，enumerate把下标从列表取出来
            print(index,item)
        user_choice = input("请输入要买的商品编号>>>：")
        if user_choice.isdigit():#判断是不是数字
            user_choice = int(user_choice)#转成整型
            if user_choice < len(shoping) and user_choice>=0:#判断列表长度len
                p_item = shoping[user_choice]#获取商品价格
                if p_item[1]<= salary:#判断商品价格，是否买得起
                    shoping1.append(p_item)#
                    salary -= p_item[1]#减钱
                    print("你以消费%s,你的余额还有\033[31;1m%s\033[0m" % (p_item[1],salary))
                else:
                    print("你的余额只剩\033[41;1m[%s]\033[0m请充值"% salary)
            else:
                print("商品不在列表中%s" % user_choice)
        elif user_choice == 'q':
            print("---你购买了---")
            for p in shoping1:
                print(p)
                exit("你的剩余余额为"% salary)
        else:
            print("你输入的是错误选项")



