# -*-encoding:utf-8 -*-
from selenium import webdriver
from time import *

#用firefox浏览器，创建一个profile
#geckodriver='C:\LenovoDrivers\geckodriver.exe'
#profileDir=r"C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\85j7ru4z.s2"
#profile1=webdriver.FirefoxProfile(profileDir)

chromedrirver='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'


browser=webdriver.Chrome(chromedrirver)
browser.implicitly_wait(10)


#browser=webdriver.Firefox()
# browser.maximize_window()

#拖动滚动条
'''
browser.get("https://tieba.baidu.com/index.html")
sleep(2)
name=browser.find_element_by_link_text("地区")
browser.execute_script("return arguments[0].scrollIntoView();",name)

browser.implicitly_wait(10)

browser.find_element_by_link_text("河南").click()
'''
#alert弹窗
'''
browser.get("http://www.baidu.com")
browser.implicitly_wait(10)
browser.execute_script("window.alert('这是一个弹框');")
'''
#保存当前页面全部图片信息
'''
browser.get("http://news.baidu.com")
browser.implicitly_wait(10)
for image in browser.find_elements_by_tag_name("img"):
    print(image.text)
    print(image.size)
    print(image.tag_name)
'''
#获取页面元素的属性
'''
browser.get("http://www.baidu.com")
browser.implicitly_wait(10)
for link in browser.find_elements_by_xpath("//*[@id]"):
    print(link.get_attribute('id'))
'''
