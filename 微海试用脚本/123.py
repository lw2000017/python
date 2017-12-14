# -*-encoding:utf-8 -*-
import time
import datetime
nowtime = time.strftime('%Y-%m-%d',time.localtime(time.time()))
# yestime = time.localtime('%Y-%m-%d',)
print(nowtime)
# print(yestime)
# print(help(time))


Nowtime = datetime.datetime.now()
Yestime = Nowtime + datetime.timedelta(days=-1,)
print(Yestime)