import os
from selenium import webdriver
#from appium import webdriver
# Returns abs path relative to this file and not cwd
device='88CFBMA23FVA' #此处设备号
pack='com.zhehekeji.sdxf_2.0.2_2 3' #此处是我们app的package名称
activity='.com.zhehekeji.sdxf.activity.login.LogoActivity'#此处是我们的app的主activity
#下面的按照我的脚本内容填写即可，里边内容的意思也很清晰吧
PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
desired_caps={}
desired_caps['device'] = 'android'
desired_caps['platformName']='Android'
desired_caps['browserName']=''
desired_caps['Version']='4.4.4'
desired_caps['deviceName']=device
#desired_caps['app']=PATH('e:\sdxf2.0.2.apk')
desired_caps['appPackage'] = pack
desired_caps['appActivity'] = activity
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)