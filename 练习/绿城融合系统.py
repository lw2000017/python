# -*-encoding:utf-8 -*-
#调用包
from selenium import webdriver
from  time import  *
#给chromedriver一个路径
chromedriver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
browser = webdriver.Chrome(chromedriver)
#打开浏览器
browser.get("http://120.26.50.11:8088/publish/crm/login.html")

#输入用户名和密码（通过id定位）
sleep(2)
browser.find_element_by_id("username").send_keys("admin")
browser.find_element_by_id("password").send_keys("admin123")
#点击登陆按钮，通过xpath定位
sleep(1)
browser.find_element_by_xpath("/html/body/div[2]/div/form/div[3]/button").click()
#最大化窗口
browser.maximize_window()
sleep(2)

# #打开管家部管理-管家管理-管家行程
# browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div[2]/div[1]").click()
# sleep(2)
# browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[2]/a").click()
# sleep(2)
# #打开客服管理
# browser.find_element_by_id("customPower").click()
# sleep(2)
# browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div[2]/a").click()
# sleep(2)
#
# #输入订单编号
# #browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div[4]/div[1]/div[1]/input").send_keys("OW20170522398681")
#
# #sleep(1)
# #点击回访状态下拉菜单
# browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div[4]/div[1]/div[2]/select").click()
# sleep(1)
# #选择售中待回访状态
# browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div[4]/div[1]/div[2]/select/option[3]").click()
# sleep(1)
# #点击确认查询按钮
# browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div[4]/div[4]").click()
#
# sleep(1)


browser.find_element_by_id("managerPower").click()
browser.implicitly_wait(10)

browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div[3]/div[1]").click()
browser.implicitly_wait(10)

browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div[3]/div[2]/div[1]/a").click()
browser.implicitly_wait(10)
sleep(2)

browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[3]/div[2]/div[2]/div[2]/div[4]/button").click()
browser.implicitly_wait(10)


browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/button").click()
sleep(5)

browser.find_element_by_css_selector("[type='text']").clear()
browser.implicitly_wait(10)


browser.find_element_by_css_selector("[type='text']").send_keys('测试测试')
browser.implicitly_wait(10)


browser.find_element_by_css_selector("[class='okenter']").click()
browser.implicitly_wait(10)


browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[3]/div[2]/div[2]/div[2]/div[4]/button").click()





















#点击头像
browser.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div[2]/div[4]/img").click()
sleep(2)
#点击退出按钮
browser.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div[2]/div[4]/div[4]/div").click()
sleep(2)
#退出浏览器
browser.quit()
