# -*-encoding:utf-8 -*-
from selenium import webdriver
import time
import unittest

class login(unittest.TestCase):
    def setUp(self):
        chromedriver = 'C:\Python27\chromedriver.exe'
        self.browser = webdriver.Chrome(chromedriver)
        self.browser.get("http://server.jiagj.com/publish/crm/login.html")
        print("\nstart")

    def test_login(self):
        browser=self.browser
        time.sleep(2)
        browser.find_element_by_id("username").clear()
        browser.find_element_by_id("username").send_keys("admin")
        browser.find_element_by_id("password").clear()
        browser.find_element_by_id("password").send_keys("admin123")
        time.sleep(1)
        browser.find_element_by_css_selector(".btnlogin").click()
        time.sleep(2)
    def test_dingdan(self):
        login.test_login(self)
        browser=self.browser
        browser.maximize_window()
        time.sleep(2)
        browser.find_element_by_id("managerPower").click()
        time.sleep(2)
        browser.find_element_by_link_text(u"订单列表").click()
        browser.implicitly_wait(10)
        browser.find_element_by_xpath('//*[@id="manager"]/div[3]/div[1]/div[4]/div[1]/div[4]/input').send_keys("17638416138")
        browser.implicitly_wait(10)
        browser.find_element_by_css_selector(".search").click()
        time.sleep(2)
        leng=browser.find_elements_by_class_name("tableth tableWidthDeal2")
        browser

    def test_logout(self):
        login.test_login(self)
        browser=self.browser
        browser.maximize_window()
        time.sleep(2)
        browser.find_element_by_id("loginuserimg").click()
        time.sleep(1)
        browser.find_element_by_id("loginquit").click()
        time.sleep(2)
    def tearDown(self):
        print "End"
        self.browser.quit()

if __name__ == '__main__':
    unittest.main()