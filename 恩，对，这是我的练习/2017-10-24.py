# -*-encoding:utf-8 -*-
'''
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_01(self):
        result = 6 - 5
        hope = 2
        self.assertEqual(result,hope,msg="shibai")
    def test_02(self):
        result_01 = 6 / 5
        hope_01 = 1.2
        self.assertEqual(result_01,hope_01)
if __name__ == '__main__':
    unittest.main()



from selenium import webdriver
import unittest
import time
class Test_0001(unittest.TestCase):
    # @classmethod           #必须使用@classmethod装饰器，所有case运行前只运行一次（作用和setUp一样，只不过setUp有多少case运行多少次)
    # def setUpClass(cls):
    #     cls.browser = webdriver.Chrome()
    #     cls.browser.get("https://www.baidu.com")
    #     time.sleep(1)
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.get("http://www.baidu.com")
        time.sleep(1)
    def tearDown(self):
        self.browser.quit()
    def test_01(self):
        self.browser.find_element_by_id("kw").send_keys("hallo")
        time.sleep(1)
    def test_02(self):
        self.browser.find_element_by_id("kw").clear()
        self.browser.find_element_by_id("kw").send_keys("hallo1")
        time.sleep(1)
    # @classmethod
    # def tearDownClass(cls):
    #     cls.browser.quit()
if __name__ == '__main__':
    unittest.main()
'''
#断言

import unittest
class Test(unittest.TestCase):
    def test_01(self):
        '''判断a==b'''
        a = 1
        b = 1
        self.assertEqual(a,b)
    def test_02(self):
        '''判断 a in b'''
        a = "hello"
        b = "hello world!"
        self.assertIn(a,b)
    def test_03(self):
        '''判断 a is True'''
        a = True
        self.assertTrue(a)
    def test_04(self):
        '''失败案例'''
        a = "hallo"
        b = "hello"
        self.assertEqual(a,b,msg="失败原因：%s != %s"%(a,b))
if __name__ == '__main__':
    unittest.main()
