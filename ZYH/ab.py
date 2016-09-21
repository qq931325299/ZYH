#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 说明:
"""
api接口压力测试
url = "http://gd.wangfanwifi.com:16621/api/userAuth?time=300&product=wxlogin&limit=10000&open_type=temp"
"""

# -*- coding: utf8 -*-
# code by Shurrik
import threading, time, httplib

HOST = 'gd.wangfanwifi.com' #主机
PORT = '16621' #端口
URI = "/api/userAuth?time=300&product=wxlogin&limit=10000&open_type=temp" #相对地址

TOTAL = 0 #总数
SUCC = 0 #响应成功数
FAIL = 0 #响应失败数
EXCEPT = 0 #响应异常数
MAXTIME = 0 #最大响应时间
MINTIME = 100 #最小响应时间，初始值为100秒
GT3 = 0 #统计3秒内响应的
LT3 = 0 #统计大于3秒响应的

# 创建一个 threading.Thread 的派生类
class RequestThread(threading.Thread):
    # 构造函数
    def __init__(self, thread_name):
        threading.Thread.__init__(self)
        self.test_count = 0

    # 线程运行的入口函数
    def run(self):
        self.test_performace()

    def test_performace(self):
            global TOTAL
            global SUCC
            global FAIL
            global EXCEPT
            global GT3
            global LT3
            try:
                st = time.time()
                conn = httplib.HTTPConnection(HOST, PORT, False)
                conn.request('GET', URI)
                res = conn.getresponse()
                print ('[返回内容]: %s'% res.read())
                print ('[http状态码]: %s' % res.status)
                print ('\n')
                start_time
                if res.status == 200:
                    TOTAL += 1
                    SUCC += 1
                else:
                    TOTAL += 1
                    FAIL += 1
                time_span = time.time()-st
                print ('线程: %s\t时间: %f\n' % (self.name,time_span))
                self.maxtime(time_span)
                self.mintime(time_span)
                if time_span > 3:
                    GT3 += 1
                else:
                    LT3 += 1
            except Exception,e:
                print (e)
                TOTAL += c1
                EXCEPT += 1
            conn.close()
    def maxtime(self,ts):
            global MAXTIME
            # print '时间: %s' % ts
            if ts > MAXTIME:
                MAXTIME = ts
    def mintime(self,ts):
            global MINTIME
            if ts < MINTIME:
                MINTIME = ts

# main 代码开始
if __name__ == "__main__":
    print ('='*50+' api接口性能测试开始 '+'='*50)
    # 开始的时间
    start_time = time.time()
    # 并发的线程数
    thread_count = 400
    print ('并发数: %d' % thread_count)

    i = 0
    while i <= thread_count:
        t = RequestThread("thread" + str(i))
        t.start()
        i += 1

    t = 0
    #并发数所有都完成或大于60秒就结束
    while TOTAL < thread_count or t > 60:
            print ('总数: %d\t成功: %d\t失败: %d\t出错: %d\n' % (TOTAL,SUCC,FAIL,EXCEPT))
            t += 1
            time.sleep(1)

    print ('='*50+' api接口性能测试结束 '+'='*50)
    print ('api接口地址: http://%s:%s%s' % (HOST,PORT,URI))
    print ('并发数: %d' % thread_count)
    print ('总数: %d\t成功: %d\t失败: %d\t出错: %d' % (TOTAL,SUCC,FAIL,EXCEPT))
    print ('成功率: %0.2f\t失败率: %0.2f\t出错率: %0.2f' % (float(SUCC)/float(TOTAL),float(FAIL)/float(TOTAL),float(EXCEPT)/float(TOTAL)))
    # print '最大响应时间: ',MAXTIME
    # print '最小响应时间: ',MINTIME
    # print '大于3秒的请求数: %d\t百分比: %0.2f' % (GT3,float(GT3)/TOTAL)
    # print '小于3秒的请求数: %d\t百分比: %0.2f' % (LT3,float(LT3)/TOTAL)
    print ('='*50+' api接口性能测试结束 '+'='*50)


