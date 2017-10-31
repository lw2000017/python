# -*-encoding:utf-8 -*-

import unittest
from selenium import webdriver
import time



class shuru(unittest.TestCase):
    def setUp(self):
        chromedriver = "C:\Python27\chromedriver.exe"
        self.browser = webdriver.Chrome(chromedriver)
        self.browser.get("http://www.baidu.com")
        time.sleep(2)
    def test_login1(self):
        browser=self.browser
        browser.find_element_by_id("kw").send_keys("hallo")
        time.sleep(1)
        browser.find_element_by_id("su").click()
        test=browser.find_element_by_link_text(u"英文结果").get_attribute("target")
        assert test=="_self"
        print(test)
    def test_login2(self):
        browser=self.browser
        browser.find_element_by_id("kw").send_keys("hallo")
        browser.implicitly_wait(10)
        browser.find_element_by_id("su").click()
        test1=browser.find_element_by_link_text(u"西汉高速重大事故").get_attribute("title")
        assert test1==u"西汉高速重大事故"
        print(test1)


    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main()