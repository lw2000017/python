# -*-encoding:utf-8 -*-

from selenium import webdriver
from  time import  *
#给chromedriver一个路径
chromedriver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
browser = webdriver.Chrome(chromedriver)
#打开浏览器
browser.get("http://120.26.50.11:8088/publish/crm/login.html")



browser.implicitly_wait(10)

# #输入账号和密码
# browser.find_element_by_id("username").send_keys("admin")
# browser.implicitly_wait(10)
# browser.find_element_by_id("password").send_keys("admin123")
#
# sleep(1)
#
# #点击登录按钮
# browser.find_element_by_xpath("/html/body/div[2]/div/form/div[3]/button").click()
#
# sleep(3)
# browser.find_element_by_link_text("订单列表")
#
# sleep(2)
#
# # js="document.getElementById('filtertermstart').removeAttribute('readonly')"
# #
# # browser.execute_script(js)
#
# browser.find_element_by_id("filtertermstart").click()
# sleep(2)
#
# browser.find_element_by_xpath('//td[@onclick="day_Click(2017,6,15);"]').click()

# sleep(3)
# username=["adminn","admi","admii","admin"]
# password=["admin","admin1","admin12","admin123"]
#for name,word in username,password:
    # browser.find_element_by_id("username").send_keys(name)
    # browser.implicitly_wait(10)
    # browser.find_element_by_id("password").send_keys(word)
    # if browser.find_element_by_css_selector(".dialogok"):
    #     browser.find_element_by_css_selector(".dialogok").click()
    #print(name)
   # print(word)
# for name in username:
#     browser.find_element_by_id("username").send_keys(name)
# for word in password:
#     browser.find_element_by_id()

def login_username(username,):
    browser.implicitly_wait(10)
    browser.find_element_by_id("username").clear()
    browser.find_element_by_id("username").send_keys(zh)

def login_password(password):
    browser.implicitly_wait(10)
    browser.find_element_by_id("password").clear()
    browser.find_element_by_id("password").send_keys(mi)

def click_login():
    sleep(1)
    browser.find_element_by_css_selector(".btnlogin").click()
def panduan():
    sleep(1)
    try :
         browser.find_element_by_css_selector(".dialogok").click()
         print("错误的账号和密码"+zh + " ccuowu de miam "+mi)
    except Exception as e :
        return


# login("admin","admin123")
# browser.implicitly_wait(10)
# panduan()

zhanghao=['a2dmin',"admin","admin123","admi1n"]
mima=["admin1243","admin1","admin13","admin123"]

# for zh in zhanghao:
#     for mi in mima:
#         while zh=="admin" and mi=="admin123":
#             login(zh,mi)
#             print("登录成功")
#             continue
#         else:
#             login(zh,mi)
#             sleep(1)
#             panduan()

for zh in zhanghao:
   for mi in mima:
       if zh=="admin":
           if mi=="admin123":
               login_username(zh)
               login_password(mi)
               click_login()
               sleep(3)
               break
           else:
               login_username(zh)
               login_password(mi)
               click_login()
               panduan()

       else:
           try:
               browser.find_element_by_link_text("订单列表")
               break
           except Exception as e:
               login_username(zh)
               login_password(mi)
               click_login()
               panduan()







'''
for zh in zhanghao:
    for  mi in mima:
        if browser.find_element_by_id("username"):
            sleep(1)
            login_username(zh,mi)
            # login_password(mi)
            if zh == "admin":
                if mi == "admin123":
                    # login_username(zh)
                    # login_password(mi)
                    click_login()
                    print ("登录成功")
                    break
                else:
                    click_login()
                    sleep(1)
                    panduan()

            else:
                browser.implicitly_wait(10)
                click_login()
                sleep(1)
                panduan()
        else:
            break
'''

