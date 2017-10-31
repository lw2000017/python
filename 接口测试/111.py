# -*-encoding:utf-8 -*-
# from selenium import webdriver
# import time
#
#
# browser=webdriver.Chrome()
#
# browser.get("http://120.26.50.11:8088/publish/crm/login.html")
#
# browser.maximize_window()
#
# time.sleep(2)
# browser.find_element_by_id("username").send_keys("admin")
# browser.implicitly_wait(10)
# browser.find_element_by_id("password").send_keys("admin123")
# browser.implicitly_wait(10)
# browser.find_element_by_css_selector(".btnlogin").click()
#
#
# browser.find_element_by_xpath('//*[@id="manager"]/div[3]/div[3]/div[2]/div[2]/div[2]/div[1]/button').click()
# browser.find_element_by_xpath("")

import math

nian=input("qingshurunianfen:")
nians=int(nian)

if nians%400==0 or nians%4==0:
    if nians%100!=0:
        print(str(nians)+"年"+"是闰年")
        print("%d年是闰年" % nians)
    else:
        print(str(nians)+"年"+"不是闰年")
        print("%d年不是闰年" % nians)
else:

    print(str(nians)+"年"+"不是闰年")
    print("%d年不是闰年"%nians)


# 12*34+78-132/6
a=12*34
b=132/6
print(a+78-b)
