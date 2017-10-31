# -*-encoding:utf-8 -*-
from appium import webdriver
import os
import time

# device='91QEBNT36F2S' #此处设备号
# pack='com.zhehe.offline' #此处是我们app的package名称
# activity='com.zhehe.offline.activity.EnterActivity'#此处是我们的app的主activity
# #下面的按照我的脚本内容填写即可，里边内容的意思也很清晰吧
# PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
# desired_caps={}
# desired_caps['device'] = 'android'
# desired_caps['platformName']='Android'
# desired_caps['browserName']=''
# desired_caps['Version']='4.4.4'
# desired_caps['deviceName']=device
# #desired_caps['app']=PATH('D:\\jr.apk')
# desired_caps['appPackage'] = pack
# desired_caps['appActivity'] = activity
# driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

#设备号
device="91QEBNT36F2S"
#包名
pack="com.zhehe.offlinemanage"
#app主activity
activity="com.zhehe.offlinemanage.activity.EnterActivity"
#虽然不知道是干嘛的，但是好像是要这样写
PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))

desired_caps={
    'device':'android',
    'platformName':'Android',
    'browserName':'',
    'Version':'4.4.4',
    'deviceName':device,
    'appPackage':pack,
    'appActivity':activity,
}
browser=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
#以上就可以打开app了，剩下的就是需要定位元素去操作咯

time.sleep(2)

browser.find_element_by_id("enter_user").clear()
browser.find_element_by_id("enter_user").send_keys("21345678903")
browser.find_element_by_id("enter_password").send_keys("a123456")
time.sleep(2)

browser.find_element_by_id("enter_confirm").click()
time.sleep(5)
browser.find_element_by_id("order_item_number").click()










browser.find_element_by_id("rb_myself").click()
browser.implicitly_wait(10)
browser.find_element_by_id("base_out").click()
time.sleep(2)
browser.quit()