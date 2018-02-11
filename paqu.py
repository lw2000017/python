# coding:utf-8
import urllib
import urllib2
import re

class Spider():
    def __init__(self):
        self.siteURL = "http://www.tu11.com/"

    def getPage(self,pageIndex):#获取索引页面的内容
        url = self.siteURL + str(pageIndex)
        print url
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read().decode('gbk')
    def getContents(self,pageIndex):
        page = self.getPage(pageIndex)
        pattern = re.compile('<div class="shupic"<a href="(.*?)">>'
            '<div class = ".*?"<a herf="(.*?html).*?<img src="(.*?.jpg)".*?">',re.S)
        items = re.findall(pattern,page)
        for item in items:
            print items[0],items[1]
    def getALLImg(self,page):#获取页面所有图片
        pattern = re.compile('<div class = "shupic".*?>(.*?)<!--',re.S)
        content = re.search(page,page)
        patternImg = re.compile('<img.*?src="(.*?)"',re.S)
        images = re.findall(patternImg,content.group(1))
        return images
    def saveImages(self,images,name):
        number = 1
        print u"发现",name,u"共有",len(images),u"张照片"
        for imageURL in images:
            splitPath = imageURL.split('.')
            fTail = splitPath.pop()
            if len(fTail)>3:
                fTail = 'jpg'
            fileName = name + '/' + str(number) + '.' +fTail
            self.saveImages(imageURL,fileName)
            number += 1



spider = Spider()
spider.getContents("xingganmeinvxiezhen")

