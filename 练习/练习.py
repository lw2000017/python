# -*-encoding:utf-8 -*-

from selenium import webdriver
import time

chromedriver='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
browser=webdriver.Chrome(chromedriver)
browser.get("http://www.baidu.com")

time.sleep(2)

browser.find_element_by_id("kw").send_keys("long")
time.sleep(1)
ac=browser.find_element_by_id("kw").text
print(len(ac))
