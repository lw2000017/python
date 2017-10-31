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
browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div[3]/div[1]").click()
#browser.implicitly_wait(10)
sleep(2)

#打开管家行程
browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div[3]/div[2]/div[2]/a").click()
browser.implicitly_wait(10)


#输入管家姓名
browser.find_element_by_css_selector("input[data-bind='value:manager']").send_keys("线下管家")
browser.implicitly_wait(10)


#选择年月份
browser.find_element_by_id("yeartime").clear()
browser.find_element_by_id("yeartime").send_keys("2016")
browser.implicitly_wait(10)

browser.find_element_by_id("montime").clear()
browser.find_element_by_id("montime").send_keys("05")
browser.implicitly_wait(10)



#选择所属区域
diqu=Select(browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div[4]/div[1]/div[3]/select[1]"))
diqu.select_by_visible_text("华东地区")
sleep(2)

sheng=Select(browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div[4]/div[1]/div[3]/select[2]"))
sheng.select_by_visible_text("浙江省")
sleep(2)

shi=Select(browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div[4]/div[1]/div[3]/select[3]"))
shi.select_by_visible_text("杭州市")
browser.implicitly_wait(10)

#点击确认查询按钮
try:
    browser.find_element_by_css_selector(".search").click()
    print("查询成功")
except Exception as e:
    print("查询失败")


#刷新界面
try:
    browser.refresh()
    print("刷新成功")
except Exception as e:
    print("刷新失败")

browser.implicitly_wait(10)

#定位到当前日期，并查看今天的详情
browser.find_element_by_css_selector("html body div#bd.sitebd div#manager.manager div.contents div.managermarchpart2 div.march div.weekcon div.eachmarch.active").click()
#browser.implicitly_wait(10)
sleep(2)

browser.find_element_by_css_selector("html body div#bd.sitebd div#manager.manager div.contents div.managermarchpart2 div.march div.weekcon div.eachmarch.active div.marchcon div.infobtn").click()
sleep(3)

#关闭弹出框
try:
    browser.find_element_by_css_selector(".delebtns").click()
    print("关闭成功")
except Exception as e:
    print("关闭失败")


browser.quit()





















