# -*-encoding:utf-8 -*-
#调用类
from time import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chromedriver='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
driver=webdriver.Chrome(chromedriver)
driver.get("http://www.baidu.com")
#输入框输入内容
driver.find_element_by_id("kw").send_keys("seleniumm")
sleep(1)
#删除多输入的m
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
sleep(1)
#输入空格键+“教程”汉字
driver.find_element_by_id("kw").send_keys(Keys.SPACE)
driver.find_element_by_id("kw").send_keys("教程")
sleep(1)
#ctrl+a 全选输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
sleep(1)

#ctrl+x 剪切输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
sleep(1)
#ctrl+v 粘贴输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'v')
sleep(1)
#通过回车键模拟键盘回车按键操作
driver.find_element_by_id("kw").send_keys(Keys.ENTER)


driver.quit()