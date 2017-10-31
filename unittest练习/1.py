# -*-coding:utf8-*-
from appium import webdriver
import os
from time import sleep


device='91QEBNT36F2S' #此处设备号
pack='com.ss.android.article.news' #此处是我们app的package名称
activity='com.ss.android.article.news.activity.SplashActivity'#此处是我们的app的主activity
#下面的按照我的脚本内容填写即可，里边内容的意思也很清晰吧
PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
desired_caps={}
desired_caps['device'] = 'android'
desired_caps['platformName']='Android'
desired_caps['browserName']=''
desired_caps['Version']='4.4.4'
desired_caps['deviceName']=device
#desired_caps['app']=PATH('D:\\jr.apk')
desired_caps['appPackage'] = pack
desired_caps['appActivity'] = activity
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(10)
'''
while 1:
    if driver.current_activity=='.activity.MainActivity':
        break
els=driver.find_elements_by_id('amb')
news_t1=els[1].text
print 'news1_title:',news_t1
els=driver.find_elements_by_id('amb')
els[2].click()
while 1:
    els=driver.find_elements_by_id('el')
    news_t2=els[0].text
    print 'news2_title:',news_t2
    if news_t2!=news_t1:
        break
driver.find_element_by_id('ab0').click()
while 1:
    if driver.current_activity=='com.ss.android.article.base.feature.search.SearchActivity':
        break
driver.find_element_by_id('ll').send_keys('lamecho')
driver.find_element_by_id('o9').click()
sleep(10)

driver.quit()

'''

driver.find_element_by_id('amg').click()
while 1:
    if driver.current_activity=='com.ss.android.article.base.feature.search.SearchActivity':
        break
driver.find_element_by_id('pk').send_keys(u'你好')
#driver.find_element_by_class_name("EditText").send_keys("lamecho")
sleep(3)
driver.find_element_by_id('sk').click()

print driver.current_activity

driver.implicitly_wait(10)
driver.find_element_by_id("sj").click()
driver.implicitly_wait(10)
if  driver.find_element_by_id("amg"):
    w=driver.get_window_size()['width']
    h=driver.get_window_size()['height']
    driver.swipe(int(w*0.25),int(h*0.5),int(w*0.75),int(h*0.5),1000)
    print u"左滑成功"
    sleep(2)
    driver.swipe(int(w*0.5),int(h*0.75),int(w*0.5),int(h*0.25) ,1000)
    print u"上滑成功"

else:
    print u"再次等待"

driver.quit()