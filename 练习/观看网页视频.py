# -*-encoding:utf-8 -*-
#调用包
from selenium import webdriver
from  time import  *
#给chromedriver一个路径
chromedriver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
browser = webdriver.Chrome(chromedriver)
#打开浏览器
browser.get("http://tv.le.com")
sleep(2)
browser.maximize_window()
#点击搜索框，输入搜索关键字
sleep(2)
browser.find_element_by_name("wd").clear()
browser.find_element_by_name("wd").send_keys("白鹿原")
sleep(2)
# browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/form/input[2]").click()

#模拟键盘回车，相当于点击搜索按钮
browser.find_element_by_name("wd").submit()
#查询的结果显示，点击文本链接，白鹿原
sleep(2)
browser.find_element_by_xpath("/html/body/div[7]/div/div[2]/div[4]/div/a[16]").click()

