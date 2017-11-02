# -*-encoding:utf-8 -*-
'''
# 判断title 方法title_is
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
print(driver.title)
title = EC.title_is("百度一下，你就知道")(driver)
print(title)
try:
    if  title != True:
        print("yes")
        pass
except Exception as e:
    print("no")
driver.quit()

# 判断文本 text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
# locator = ("name","tj_settingicon")
# text = "设置"
result = EC.text_to_be_present_in_element(("name","tj_settingicon"),u"设置")(driver)
print(result)
driver.quit()
'''
# 判断弹出框alert_is_present
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from bs4 import BeautifulSoup