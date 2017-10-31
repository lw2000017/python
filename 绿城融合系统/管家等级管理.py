# -*-encoding:utf-8 -*-

from selenium import webdriver
from  time import  *
from  selenium.webdriver.support.ui import Select

#给chromedriver一个路径
chromedriver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
browser = webdriver.Chrome(chromedriver)
#打开浏览器
browser.get("http://120.26.50.11:8088/publish/crm/login.html")



browser.implicitly_wait(10)

#输入账号和密码
browser.find_element_by_id("username").send_keys("admin")

browser.find_element_by_id("password").send_keys("admin123")

sleep(1)

#点击登录按钮
browser.find_element_by_xpath("/html/body/div[2]/div/form/div[3]/button").click()


browser.maximize_window()

browser.implicitly_wait(10)

#打开管家部管理

browser.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div[2]/div[1]/a").click()
browser.implicitly_wait(10)


#打开管家管理
browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div[2]/div[1]").click()
browser.implicitly_wait(10)

sleep(2)
#打开管家等级管理
browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[3]/a").click()
browser.implicitly_wait(10)


#选择等级名称
select1=Select(browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div[5]/div[1]/div[1]/select"))
select1.select_by_visible_text("资深管家")

browser.find_element_by_css_selector(".search").click()

browser.implicitly_wait(10)


try:
    browser.refresh()
    print("第一次刷新成功")
except Exception as e:
    print("第一次刷新失败")

#选择区域
select2=Select(browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div[5]/div[1]/div[2]/select[1]"))
select2.select_by_visible_text("华东地区")
sleep(1)

select3=Select(browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div[5]/div[1]/div[2]/select[2]"))
select3.select_by_visible_text("浙江省")
sleep(1)

select4=Select(browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div[5]/div[1]/div[2]/select[3]"))
select4.select_by_visible_text("杭州市")
sleep(1)



browser.find_element_by_css_selector(".search").click()


try:
    browser.refresh()
    print("第二次刷新成功")
except Exception as e:
    print("第二次刷新失败")





















