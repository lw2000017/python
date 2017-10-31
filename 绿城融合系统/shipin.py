# -*-encoding:utf-8 -*-

from selenium import webdriver
from  time import  *
from  selenium.webdriver.support.ui import Select


#给chromedriver一个路径
chromedriver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
browser = webdriver.Chrome(chromedriver)
#打开浏览器
browser.maximize_window()


browser.get("http://hn.gkwlpx.com/Home/RegionHome?rgnId=411400")
browser.implicitly_wait(10)


#browser.find_element_by_xpath("/html/body/div[1]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[1]/td/div/div[2]/a[4]").click()
browser.implicitly_wait(10)


browser.find_element_by_id("LoginAccount").send_keys("41230119580615007X")
sleep(2)
browser.find_element_by_id("LoginPassword").send_keys("15007X")
sleep(2)

browser.find_element_by_id("LoginValCode").click()
sleep(10)

browser.find_element_by_id("btnSubmit").click()

sleep(5)

'''
#职业能力1
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/div[3]/div/div/table/tbody/tr[3]/td[4]/a").click()
sleep(5)


#browser.find_element_by_css_selector("object[type='application/x-shockwave-flash]").click()


# sleep(400)
# browser.refresh()
#
#
# sleep(400)
# browser.refresh()
#
# sleep(400)
# browser.refresh()
#
# sleep(400)
# browser.refresh()
#
# sleep(400)
# browser.refresh()
#
# sleep(400)
# browser.refresh()
#
# sleep(400)
# browser.close()
# sleep(5)

#第6讲
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[6]/td[4]/a").click()
sleep(5)


windows=browser.window_handles
browser.switch_to.window(windows[-1])
sleep(2400)

browser.close()
sleep(5)
#第7讲
windows1=browser.window_handles
browser.switch_to.window(windows1[-1])
sleep(5)
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[7]/td[4]/a").click()


windows=browser.window_handles
browser.switch_to.window(windows[-1])
sleep(2400)

browser.close()
sleep(5)


#第8讲
windows1=browser.window_handles
browser.switch_to.window(windows1[-1])
sleep(5)
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[8]/td[4]/a").click()


windows=browser.window_handles
browser.switch_to.window(windows[-1])
sleep(2400)

browser.close()
sleep(5)


#第9讲
windows1=browser.window_handles
browser.switch_to.window(windows1[-1])
sleep(5)
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[9]/td[4]/a").click()


windows=browser.window_handles
browser.switch_to.window(windows[-1])
sleep(2400)

browser.close()
sleep(5)


#第10讲
windows1=browser.window_handles
browser.switch_to.window(windows1[-1])
sleep(5)
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[10]/td[4]/a").click()


windows=browser.window_handles
browser.switch_to.window(windows[-1])
sleep(2400)

browser.close()
sleep(5)

#第11讲
windows1=browser.window_handles
browser.switch_to.window(windows1[-1])
sleep(5)
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[11]/td[4]/a").click()


windows=browser.window_handles
browser.switch_to.window(windows[-1])
sleep(2400)

browser.close()
sleep(5)

#第12讲
windows1=browser.window_handles
browser.switch_to.window(windows1[-1])
sleep(5)
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[12]/td[4]/a").click()


windows=browser.window_handles
browser.switch_to.window(windows[-1])
sleep(2400)

browser.close()
sleep(5)


#第13讲
windows1=browser.window_handles
browser.switch_to.window(windows1[-1])
sleep(5)
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[13]/td[4]/a").click()


windows=browser.window_handles
browser.switch_to.window(windows[-1])
sleep(2400)

browser.close()
sleep(5)

#第14讲
windows1=browser.window_handles
browser.switch_to.window(windows1[-1])
sleep(5)
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[14]/td[4]/a").click()


windows=browser.window_handles
browser.switch_to.window(windows[-1])
sleep(2400)

browser.close()
sleep(5)

#第15讲
windows1=browser.window_handles
browser.switch_to.window(windows1[-1])
sleep(5)
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[15]/td[4]/a").click()


windows=browser.window_handles
browser.switch_to.window(windows[-1])
sleep(2400)

browser.close()
sleep(5)


#第16讲
windows1=browser.window_handles
browser.switch_to.window(windows1[-1])
sleep(5)
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[16]/td[4]/a").click()


windows=browser.window_handles
browser.switch_to.window(windows[-1])
sleep(2400)

browser.close()
sleep(5)


#第17讲
windows1=browser.window_handles
browser.switch_to.window(windows1[-1])
sleep(5)
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[17]/td[4]/a").click()


windows=browser.window_handles
browser.switch_to.window(windows[-1])
sleep(2400)

browser.close()
sleep(5)

#第18讲
windows1=browser.window_handles
browser.switch_to.window(windows1[-1])
sleep(5)
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[18]/td[4]/a").click()


windows=browser.window_handles
browser.switch_to.window(windows[-1])
sleep(2400)

browser.close()
sleep(5)

#第19讲
windows1=browser.window_handles
browser.switch_to.window(windows1[-1])
sleep(5)
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[19]/td[4]/a").click()


windows=browser.window_handles
browser.switch_to.window(windows[-1])
sleep(2400)

browser.close()
sleep(5)
'''


