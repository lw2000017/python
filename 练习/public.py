# -*-encoding:utf-8 -*-

from selenium import webdriver
from time import *

#
# #调用
# def diaoyong():
#     chromedriver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
#     browser = webdriver.Chrome(chromedriver)
# #打开浏览器
#     browser.get("http://120.26.50.11:8088/publish/crm/login.html")
#     sleep(2)

class login():

    def user_login(self,browser):
    #输入用户名和密码（通过id定位）
        browser.find_element_by_id("username").send_keys("admin")
        browser.find_element_by_id("password").send_keys("admin123")
    #点击登陆按钮，通过xpath定位
        sleep(1)
        browser.find_element_by_xpath("/html/body/div[2]/div/form/div[3]/button").click()
    #最大化窗口
        browser.maximize_window()
        sleep(2)
    def user_logout(self,browser):
        browser.find_element_by_id("loginuserimg").click()
        sleep(2)
        # 点击退出按钮
        browser.find_element_by_css_selector(".loginoutbtn").click()
        sleep(2)
        # 退出浏览器
        browser.quit()




