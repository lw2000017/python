# -*-encoding:utf-8 -*-
from selenium import webdriver
import unittest
from selenium.webdriver.support.wait import WebDriverWait
import time

class Login(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.get("http://www.unitportal.com/web/admin/dist/login.html")
        self.browser.maximize_window()
    def tearDown(self):
        time.sleep(3)
        # self.browser.find_element_by_xpath('//*[@id="userInfo"]/div/a').click()
        self.browser.quit()
    def test_login(self):
        self.browser.implicitly_wait(10)
        # self.browser.find_element_by_xpath('//*[@id="login"]/form/div[1]/p/input').send_keys("admin")
        # self.browser.find_element_by_xpath('//*[@id="login"]/form/div[2]/p/input').send_keys("123456")
        '''CSS通过TYPE属性来定位'''
        # self.browser.find_element_by_css_selector("[type = 'text']").send_keys("admin")
        # self.browser.find_element_by_css_selector("[type = 'password' ]").send_keys("123456")
        # self.browser.find_element_by_class_name("submit").click()
        self.browser.find_element_by_class_name("rt").click()
        WebDriverWait(self.browser,3,poll_frequency=0.1).until(lambda x:x.find_element_by_class_name("layui-layer-title"))
        note = self.browser.find_element_by_class_name("layui-layer-content").text
        if note == "密码重置，请联系管理员（17858649371）" :
            print("提示信息正确！")
            self.browser.find_element_by_class_name("layui-layer-btn0").click()
        else:
            print("提示信息不正确")




if __name__ == '__main__':
    unittest.main()

