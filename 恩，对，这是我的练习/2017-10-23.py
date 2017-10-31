# -*-encoding:utf-8 -*-
from selenium import webdriver
import time
browser=webdriver.Chrome()
browser.get("https://www.baidu.com")
print(browser.get_cookies())
time.sleep(2)
browser.find_element_by_link_text("登录").click()
time.sleep(2)
browser.find_element_by_name("userName").clear()
browser.find_element_by_name("userName").send_keys("15836889160")
browser.find_element_by_name("password").send_keys("lw200017")
time.sleep(10)

browser.find_element_by_id("TANGRAM__PSP_10__submit").click()
time.sleep(2)
print(browser.get_cookies())












time.sleep(2)
browser.quit()
# BIDUPSID=ED7444F79D41D9A90CF2512B15DA35A7; PSTM=1505274091; MCITY=-179%3A; BAIDUID=ED7444F79D41D9A90CF2512B15DA35A7:SL=0:NR=20:FG=1; plus_cv=1::m:21732389; FP_UID=ac2d110fe294b150839379cf78d7eee3; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BD_CK_SAM=1; PSINO=1; BDUSS=2F4MH5rSW5OWDlESGg0bnFnSHZobldFU2pBWHBtUHc4YldUVDlEU1A3N2tRQlZhSVFBQUFBJCQAAAAAAAAAAAEAAAAa33QswuTU2rXYx~K1xNDHs70AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOSz7Vnks-1ZN; BD_HOME=1; H_PS_PSSID=1448_13549_21090_17001_24331_24022_20928; BD_UPN=12314753; sug=3; sugstore=1; ORIGIN=0; bdime=0