"""
#职业能力2
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/div[3]/div/div/table/tbody/tr[4]/td[4]/a").click()
sleep(10)


#第20讲
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[4]/a").click()
sleep(10)


windows=browser.window_handles
browser.switch_to.window(windows[-1])
sleep(900)

browser.close()
sleep(10)



#第21讲
windows1=browser.window_handles
browser.switch_to.window(windows1[-1])
sleep(10)
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[4]/a").click()


windows=browser.window_handles
browser.switch_to.window(windows[-1])
sleep(2400)

browser.close()
sleep(10)

#第22讲
windows1=browser.window_handles
browser.switch_to.window(windows1[-1])
sleep(10)
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[3]/td[4]/a").click()


windows=browser.window_handles
browser.switch_to.window(windows[-1])
sleep(2400)

browser.close()
sleep(10)



#第23讲
windows1=browser.window_handles
browser.switch_to.window(windows1[-1])
sleep(10)
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[4]/td[4]/a").click()


windows=browser.window_handles
browser.switch_to.window(windows[-1])
sleep(2400)

browser.close()
sleep(10)


#第24讲
windows1=browser.window_handles
browser.switch_to.window(windows1[-1])
sleep(10)
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[5]/td[4]/a").click()


windows=browser.window_handles
browser.switch_to.window(windows[-1])
sleep(2400)

browser.close()
sleep(10)


#第25讲
windows1=browser.window_handles
browser.switch_to.window(windows1[-1])
sleep(10)
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[6]/td[4]/a").click()


windows=browser.window_handles
browser.switch_to.window(windows[-1])
sleep(2400)

browser.close()
sleep(10)




#第26讲
windows1=browser.window_handles
browser.switch_to.window(windows1[-1])
sleep(10)
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[7]/td[4]/a").click()


windows=browser.window_handles
browser.switch_to.window(windows[-1])
sleep(2400)

browser.close()
sleep(10)





#第27讲
windows1=browser.window_handles
browser.switch_to.window(windows1[-1])
sleep(10)
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[8]/td[4]/a").click()


windows=browser.window_handles
browser.switch_to.window(windows[-1])
sleep(2400)

browser.close()
sleep(10)





#第28讲
windows1=browser.window_handles
browser.switch_to.window(windows1[-1])
sleep(10)
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[9]/td[4]/a").click()


windows=browser.window_handles
browser.switch_to.window(windows[-1])
sleep(2400)

browser.close()
sleep(10)




#第29讲
windows1=browser.window_handles
browser.switch_to.window(windows1[-1])
sleep(10)
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[10]/td[4]/a").click()


windows=browser.window_handles
browser.switch_to.window(windows[-1])
sleep(2400)

browser.close()
sleep(10)





#第30讲
windows1=browser.window_handles
browser.switch_to.window(windows1[-1])
sleep(10)
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[11]/td[4]/a").click()


windows=browser.window_handles
browser.switch_to.window(windows[-1])
sleep(2400)

browser.close()
sleep(10)

#返回到列表
windows1=browser.window_handles
browser.switch_to.window(windows1[-1])
sleep(10)


browser.get("http://xy.gkwlpx.com/Home")

sleep(10)

"""

'''
#打开绪论
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/div[3]/div/div/table/tbody/tr[10]/td[4]/a").click()
sleep(10)


#打开视频
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr/td[4]/a").click()


windows=browser.window_handles
browser.switch_to.window(windows[-1])
sleep(2400)

browser.close()
sleep(10)


#职业道德1

browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/div[3]/div/div/table/tbody/tr[6]/td[4]/a").click()
sleep(10)


#第一章
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[4]/a").click()
sleep(10)
windows=browser.window_handles
browser.switch_to.window(windows[-1])
sleep(2400)

browser.close()
sleep(10)



#第二章
windows1=browser.window_handles
browser.switch_to.window(windows1[-1])
sleep(10)
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[4]/a").click()


windows=browser.window_handles
browser.switch_to.window(windows[-1])
sleep(2400)

browser.close()
sleep(10)



#第三章
windows1=browser.window_handles
browser.switch_to.window(windows1[-1])
sleep(10)
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[3]/td[4]/a").click()


windows=browser.window_handles
browser.switch_to.window(windows[-1])
sleep(2400)

browser.close()
sleep(10)
'''

