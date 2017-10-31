# -*-encoding:utf-8 -*-
from selenium import webdriver
from time import *
chromedriver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
browser = webdriver.Chrome(chromedriver)
browser.get("http://120.26.50.11:8088/publish/crm/login.html")


browser.implicitly_wait(10)
#输入错误的账号和密码
browser.find_element_by_id("username").send_keys("admin")
browser.implicitly_wait(10)
browser.find_element_by_id("password").send_keys("123456")
browser.implicitly_wait(10)
browser.find_element_by_css_selector(".btnlogin").click()

try:
    browser.implicitly_wait(10)
    browser.find_element_by_xpath("//*[@id='dialog']/div[1]").click()
    print("用户名和密码错误")
except Exception as  e:
    print("用户名和密码没有错误")

browser.implicitly_wait(10)

browser.find_element_by_id("dialogok").click()
browser.implicitly_wait(10)
#输入正确的账号和密码
browser.find_element_by_id("username").clear()
browser.find_element_by_id("username").send_keys("admin")
browser.implicitly_wait(10)
browser.find_element_by_id("password").clear()
browser.find_element_by_id("password").send_keys("admin123")
browser.implicitly_wait(10)
browser.find_element_by_css_selector(".btnlogin").click()
try:
    browser.implicitly_wait(10)
    browser.find_element_by_xpath("//*[@id='manager']/div[3]/div[1]/div[1]/div[1]")
    print("用户名和密码正确")
except Exception as  e:
    print("-------")


browser.quit()