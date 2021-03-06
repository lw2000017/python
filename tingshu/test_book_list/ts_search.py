# -*-encoding:utf-8 -*-
from selenium import webdriver
import unittest
import time
from selenium.webdriver.support.wait import WebDriverWait
class Search(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.get("http://www.unitportal.com/web/admin/dist/login.html")
        self.browser.maximize_window()
        time.sleep(2)
        '''CSS通过TYPE属性来定位'''
        self.browser.find_element_by_css_selector("[type = 'text']").send_keys("admin")
        self.browser.find_element_by_css_selector("[type = 'password' ]").send_keys("123456")
        self.browser.find_element_by_class_name("submit").click()

    def tearDown(self):
        time.sleep(3)
        self.browser.find_element_by_xpath('//*[@id="userInfo"]/div/a').click()
        self.browser.quit()
    def test_01(self):
        WebDriverWait(self.browser,3).until(
            lambda x: x.find_element_by_xpath('//*[@id="content"]/div[1]/div[1]/input')
        ).send_keys("海底两万里")

        # wenben = self.browser.find_element_by_xpath('//*[@id="content"]/div[1]/div[1]/input').text
        # print(wenben)

        self.browser.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/a[2]').click()
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()