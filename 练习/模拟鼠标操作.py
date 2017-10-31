# -*-encoding:utf-8 -*-
#调用类
from time import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
chromedriver='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
driver=webdriver.Chrome(chromedriver)
driver.get("http://pan.baidu.com")
sleep(2)
#点击账号密码登陆
driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[6]/div/div[6]/div[2]/a").click()
sleep(2)
#输入账号的密码
driver.find_element_by_id("TANGRAM__PSP_4__userName").clear()
driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("15836889160")
sleep(1)
driver.find_element_by_id("TANGRAM__PSP_4__password").clear()
driver.find_element_by_id("TANGRAM__PSP_4__password").send_keys("lw200017")
driver.find_element_by_id("TANGRAM__PSP_4__password").submit()

sleep(2)
#选择一个元素，鼠标右键点击（利用css定位）
right_click=driver.find_element_by_css_selector("[title='《白L原》2017.HD1080P同步TV']")
ActionChains(driver).context_click(right_click).perform()


driver.quit()