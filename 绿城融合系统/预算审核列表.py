# -*-encoding:utf-8 -*-

from selenium import webdriver
from  time import  *
from  selenium.webdriver.support.ui import Select
from  selenium.webdriver.common.keys import Keys

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

sleep(2)





#打开管家部管理
browser.find_element_by_id("managerPower").click()
browser.implicitly_wait(10)

#打开预算审核列表
browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div[1]/div[1]").click()#打开订单管理

browser.implicitly_wait(10)
browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div[1]/div[1]").click()#打开订单管理
browser.implicitly_wait(10)
browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/a").click()#打开预算审核列表

browser.implicitly_wait(10)



#条件筛选

browser.find_element_by_id("filtertermstart").clear()
browser.find_element_by_id("filtertermstart").send_keys("2017-05-24")#输入下单时间的开始时间
browser.implicitly_wait(10)

browser.find_element_by_id("filtertermend").clear()
browser.find_element_by_id("filtertermend").send_keys("2017-05-27")#输入下单时间的结束时间
browser.implicitly_wait(10)


#输入订单编号
browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/div[4]/div[1]/div[2]/input").send_keys("OW20170522576521")
browser.implicitly_wait(10)

#输入业主姓名
browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/div[4]/div[1]/div[3]/input").send_keys("测试")
browser.implicitly_wait(10)


#输入管家姓名
browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/div[4]/div[1]/div[4]/input").send_keys("线下管家")
browser.implicitly_wait(10)

#输入审核报告编号
browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/div[4]/div[3]/div[1]/input").send_keys("L20170522791186")
browser.implicitly_wait(10)


#选择订单状态
select=Select(browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/div[4]/div[3]/div[2]/select"))
select.select_by_visible_text("已付款已派单")
browser.implicitly_wait(10)


#选择审核状态
select=Select(browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/div[4]/div[3]/div[3]/select"))
select.select_by_visible_text("已提交")
browser.implicitly_wait(10)


#选择地址

#选择省份
select=Select(browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/div[4]/div[5]/select[1]"))
select.select_by_visible_text("浙江省")
browser.implicitly_wait(10)

#选择市
select=Select(browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/div[4]/div[5]/select[2]"))
select.select_by_visible_text("杭州市")
browser.implicitly_wait(10)

#选择区
select=Select(browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/div[4]/div[5]/select[3]"))
select.select_by_visible_text("余杭区")
browser.implicitly_wait(10)

#输入地址
browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/div[4]/div[5]/input").send_keys("梦想小镇")
browser.implicitly_wait(10)


#点击确认查询按钮
browser.find_element_by_css_selector(".search").click()

#判断是否刷新界面，成功或失败都返回一个值
try:
    browser.refresh()
    print("刷新成功")
except Exception as e:
    print("刷新失败")



#选择每页显示数
select =Select(browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div[4]/div[3]/select"))
select.select_by_visible_text("20")#每页显示20条
browser.implicitly_wait(10)
browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div[4]/div[8]").click()#点击确定按钮
browser.implicitly_wait(10)
# try:
#     shurzi = browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[3]/div[2]/div[1]/div[2]/div[229]").text
#     print("shuzi")
# except Exception as e:
#     print("shibai")
browser.refresh()
sleep(2)
#点击 上一页和下一页
try:
    browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div[4]/div[5]").click()#点击上一页
    print("跳转上一页成功")
except Exception as e:
    print("跳转上一页失败")
sleep(2)
try:
    browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div[4]/div[6]").click()#点击下一页
    print("跳转下一页成功")
except Exception as e:
    print("跳转至下一页失败")
browser.implicitly_wait(10)


#手动输入页面
browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div[4]/div[7]/input").clear()
browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div[4]/div[7]/input").send_keys("5")#手动输入5
browser.implicitly_wait(10)
browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div[4]/div[8]").click()

sleep(1)

browser.find_element_by_css_selector(".userimg").click()
sleep(2)
browser.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div[2]/div[4]/div[4]/div").click()
# try:
#     browser.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div[2]/div[4]/div[4]/div").click()
#     print("退出成功")
# except Exception as e:
#     print("退出失败")
sleep(1)







browser.quit()







































