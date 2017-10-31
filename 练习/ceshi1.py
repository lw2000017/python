from selenium import webdriver
from public import login
import time

chromedriver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
browser = webdriver.Chrome(chromedriver)
#打开浏览器
browser.get("http://120.26.50.11:8088/publish/crm/login.html")
time.sleep(2)


login().user_login(browser)
time.sleep(2)
#复选框
browser.find_element_by_id("loginuserimg").click()
time.sleep(4)
browser.find_element_by_id('setupPower').click()
time.sleep(5)
browser.find_element_by_xpath('//*[@id="side"]/div[1]/div[2]/div[1]').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="side"]/div[1]/div[2]/div[2]/div[2]/a').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="manager"]/div[3]/div[3]/div[2]/div[2]/div[2]/div[6]/a').click()

time.sleep(5)
for i in browser.find_elements_by_xpath('//input[@type="checkbox"]'):
    browser.implicitly_wait(10)
    i.click()