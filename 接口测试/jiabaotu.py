# -*-encoding:utf-8 -*-
from selenium import webdriver
import time

browser=webdriver.Chrome()
#打开浏览器，输入地址，并且最大化窗口
browser.get("http://120.26.50.11:8601/admin/login.html")
browser.maximize_window()
browser.implicitly_wait(10)
#输入用户名
browser.find_element_by_xpath("//input[@type='text']").send_keys("admin")
#输入密码
browser.find_element_by_xpath("//input[@type='password']")
#点击登录按钮


time.sleep(2)
#关闭浏览器
browser.quit()



