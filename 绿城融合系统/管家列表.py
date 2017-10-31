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


#打开管家列表
browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[1]/a").click()
browser.implicitly_wait(10)


#选择地址

select1=Select(browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div[5]/div[1]/div[1]/select[1]"))
select1.select_by_visible_text("华东地区")
sleep(1)

select2=Select(browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div[5]/div[1]/div[1]/select[2]"))
select2.select_by_visible_text("浙江省")
sleep(1)

select3=Select(browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div[5]/div[1]/div[1]/select[3]"))
select3.select_by_visible_text("杭州市")
browser.implicitly_wait(10)

#输入手机号
browser.find_element_by_css_selector("input[data-bind='value:phone']").send_keys("13102011012")
browser.implicitly_wait(10)


#输入管家姓名
browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div[5]/div[1]/div[3]/input").send_keys("线下管家1")
browser.implicitly_wait(10)

#选择管家等级
select4=Select(browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div[5]/div[1]/div[4]/select"))
select4.select_by_visible_text("资深管家")
browser.implicitly_wait(10)

#点击确认查看按钮
try:
    browser.find_element_by_css_selector(".search").click()
    print("查询成功")
except Exception as e:
    print("查询失败")

browser.implicitly_wait(10)
#刷新界面
try:
    browser.refresh()
    print("第一次刷新成")
except Exception as e:
    print("第一次刷新失败")

browser.implicitly_wait(10)


#选择每页显示数
select5=Select(browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[3]/div[4]/div[3]/select"))
select5.select_by_visible_text("20")
browser.implicitly_wait(10)


#点击确定按钮
try:
    browser.find_element_by_css_selector(".jumpenter").click()
    print("第一次跳转成功")
except Exception as e:
    print("第一次跳转失败")

browser.implicitly_wait(10)

#再次刷新界面
try:
    browser.refresh()
    print("第二次刷新成功")
except Exception as e:
    print("第二次刷新失败")

browser.implicitly_wait(10)


#点击上一页和下一页
try:
    browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[3]/div[4]/div[5]").click()
    print("跳转上一页成功")
except Exception as e:
    print("跳转上一页失败")

browser.implicitly_wait(10)

try:
    browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[3]/div[4]/div[6]").click()
    print("跳转下一页成功")
except Exception as e:
    print("跳转下一页失败")

browser.implicitly_wait(10)


#输入跳转页码
browser.find_element_by_css_selector("input[data-bind='value:jumppage']").send_keys("5")

browser.implicitly_wait(10)

try:
    browser.find_element_by_css_selector(".jumpenter").click()
    print("第2次跳转成功")
except Exception as e:
    print("第2次跳转失败")

browser.implicitly_wait(10)



#再次刷新界面
try:
    browser.refresh()
    print("第3次刷新成功")
except Exception as e:
    print("第3次刷新失败")

sleep(2)



#点击新增管家按钮
browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/button").click()
browser.implicitly_wait(10)

#输入管家姓名
browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div[3]/div[2]/div[2]/div[1]/input").send_keys("测试输入")
sleep(2)

#选择生日
browser.find_element_by_id("birthday").send_keys("2017-06-01")
sleep(2)


#点击关闭按钮
try:
    browser.find_element_by_css_selector(".delebtn").click()
    print("关闭成功")
except Exception as e:
    print("关闭失败")


sleep(2)


#退出
browser.find_element_by_id("loginuserimg").click()
sleep(1)


browser.find_element_by_css_selector(".loginoutbtn").click()
sleep(2)


try:
    browser.find_element_by_xpath("/html/body/div[2]/div/div")
    print("退出成功")
except Exception as e:
    print("退出失败")


sleep(1)

browser.quit()