'''
print("职业道德2")
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/div[3]/div/div/table/tbody/tr[7]/td[4]/a").click()
sleep(10)

# #第1章
# browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[4]/a").click()
# sleep(10)
# windows=browser.window_handles
# browser.switch_to.window(windows[-1])
# print("等待")
# sleep(2400)
#
# browser.close()
# sleep(10)

#第2章

# browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[4]/a").click()
# sleep(10)
# windows=browser.window_handles
# browser.switch_to.window(windows[-1])
# print("等待")
# sleep(2400)
#
# browser.close()
# sleep(10)

#第8章
# windows=browser.window_handles
# browser.switch_to.window(windows[-1])
sleep(5)
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[8]/td[4]/a").click()
sleep(10)
windows=browser.window_handles
browser.switch_to.window(windows[-1])
print("等待")
sleep(1800)

browser.close()
sleep(10)



#第3章
windows=browser.window_handles
browser.switch_to.window(windows[-1])
sleep(5)
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[3]/td[4]/a").click()
sleep(10)
windows=browser.window_handles
browser.switch_to.window(windows[-1])
print("等待")
sleep(1800)

browser.close()
sleep(10)

#第4章
windows=browser.window_handles
browser.switch_to.window(windows[-1])
sleep(5)
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[4]/td[4]/a").click()
sleep(10)
windows=browser.window_handles
browser.switch_to.window(windows[-1])
print("等待")
sleep(1800)

browser.close()
sleep(10)



#第5章
windows=browser.window_handles
browser.switch_to.window(windows[-1])
sleep(5)
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[5]/td[4]/a").click()
sleep(10)
windows=browser.window_handles
browser.switch_to.window(windows[-1])
print("等待")
sleep(1800)

browser.close()
sleep(10)


#第6章
windows=browser.window_handles
browser.switch_to.window(windows[-1])
sleep(5)
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[6]/td[4]/a").click()
sleep(10)
windows=browser.window_handles
browser.switch_to.window(windows[-1])
print("等待")
sleep(1800)

browser.close()
sleep(10)



#第7章
windows=browser.window_handles
browser.switch_to.window(windows[-1])
sleep(5)
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[7]/td[4]/a").click()
sleep(10)
windows=browser.window_handles
browser.switch_to.window(windows[-1])
print("等待")
sleep(1800)

browser.close()
sleep(10)


#返回列表
windows=browser.window_handles
browser.switch_to.window(windows[-1])
sleep(10)
browser.back()
print("返回上一页")
sleep(10)
'''
'''
print("职业道德3")
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/div[3]/div/div/table/tbody/tr[8]/td[4]/a").click()
sleep(10)

#第1章
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[4]/a").click()
sleep(10)
windows=browser.window_handles
browser.switch_to.window(windows[-1])
print("等待")
sleep(2400)

browser.close()
sleep(10)

#第2章

browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[4]/a").click()
sleep(10)
windows=browser.window_handles
browser.switch_to.window(windows[-1])
print("等待")
sleep(2400)

browser.close()
sleep(10)

#第8章

browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[8]/td[4]/a").click()
sleep(10)
windows=browser.window_handles
browser.switch_to.window(windows[-1])
print("等待")
sleep(2400)

browser.close()
sleep(10)



#第3章

browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[3]/td[4]/a").click()
sleep(10)
windows=browser.window_handles
browser.switch_to.window(windows[-1])
print("等待")
sleep(2400)

browser.close()
sleep(10)

#第4章

browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[4]/td[4]/a").click()
sleep(10)
windows=browser.window_handles
browser.switch_to.window(windows[-1])
print("等待")
sleep(2400)

browser.close()
sleep(10)



#第5章

browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[5]/td[4]/a").click()
sleep(10)
windows=browser.window_handles
browser.switch_to.window(windows[-1])
print("等待")
sleep(2400)

browser.close()
sleep(10)


#第6章

browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[6]/td[4]/a").click()
sleep(10)
windows=browser.window_handles
browser.switch_to.window(windows[-1])
print("等待")
sleep(2400)

browser.close()
sleep(10)



#第7章

browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[7]/td[4]/a").click()
sleep(10)
windows=browser.window_handles
browser.switch_to.window(windows[-1])
print("等待")
sleep(2400)

browser.close()
sleep(10)


#返回列表
windows=browser.window_handles
browser.switch_to.window(windows[-1])
sleep(10)
browser.back()
print("返回上一页")
sleep(10)

print("职业道德3")
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/div[3]/div/div/table/tbody/tr[8]/td[4]/a").click()
sleep(10)


#第1章
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[4]/a").click()
sleep(10)
windows=browser.window_handles
browser.switch_to.window(windows[-1])
print("等待")
sleep(2700)

browser.close()
sleep(10)

#第2章
windows=browser.window_handles
browser.switch_to.window(windows[-1])
sleep(5)
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[4]/a").click()
sleep(10)
windows=browser.window_handles
browser.switch_to.window(windows[-1])
print("等待")
sleep(2700)

browser.close()
sleep(10)

#第3章
windows=browser.window_handles
browser.switch_to.window(windows[-1])
sleep(5)
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[3]/td[4]/a").click()
sleep(10)
windows=browser.window_handles
browser.switch_to.window(windows[-1])
print("等待")
sleep(2700)

browser.close()
sleep(10)



#返回列表
windows=browser.window_handles
browser.switch_to.window(windows[-1])
sleep(10)
browser.back()
print("返回上一页")
sleep(10)

print("职业道德4")
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/div[3]/div/div/table/tbody/tr[9]/td[4]/a").click()
sleep(10)

#第1章

browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[4]/a").click()
sleep(10)
windows=browser.window_handles
browser.switch_to.window(windows[-1])
print("等待")
sleep(2700)

browser.close()
sleep(10)

#第2章
windows=browser.window_handles
browser.switch_to.window(windows[-1])
sleep(5)
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[4]/a").click()
sleep(10)
windows=browser.window_handles
browser.switch_to.window(windows[-1])
print("等待")
sleep(2700)

browser.close()
sleep(10)

#第3章
windows=browser.window_handles
browser.switch_to.window(windows[-1])
sleep(5)
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[3]/td[4]/a").click()
sleep(10)
windows=browser.window_handles
browser.switch_to.window(windows[-1])
print("等待")
sleep(2700)

browser.close()
sleep(10)



#返回列表
windows=browser.window_handles
browser.switch_to.window(windows[-1])
sleep(10)
browser.back()
print("返回上一页")
sleep(10)


print("职业道德5")
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/div[3]/div/div/table/tbody/tr[10]/td[4]/a").click()
sleep(10)

#第1章

browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[4]/a").click()
sleep(10)
windows=browser.window_handles
browser.switch_to.window(windows[-1])
print("等待")
sleep(2700)

browser.close()
sleep(10)

#第2章
windows=browser.window_handles
browser.switch_to.window(windows[-1])
sleep(5)
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[4]/a").click()
sleep(10)
windows=browser.window_handles
browser.switch_to.window(windows[-1])
print("等待")
sleep(2700)

browser.close()
sleep(10)

#第3章
windows=browser.window_handles
browser.switch_to.window(windows[-1])
sleep(5)
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[3]/td[4]/a").click()
sleep(10)
windows=browser.window_handles
browser.switch_to.window(windows[-1])
print("等待")
sleep(2700)

browser.close()
sleep(10)



#返回列表
windows=browser.window_handles
browser.switch_to.window(windows[-1])
sleep(10)
browser.back()
print("返回上一页")
sleep(10)
'''

print("职业道德6")
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/div[3]/div/div/table/tbody/tr[11]/td[4]/a").click()
sleep(10)

#第1章
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[4]/a").click()
sleep(10)
windows=browser.window_handles#获取当前窗口的句柄
browser.switch_to.window(windows[-1])#切换至另一个窗口
print("等待")
sleep(200)

browser.close()
sleep(10)

#第2章
windows=browser.window_handles
browser.switch_to.window(windows[-1])
sleep(10)
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[4]/a").click()
sleep(10)
windows=browser.window_handles
browser.switch_to.window(windows[-1])
print("等待")
sleep(3000)

browser.close()
sleep(10)

#第3章
windows=browser.window_handles
browser.switch_to.window(windows[-1])
sleep(10)
browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[3]/td[4]/a").click()
sleep(10)
windows=browser.window_handles
browser.switch_to.window(windows[-1])
print("等待")
sleep(3000)

browser.close()
sleep(10)












browser.quit()

