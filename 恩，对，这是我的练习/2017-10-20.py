# -*-encoding:utf-8 -*-
from selenium import webdriver
import time

browser=webdriver.Chrome()
browser.get("http://www.baidu.com")
# 设置浏览器窗口大小
browser.set_window_size(960,240)
# 截取屏幕，并把截取的屏幕放在一个文件路径下
browser.get_screenshot_as_file("E:/1.png")
# 获取当前页面句柄（切换窗口使用）
h = browser.current_window_handle
print(h)

# 获取百度页面的所有句柄
all_h = browser.find_elements_by_css_selector(".mnav")
# 点击打开第一个按钮
all_h[0].click()

s = browser.window_handles
print(s)
time.sleep(2)
# 返回上一个页面
browser.back()
time.sleep(2)
# 从上一个页面返回到当前页面
# browser.forward()

# 打印href标签
url = browser.find_elements_by_css_selector(".mnav")
for i in url:
    print(i.get_attribute("href"))

















#关闭当前窗口
# browser.close()
time.sleep(2)
#关闭浏览器
browser.quit()