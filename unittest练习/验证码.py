# -*-encoding:utf-8 -*-
from  selenium import webdriver
import pytesseract
from PIL import Image

browser=webdriver.Chrome()
browser.get("http://123.206.221.113:8010/login")

browser.maximize_window()

browser.save_screenshot("e://aaa.png")
imgelement=browser.find_element_by_xpath('//*[@id="captcha"]')
location = imgelement.location
size=imgelement.size

rangle=(int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height']))
i=Image.open("e://aaa.png")

frame4=i.crop(rangle)
frame4.save("e://frame4.png")
aa=Image.open("e://frame4.png")
text=pytesseract.image_to_string(aa).strip()
print(text)