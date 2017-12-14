# -*-encoding:utf-8 -*-
import urllib2
import urllib
import re
import tool
import os

class Spider:
    # 页面初始化
    def __init__(self):
        self.siteURL = "http://www.mzitu.com/"
        self.tool = tool.Tool()

    # 获取索引页面的内容
    def getPage(self,pageIndex):
        url = self.siteURL + "/" + str(pageIndex)
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read().decode('gbk')

    # 获取页面所有图片
    def getAllImg(self,page):
        pattern = re.compile('<div class="main".*?>(.*?)<!--',re.S)
        # 获取页面所有代码
        content = re.search((pattern,page))
        # 从代码中提取图片
        patternImg = re.compile('<img.*?src="(.*?)"',re.S)
        image = re.findall(patternImg,content,group(1))
        return image

    # 保存多张图片
    def saveImags(self,images,name):
        number = 1
        print u"发现",name,u"共有",len(images),u"照片"
        for imageURL in images:
            splitPath = imageURL.split(".")
            fTail = splitPath.pop()
            if len(fTail) > 3:
                fTail = "jpg"
            fileName = name + "/" + str(number)+ "." + fTail
            self.saveImags(imageURL,fileName)
            number += 1
