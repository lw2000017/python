# -*-encoding:utf-8 -*-
from selenium import webdriver
import time
import OrderManager

class denglu():
    def test_denglu(self):
        chromedriver = 'C:\Python27\chromedriver.exe'
        browser = webdriver.Chrome(chromedriver)
        browser.find_element_by_id("username").clear()
        browser.find_element_by_id("username").send_keys("admin")
        browser.find_element_by_id("password").clear()
        browser.find_element_by_id("password").send_keys("admin123")
        time.sleep(1)
        browser.find_element_by_css_selector(".btnlogin").click()
        time.sleep(2)