# -*-encoding:utf-8 -*-
from selenium import webdriver
import unittest
from selenium.webdriver.support import expected_conditions as EC
import time
class Login(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.get("http://www.unitportal.com/web/admin/dist/login.html")
        self.browser.maximize_window()
    def tearDown(self):
        time.sleep(3)
        self.browser.find_element_by_xpath('//*[@id="userInfo"]/div/a').click()
        self.browser.quit()
    def test_login(self):
        time.sleep(2)
        '''CSS通过TYPE属性来定位'''
        self.browser.find_element_by_css_selector("[type = 'text']").send_keys("admin")
        self.browser.find_element_by_css_selector("[type = 'password' ]").send_keys("123456")
        self.browser.find_element_by_class_name("submit").click()


if __name__ == '__main__':
    unittest.main()

