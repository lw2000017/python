# -*-encoding:utf-8 -*-
from selenium import webdriver
import time
#
# #给chromedriver一个路径
chromedriver = 'C:\Python\chromedriver.exe'
browser = webdriver.Chrome(chromedriver)
browser.get("http://120.26.50.11:8088/publish/crm/login.html")

class user_login():
    def login(self,username,password):
        browser.find_element_by_id("username").send_keys(username)
        browser.find_element_by_id('password').send_keys(password)
        time.sleep(1)
        browser.find_element_by_css_selector(".btnlogin").click()
        browser.maximize_window()

class user_logout():
    def logout(self):
        browser.find_element_by_id("loginuserimg").click()
        time.sleep(2)
        browser.find_element_by_id("loginquit").click()
        time.sleep(2)
        browser.quit()
