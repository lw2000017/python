# -*-encoding:utf-8 -*-

from selenium import webdriver
from  time import  *
#给chromedriver一个路径
chromedriver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
browser = webdriver.Chrome(chromedriver)
#打开浏览器
browser.get("http://120.26.50.11:8088/publish/crm/login.html")



browser.implicitly_wait(10)


browser.find_element_by_id("username").send_keys("admin")

browser.find_element_by_id("password").send_keys("admin123")

sleep(1)


browser.find_element_by_xpath("/html/body/div[2]/div/form/div[3]/button").click()

browser.quit()