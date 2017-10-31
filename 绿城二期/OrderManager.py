# -*-encoding:utf-8 -*-
from  selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
import unittest

class yingyun(unittest.TestCase):
    def setUp(self):
        chromedriver='C:\Python27\chromedriver.exe'
        self.browser=webdriver.Chrome(chromedriver)
        self.browser.get("http://server.jiagj.com/publish/crm/login.html")
        print "\nStart"

    def test_login(self):
        browser = self.browser
        time.sleep(2)
        browser.find_element_by_id("username").clear()
        browser.find_element_by_id("username").send_keys("admin")
        browser.find_element_by_id("password").clear()
        browser.find_element_by_id("password").send_keys("admin123")
        time.sleep(1)
        browser.find_element_by_css_selector(".btnlogin").click()
        time.sleep(2)
    def test_ddlb_tjsx(self):#订单列表_条件筛选
        yingyun.test_login(self)
        browser=self.browser
        browser.maximize_window()
        browser.find_element_by_id("managerPower").click()
        browser.implicitly_wait(10)
        browser.find_element_by_link_text(u"订单列表").click()
        browser.implicitly_wait(10)
        browser.find_element_by_id("filtertermstart").clear()
        browser.find_element_by_id('filtertermstart').send_keys("2017-07-30")
        browser.find_element_by_id("filtertermend").clear()
        browser.find_element_by_id("filtertermend").send_keys("2017-08-29")#下单时间
        browser.find_element_by_xpath('//input[@data-bind="value:link"]').send_keys("OT20170829312919")#订单主编号
        browser.find_element_by_xpath('//input[@data-bind="value:username"]').send_keys(u"lw测试")#业主姓名
        browser.find_element_by_xpath('//input[@data-bind="value:phone"]').send_keys('17638416138')  # 业主姓名



    def tearDown(self):
        print "End"
        self.browser.quit()

if __name__ == '__main__':
    unittest.main()