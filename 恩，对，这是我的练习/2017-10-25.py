# -*-encoding:utf-8 -*-


"""
# 一.登录方法封装
# 1.把登录携程一个登录类，里面写个登录的方法
class login():
    '''封装一个登录'''
    def __init__(self,browser):
        browser = webdriver.Chrome()
        self.browser=browser
    def int_username(self,username):
        '''输入账号'''
        self.browser.find_element_by_id("username").clear()
        self.browser.find_element_by_id("username").send_keys(username)
    def int_password(self,password):
        '''输入密码'''
        self.browser.find_element_by_id("password").clear()
        self.browser.find_element_by_id("password").send_keys(password)
    def click_button(self):
        '''点击登录按钮'''
        self.browser.find_element_by_id("button").click()
    def login(self,username,password):
        '''登录方法'''
        self.int_username(username)
        self.int_password(password)


# 2.调用公共登录方法
from selenium import webdriver
import unittest

login_url= "https://www.xxx.com"
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.browser= webdriver.Chrome()
        self.browser.get(login_url)
    def tearDown(self):
        self.browser.quit()
    def test_login(self):
        # 调用登录类里面的login方法
        
if __name__ == '__main__':
    unittest.main()
"""

"""
# 异常处理，并且截图
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException

broweser = webdriver.Chrome()
broweser.get("https://www.baidu.com")
time.sleep(2)
try:
    # 查找该元素，现在的id是错误的，所以查到不到该元素，然后会抛出异常
    broweser.find_element_by_id("kww")
except NoSuchElementException as msg:
    # 打印抛出的异常的错误代码，可避免因为错误而执行不下去
    print("查找元素异常%s"%msg)
    # 返回一个现在时间
    nowTime =time.strftime("%Y%m%d.%H.%M.%S")
    # 保存当前页面截图，并把该截图放在一个文件夹下（不输入文件夹，默认放在文件目录下），并且文件命名为当前时间
    t = broweser.get_screenshot_as_file("E:\\%s.jpg"%nowTime)
    # 打印是否保存截图，成功保存返回True，若失败则返回False
    print("截图结果是：%s"%t)
broweser.quit()
"""

'''
from selenium import webdriver
import unittest,time
from selenium.webdriver.support import expected_conditions as EC


class Login(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.get("https://passport.cnblogs.com/user/signin")
        time.sleep(2)
    def tearDown(self):
        self.browser.quit()
    def test_login(self):

        try:
            self.browser.find_element_by_id("input1").clear()
            self.browser.find_element_by_id("input1").send_keys("lw200017")
            self.browser.find_element_by_id("input2").clear()
            self.browser.find_element_by_id("input2").send_keys("lw200017..++--")
            self.browser.find_element_by_id("signin").click()
            time.sleep(2)
            locator = ("id","lnk_current_user")
            result = EC.text_to_be_present_in_element(locator,"hallo,MR.智障")(self.browser)
            self.assertFalse(result)
        except Exception as msg:
            print("异常原因为：%s"%msg)
            raise
if __name__ == '__main__':
    unittest.main()
'''


# 判断元素是否消失
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
browser = webdriver.Chrome()
browser.get("https://www.baidu.com")
WebDriverWait(browser,10).until(lambda x:x.find_element_by_id("kw")).send_keys("selenium")
try:
    is_disappeared = WebDriverWait(browser,10,1).until_not(lambda x:x.find_element_by_id("kw").is_displayed(),message="没有消失掉")
    print(is_disappeared)
except TimeoutException as msg:
    print("%s"%msg)
browser.quit()


