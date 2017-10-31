# -*-encoding:utf-8 -*-

from selenium import webdriver
from  time import  *
from  selenium.webdriver.support.ui import Select
from  selenium.webdriver.common.keys import Keys

#给chromedriver一个路径
chromedriver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
browser = webdriver.Chrome(chromedriver)
#打开浏览器
browser.get("http://120.26.50.11:8088/publish/crm/login.html")



browser.implicitly_wait(10)

#输入账号和密码
browser.find_element_by_id("username").send_keys("admin")

browser.find_element_by_id("password").send_keys("admin123")

sleep(1)

#点击登录按钮
browser.find_element_by_xpath("/html/body/div[2]/div/form/div[3]/button").click()


browser.maximize_window()

sleep(2)





#打开管家部管理
browser.find_element_by_id("managerPower").click()
browser.implicitly_wait(10)

#打开订单列表
browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div[1]/div[1]").click()
sleep(2)

browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div[1]/div[1]").click()
sleep(2)


browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]/a").click()
sleep(2)

#输入订单时间
browser.find_element_by_id("filtertermstart").clear()
browser.find_element_by_id("filtertermstart").send_keys("2017-05-24")
browser.implicitly_wait(10)

browser.find_element_by_id("filtertermend").clear()
browser.find_element_by_id("filtertermend").send_keys("2017-05-27")
browser.implicitly_wait(10)
browser.find_element_by_css_selector(".search").click()

# #选择订单时间？
# browser.find_element_by_id("filtertermstart").click()
# browser.implicitly_wait(10)
# browser.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[6]/td[4]").click()
# sleep(2)
#
# browser.find_element_by_id("filtertermend").click()
# sleep(2)
# browser.find_element_by_css_selector("html body div.WdateDiv div table.WdayTable tbody tr td.WotherDay").click()




#输入订单编号
browser.find_element_by_css_selector("[data-bind='value:ordercode']").send_keys("OW20170525391864")
browser.implicitly_wait(10)
browser.find_element_by_css_selector(".search").click()

browser.implicitly_wait(10)

#输入业主姓名
browser.find_element_by_css_selector("[data-bind='value:username']").send_keys("测试")
browser.implicitly_wait(10)
browser.find_element_by_css_selector(".search").click()

browser.implicitly_wait(10)
#输入管家姓名
browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/div[4]/div[1]/div[4]/input").send_keys("线下管家1")
browser.implicitly_wait(10)
browser.find_element_by_css_selector(".search").click()

browser.implicitly_wait(10)
#选择当前阶段，产品名称选择‘测试1’
select= Select(browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/div[4]/div[3]/div[1]/select[1]"))
select.select_by_visible_text("测试1")

browser.implicitly_wait(10)
#选择当前阶段，上一级产品的产品节点
select=Select(browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/div[4]/div[3]/div[1]/select[2]"))
select.select_by_visible_text("测试节点1")

browser.implicitly_wait(10)
# #选择当前阶段
# browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/div[4]/div[3]/div[1]/select[1]").click()#点击产品名称下拉框
# browser.implicitly_wait(10)
#
# browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/div[4]/div[3]/div[1]/select[1]/option[9]").click()#选择产品名称
#
# sleep(1)
# #选择产品节点名称，现在有问题
# browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/div[4]/div[3]/div[1]/select[2]").click()#点击产品节点下拉框


#选择订单状态
browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/div[4]/div[3]/div[2]/select").click
browser.implicitly_wait(10)
browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/div[4]/div[3]/div[2]/select/option[4]").click()#选择已付款已派单订单
browser.implicitly_wait(10)
browser.find_element_by_css_selector(".search").click()

browser.implicitly_wait(10)
#选择用户类型
browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/div[4]/div[3]/div[3]/select").click()
browser.implicitly_wait(10)
browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/div[4]/div[3]/div[3]/select/option[3]").click()#选择意向用户
browser.implicitly_wait(10)
browser.find_element_by_css_selector(".search").click()

browser.implicitly_wait(10)
#选择订单来源
browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/div[4]/div[3]/div[4]/select").click()
browser.implicitly_wait(10)
browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/div[4]/div[3]/div[4]/select/option[2]").click()#选择微信
browser.implicitly_wait(10)
browser.find_element_by_css_selector(".search").click()

browser.implicitly_wait(10)
#选择地址
browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/div[4]/div[5]/select[1]").click()
browser.implicitly_wait(10)
browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/div[4]/div[5]/select[1]/option[3]").click()#选择浙江省
browser.implicitly_wait(10)
browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/div[4]/div[5]/select[2]").click()
browser.implicitly_wait(10)
browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/div[4]/div[5]/select[2]/option[2]").click()#选择杭州市
browser.implicitly_wait(10)
browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/div[4]/div[5]/select[3]").click()
browser.implicitly_wait(10)
browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/div[4]/div[5]/select[3]/option[9]").click()#选择余杭区
browser.implicitly_wait(10)
browser.find_element_by_css_selector(".inputaddress").send_keys("梦想小镇")
browser.implicitly_wait(10)
browser.find_element_by_css_selector(".search").click()


#界面刷新
#browser.find_element_by_css_selector(".search").send_keys(Keys.F5)

try:
    browser.refresh()
    print("chenggong")
except Exception as e:
    print("shibai")




#选择每页显示数
select =Select(browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div[4]/div[3]/select"))
select.select_by_visible_text("20")#每页显示20条
browser.implicitly_wait(10)
browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div[4]/div[8]").click()#点击确定按钮
sleep(2)
#点击 上一页和下一页
browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div[4]/div[5]").click()#点击上一页
browser.implicitly_wait(10)
browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div[4]/div[6]").click()#点击下一页
browser.implicitly_wait(10)


#手动输入页面
browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div[4]/div[7]/input").clear()
browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div[4]/div[7]/input").send_keys("5")#手动输入5
browser.implicitly_wait(10)
browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div[4]/div[8]").click()
















browser.find_element_by_css_selector(".userimg").click()
sleep(2)

browser.find_element_by_css_selector(".loginoutbtn").click()
sleep(1)







browser.quit()