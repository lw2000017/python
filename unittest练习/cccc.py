# -*-coding:utf8-*-
import  unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys



class ceshi(unittest.TestCase):
    def setUp(self):
        chromedriver = "c:\Python27\chromedriver.exe"
        self.browser = webdriver.Chrome(chromedriver)
        self.browser.get("https://www.jd.com")
        print "Start"
    def test_01(self):
        browser=self.browser
        browser.implicitly_wait(20)
        browser.find_element_by_id("key").send_keys("")