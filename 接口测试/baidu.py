# -*-encoding:utf-8 -*-
# import HTMLTestRunner
from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import NoSuchAttributeException
import unittest,time

class Baidu(unittest.TestCase):
    def setUp(self):
        self.browser=webdriver.Chrome()
        self.browser.implicitly_wait(10)
        self.base_url="http://www.baidu.com"
        self.verificationErrors=[]#脚本运行时，错误信息将被打印到这个列表中
        self.accept_next_alert=True#是否继续接受一下警告
    def test_baidu_search(self):
        u'''百度搜索'''
        browser=self.browser
        browser.get(self.base_url+'/')
        browser.find_element_by_id("kw").send_keys("selenium webdriver")
        browser.find_element_by_id("su").click()
        time.sleep(2)
        browser.close()

    def test_baidu_set(self):
        u"""百度设置"""
        browser = self.browser
        # 进入搜索设置页
        browser.get(self.base_url + '/gaoji/preferences.html')
        # 设置每页搜索结果为 20 条
        m = browser.find_element_by_name("NR")
        m.find_element_by_xpath("//option[@value='20']").click()
        time.sleep(2)
        # 保存设置的信息
        browser.find_element_by_xpath("/html/body/form/div/input").click()
        time.sleep(2)
        #弹窗，并且同意
        browser.switch_to_alert().accept()
        time.sleep(2)

    def tearDown(self):
        self.browser.quit()
        self.assertEqual([], self.verificationErrors)#查前面的verificationErrors的列表是否为空。不为空，输入列表中的报错信息


if __name__ == "__main__":
    unittest.main()