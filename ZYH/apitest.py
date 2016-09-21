#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import os
import sys
import time
import requests
reload(sys)
sys.setdefaultencoding('utf-8')#查询系统默认编码
apiurl = "http://prod.devops.ihangmei.com/dashboard-api/api/job/20170728095506"
start = time.clock()
if not os.path.exists('response.json'):
    request = requests.get(apiurl)
    # request = requests.get(apiurl)
    response = request.content
    with open('response.json','w+') as f:
        f.write(response)
else:
    with open('response.json','r') as f:
        response =  f.read()
reg = re.compile(r'"mac":"(.*?)","status":"(.*?)".*?"result":"(.*?)","updateTime":"(.*?)"')
res = re.findall(reg,response)#查找所有的reg返回的值， 对象   文件
for i in res:
    print i
print u"总记录数:",len(res)
#print u"列名: --> mac,status,result,updateTime"
#print u"第1条记录: -->",res[0]
#print u"第10条记录: -->",res[10]
#print u"第100条记录: -->",res[100]
#print u"第1000条记录: -->",res[1000]
#print u"第10000条记录: -->",res[10000]
result_null_sum = 0
result_notnull_sum = 0
result_ok_sum = 0
result_new_sum = 0
result_other_sum = 0
status_pending_count = 0
status_success_count = 0
status_ongoing_count = 0
status_other_count = 0
for mac,status,result,updatetime in res:
    if result == "":
        result_null_sum += 1
    elif result == "download ok restart ok":
        result_ok_sum += 1
    elif result == "ops is new":
        result_new_sum += 1
    else:
        result_other_sum += 1
    if status == "success":
        status_success_count += 1
    elif status == "ongoing":
        status_ongoing_count += 1
    elif status == "pending":
        status_pending_count += 1
    else:
        status_other_count += 1
print "status : success -->",status_success_count
print "status : pending -->",status_pending_count
print "status : ongoing -->",status_ongoing_count
print "status : other -->",status_other_count
print "result : null -->",result_null_sum
print "result : ops is new -->",result_new_sum
print "result : download ok restart ok -->",result_ok_sum
print "result : other -->",result_other_sum
end = time.clock()
print u"运行时间: ",end-start,"秒"
for i in range(60):
    sys.stdout.write("*")
    sys.stdout.flush()
    time.sleep(0.1)

# print  os.getcwd()






