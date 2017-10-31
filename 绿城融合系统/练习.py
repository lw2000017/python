# -*-encoding:utf-8 -*-
'''
from selenium import webdriver
import time
chromedriver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
browser = webdriver.Chrome(chromedriver)
browser.get("http://www.baidu.com")
browser.implicitly_wait(10)
browser.find_element_by_id("kw").send_keys("python")
browser.implicitly_wait(10)
browser.find_element_by_id("su").click()
browser.implicitly_wait(10)
browser.find_element_by_link_text("Python_百度百科").click()
time.sleep(3)
windows=browser.window_handles#获取当前窗口的句柄
browser.switch_to.window(windows[-1])#切换至另一个窗口
time.sleep(3)
browser.find_element_by_link_text("源代码").click()
time.sleep(3)
browser.find_element_by_link_text("胶水语言").click()
time.sleep(3)
windows=browser.window_handles
browser.switch_to.window(windows[-1])
browser.close()
time.sleep(2)
windows=browser.window_handles
browser.switch_to.window(windows[-1])
browser.close()
'''

# L=[1,2,3,4,5,6,7,8,9,0]
# n=int(input("qing shuru :"))
# for i in range(n):
#     print(i)
#
# print([x*x for x in range(1,10) ])


# n=1
# while n<100:
#     if n>10:
#         break
#     print n
#     n=n+1


from selenium import webdriver
import time
chromedriver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
browser = webdriver.Chrome(chromedriver)
browser.get("http://www.baidu.com")

guanjianzi={"selenium","ceshi","ceshi1","ceshi2"}


for i in guanjianzi:
    if i == "selenium":
        browser.find_element_by_id("kw").clear()
        browser.find_element_by_id("kw").send_keys(i)
        browser.implicitly_wait(10)
        browser.find_element_by_id("su").click()
        print(i)
        break
    else:
        browser.find_element_by_id("kw").clear()
        browser.find_element_by_id("kw").send_keys(i)
        print(i)







