# -*-encoding:utf-8 -*-
from selenium import webdriver
import unittest
import time
class Login(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.get("http://www.unitportal.com/web/admin/dist/login.html")
        self.browser.maximize_window()
    def tearDown(self):
        self.browser.implicitly_wait(10)
        # self.browser.find_element_by_xpath('//*[@id="userInfo"]/div/a').click()
        self.browser.quit()
    def test_login_1(self):
        time.sleep(2)
        # self.browser.find_element_by_xpath('//*[@id="login"]/form/div[1]/p/input').send_keys("admin")
        # self.browser.find_element_by_xpath('//*[@id="login"]/form/div[2]/p/input').send_keys("123456")
        '''CSS通过TYPE属性来定位'''
        self.browser.find_element_by_css_selector("[type = 'text']").send_keys("admin")
        self.browser.find_element_by_css_selector("[type = 'password' ]").send_keys("123456")
        '''点击记住密码复选框'''
        self.browser.find_element_by_css_selector("[type = 'checkbox']").click()
        self.browser.find_element_by_class_name("submit").click()
    def test_login_2(self):
        self.test_login_1()
        time.sleep(2)
        self.browser.find_element_by_xpath('//*[@id="userInfo"]/div/a').click()
        self.browser.implicitly_wait(10)
        self.browser.find_element_by_class_name("submit").click()
        time.sleep(2)
        '''点击退出按钮成功，则记住了密码，否则，没有记住'''
        Button = self.browser.find_element_by_xpath('//*[@id="userInfo"]/div/a').text
        if Button == "退出登录" :
            print("记住账号密码成功")
        else:
            print("记住账号密码失败")


            # username = self.browser.find_element_by_css_selector("[type = 'text']").text()
        # if username == "admin":
        #     print("记住账号成功")
        #     print(username)
        # else:
        #     print("没有记住密码")
        # password = self.browser.find_element_by_css_selector("[type = 'password']").text()
        # print(password)

if __name__ == '__main__':
    unittest.main()

