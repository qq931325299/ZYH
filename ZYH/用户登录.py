#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author：Huajia
# 模拟用户登录

p = 0
list1 = []
user = {}
f1 = open("account_lock.txt", "r+", encoding="utf-8")  # 打开用户锁定文件
f2 = open("account.txt", "r+", encoding="utf-8")  # 打开存用户名密码文件
# 读取文件F1的内容并把每行的\n去掉然后加入到list这个空列表
for lock_list in f1.readlines():
    list1.append(lock_list.strip())
f1.close()
# 读取文件F2的内容，并把数据写入user这个空字典里面去
for list2 in f2.readlines():
    list2 = list2.strip().split()
    user[list2[0]] = list2[1]
f2.close()
for i in range(3):  # 进入大循环，用户名错误3次自动退出系统。
    user_name = input("请输入用户名：")
    if user_name in list1:  # 判断输入的用户名是否在list列表里面
        print("用户名\033[31;1m %s \033[0m已经被锁定，请联系管理员！" % (user_name))
        continue  # 提示完用户被锁定继续进行下面程序的执行
    if user_name in user:
        while p < 3:  # 循环判断密码输入错误3次锁定该用户
            password = input("请输入密码：")  # 输入密码
            if user[user_name] == password:  # 判断密码是否正确，如果正确提示登录成功，如果不正确则提示“密码错误，重新输入”。注：错误3次，锁定用户
                print("用户名密码正确，登录成功！！")
                exit()
            elif user[user_name] != password:
                print("密码错误，请重新输入！还有%d次机会"% (2 -p) )
                p += 1
        else:
            print("密码已经输错3次，用户 \033[31;1m %s \033[0m 被锁定,请联系管理员解锁用户！" % (user_name))
            f1 = open("account_lock.txt", "a", encoding="utf-8")  # 打开F1这个文件，将锁定的用户名写入锁定文件。
            user_name = "%s\n" % (user_name)
            f1.write(user_name)
        exit()
    else:
        print("你输入的用户名 \033[31;1m %s \033[0m 不存在，请重新输入！" % (user_name))
else:
    print("用户名三次错误，自动退出程序！")
