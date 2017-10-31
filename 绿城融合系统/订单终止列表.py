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
browser.find_element_by_id("managerPower").click()
browser.implicitly_wait(10)

#打开订单终止列表
browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div[1]/div[1]").click()#打开订单管理

browser.implicitly_wait(10)
browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div[1]/div[1]").click()#打开订单管理
browser.implicitly_wait(10)
browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[4]/a").click()#打开订单终止列表

browser.implicitly_wait(10)


#条件筛选


browser.find_element_by_id("filtertermstart").clear()
browser.find_element_by_id("filtertermstart").send_keys("2017-05-24")#输入申请终止服务时间的开始时间
browser.implicitly_wait(10)

browser.find_element_by_id("filtertermend").clear()
browser.find_element_by_id("filtertermend").send_keys("2017-05-27")#输入申请终止服务时间的结束时间
browser.implicitly_wait(10)

#选择退款状态
select=Select(browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div[4]/div[1]/div[2]/select"))
select.select_by_visible_text("已受理")
browser.implicitly_wait(10)

#选择退款理由
select1=Select(browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div[4]/div[1]/div[3]/select"))
select1.select_by_visible_text("装修延期")
browser.implicitly_wait(10)

#选择订单状态
select2=Select(browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div[4]/div[1]/div[4]/select"))
select2.select_by_visible_text("已付款已派单")
browser.implicitly_wait(10)

#点击确认查询按钮
browser.find_element_by_css_selector(".search").click()
browser.implicitly_wait(10)



#判断是否刷新界面，成功或失败都返回一个值
try:
    browser.refresh()
    print("第一次刷新成功")
except Exception as e:
    print("第一次刷新失败")


sleep(2)
#选择每页显示数
try:
    select3=Select(browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[3]/div[4]/div[3]/select"))
    select3.select_by_visible_text("20")
    browser.implicitly_wait(10)
    browser.find_element_by_css_selector(".jumpenter").click()#点击确定按钮
    browser.implicitly_wait(10)
    print("跳转成功")
except Exception as e:
    print("跳转失败")


try:
    browser.refresh()
    print("第二次刷新成功")
except  Exception   as e:
    print("第二次刷新失败")

sleep(2)
#点击 上一页和下一页
try:
    browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[3]/div[4]/div[5]").click()#点击上一页
    print("跳转上一页成功")
except Exception as e:
    print("跳转上一页失败")
sleep(2)
try:
    browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[3]/div[4]/div[6]").click()#点击下一页
    print("跳转下一页成功")
except Exception as e:
    print("跳转下一页失败")
browser.implicitly_wait(10)

try:
    browser.refresh()
    print("第三次刷次成功")
except Exception as e:
    print("第三次刷新失败")


#手动输入页面
browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[3]/div[4]/div[7]/input").clear()
browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[3]/div[4]/div[7]/input").send_keys("5")#手动输入5
browser.implicitly_wait(10)
browser.find_element_by_css_selector(".jumpenter").click()

sleep(1)
#退出
browser.find_element_by_css_selector(".userimg").click()#点击头像，登录名
sleep(2)
browser.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div[2]/div[4]/div[4]/div").click()#点击退出按钮
sleep(2)



try:
    browser.find_element_by_css_selector(".title")
    print("退出成功")
except  Exception as  e:
    print("退出失败")


sleep(1)


browser.quit()