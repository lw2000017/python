# -*-encoding:utf-8 -*-
'''
from selenium import webdriver
import time

browser=webdriver.Chrome()
browser.get("http://server.jiagj.com/publish/crm/login.html")
browser.maximize_window()
browser.implicitly_wait(10)
browser.find_element_by_id("username").send_keys("admin")
browser.find_element_by_id("password").send_keys("admin123")
browser.find_element_by_css_selector(".btnlogin").click()

time.sleep(5)
browser.implicitly_wait(10)
browser.find_element_by_id("managerPower").click()
browser.find_element_by_link_text("订单列表").click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="manager"]/div[3]/div[1]/div[4]/div[1]/div[4]/input').send_keys("15836889160")
browser.find_element_by_css_selector(".search").click()
time.sleep(2)

# # contains定位方法，可定位关键字
# ll = browser.find_elements_by_xpath('//*/div[contains(@class,"tableth tableWidthDeal")]')
# for ll in ll :
#     ll = ll.text
#     print(ll)
tests = browser.find_elements_by_xpath('//div[contains(@class,"tableth tableWidthDeal1")]')
for test in tests:
    tests = test.text
    print(tests)
browser.quit()



from selenium import webdriver
import unittest,time
from selenium.webdriver.support.wait import WebDriverWait
class T(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.get("https://www.baidu.com")
        WebDriverWait(self.browser,10).until(lambda x:x.find_element_by_link_text("登录"),message="没有找到").click()
    def tearDown(self):
        self.browser.quit()
    def login(self):
        time.sleep(3)
        try:
            self.browser.find_element_by_id("input").send_keys("asasasa")
        except Exception as e:
            print("meiyou zhaodao")
    # def test_01(self):
    #     self.login()
    #     self.is_login_sucess()


if __name__ == '__main__':
    unittest.main()


import xlrd

data = xlrd.open_workbook("E:\\111.xlsx")   #获取文件路径
table = data.sheet_by_name('Sheet1')  # 通过名称获取
nrows = table.nrows  # 获取总行数
ncols = table.ncols  # 获取总列数

# 获取一行或一列的值，参数是第几行
print(table.row_values(2))  # 获取第一行的值
print(table.col_values(0))  # 获取第一列的值


# 封装读取方法
import xlrd
class ExcelUtil():
    def __init__(self,excelPath,sheetName):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols
    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j = 1
            for i in range(self.rowNum-1):
                s = {}
                # 从第二行取对应values值
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
            return r
if __name__ == '__main__':
    filePath = "e:\\111.xlsx"
    sheetName = "Sheet1"
    data = ExcelUtil(filePath,sheetName)
    print(data.dict_data())
'''

import ddt
import unittest

test_data=[{
    "username":"test_01",
    "password":"test_psw_01"
},
    {
        "username":"test_02",
        "password":"test_psw_02"
    },
    {
        "username":"test_03",
        "password":"test_psw_03"
    }]

@ddt.ddt
class test(unittest.TestCase):
    def setUp(self):
        print("start")
    def tearDown(self):
        print("end")
    @ddt.data(*test_data)
    def test_ddt(self,data):
        print(data)
if __name__ == '__main__':
    unittest.main()



