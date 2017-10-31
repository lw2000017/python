 # -*-encoding:utf-8 -*-

from selenium import webdriver
from  time import  *



#给chromedriver一个路径
chromedriver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
browser = webdriver.Chrome(chromedriver)
#打开浏览器
browser.get("http://m.zjsdxf.cn:9003/admin/index.html")



browser.find_element_by_xpath("/html/body/div/div[1]/p[2]").click()
sleep(1)

browser.find_element_by_xpath("/html/body/div/div[2]/form/div[1]/input").send_keys("huashu_001")
browser.implicitly_wait(10)

browser.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/input").send_keys("123456")
browser.implicitly_wait(10)



browser.find_element_by_xpath("/html/body/div/div[2]/form/button").click()
sleep(2)


browser.find_element_by_xpath("/html/body/div[2]/ul/li[3]").click()
browser.implicitly_wait(10)

# for:
#     try:
#         browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/div/div/div[1]/h4").click()
#     except Exception as e:
#         browser.find_element_by_xpath("/html/body/div[3]/div[2]/table/tbody/tr[1]/td[3]/a").click()
#
#
# if browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/div/div/div[1]/h4").click():





















