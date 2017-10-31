# -*-encoding:utf-8 -*-

from selenium import webdriver
from time import *

from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from  selenium.webdriver.support.ui import Select
#browser=webdriver.Ie()
#给chromedriver一个路径
chromedriver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
browser = webdriver.Chrome(chromedriver)
sleep(1)

browser.get("http://www.baidu.com")

browser.find_element_by_id("kw").send_keys("hallo")

browser.find_element_by_id("su").click()

sleep(2)

browser.set_window_size(600,600)

sleep(2)

#js="window.wcrollTo(100,200);"
browser.execute_script("window.wcrollTo(100,200)")


'''
browser.get("http://120.26.50.11:8088/publish/crm/login.html")
browser.implicitly_wait(10)
# cookie=browser.get_cookies()
# print(cookie)
# browser.add_cookie({'name':'username','value':'admin'})
# browser.add_cookie({'name':'password','value':'admin123'})
#browser.maximize_window()

#输入账号和密码
def login():
    browser.find_element_by_id("username").send_keys("admin")
    browser.find_element_by_id("password").send_keys("admin123")
    sleep(1)

#点击登录按钮

    browser.find_element_by_xpath("/html/body/div[2]/div/form/div[3]/button").click()

    sleep(2)
#退出
def logout():
    browser.find_element_by_id("loginuserimg").click()
    sleep(1)


    browser.find_element_by_css_selector(".loginoutbtn").click()
    sleep(2)


    try:
        browser.find_element_by_xpath("/html/body/div[2]/div/div")
        print("退出成功")
    except Exception as e:
        print("退出失败")


    sleep(1)




sleep(2)
try:
    browser.get("http://120.26.50.11:8088/publish/crm/login.html")
    print("打开成功")
except Exception as e:
    print("打开失败")

login()


sleep(2)

browser.set_window_size(600,600)
sleep(2)
browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]/a").click()
#browser.implicitly_wait(10)

sleep(2)
js='window.scrollTo(100,200);'
browser.execute_script(js)

'''












# sleep(2)
#
# #browser.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[4]/div/div[1]")
# shubiao=ActionChains(browser)
# cc=browser.find_element_by_link_text("更多产品")
#
# browser.refresh()
# sleep(2)
# shubiao.move_to_element(cc)






# browser.find_element_by_id("kw").send_keys("hallo")
# browser.find_element_by_id("kw").submit()
# sleep(2)
#
# browser.find_element_by_link_text("hallo中文意思").click()
#
#
#
# #切换窗口
# windows=browser.window_handles
# browser.switch_to.window(windows[-1])
# sleep(2)
# browser.close()
# sleep(2)
# windows=browser.window_handles
# browser.switch_to.window(windows[-1])
#
# sleep(2)
# try:
#     browser.back()
#     print("返回成功")
# except Exception as e:
#     print("返回失败")
#
#
# yuansu=browser.find_element_by_id("ke")
# ActionChains(yuansu).c
#
# ActionChains(browser.find_element_by_id("ke")).context_click()








# #打开浏览器
# browser.get("http://hn.gkwlpx.com/Home/RegionHome?rgnId=411400")
# sleep(2)
# #关闭弹出的提示框
# browser.find_element_by_xpath("/html/body/div[1]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[1]/td/div/div[2]/a[4]").click()
# sleep(2)
# #输入用户名
# browser.find_element_by_id("LoginAccount").send_keys("41230119580615007X")
# sleep(1)
# #输入密码
# browser.find_element_by_id("LoginPassword").send_keys("15007X")
# sleep(1)
# #点击验证码输入框
# browser.find_element_by_id("LoginValCode").click()
# sleep(10)
# #期间手动输入验证码，然后，点击登录按钮
# browser.find_element_by_id("btnSubmit").click()
# sleep(6)
#
# # #打开我的课程
# # browser.find_element_by_id("3e23316023894b1a8b95ccc8d95531e2").click()
# # sleep(2)
# #点击继续学习
# browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/table/tbody/tr/td[2]/a").click()
#
#
#
# # jindu=browser.find_element_by_id("div_ProgressBar_value").text
# # if jindu=100%:
# #     browser.close()
# # elif:
# #     sleep(10)
# #
#
#
#
# browser.find_element_by_id("kw").send_keys(Keys.ALT,'')

























