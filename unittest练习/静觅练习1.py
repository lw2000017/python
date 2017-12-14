# -*-encoding:utf-8 -*-
import urllib2
import urllib

# request1 = urllib2.Request("http://www.baidu.com")
# response1 = urllib2.urlopen(request1)
# print response1.read()

# '''传递参数，post方法'''
# values = {"username" : "xxxx","passwprd":"xxxx"}
# data = urllib.urlencode(values)
# url = "http://xxxxxxxx"
# request = urllib2.Request(url,data)
# response = urllib2.urlopen(request)
# print response.read()
#
#
# '''传递参数，get方法'''
# values1 = {}
# values1["username"] = "xxxxx"
# values1["password"] = "xxxxx"
# data1 = urllib.urlencode(values1)
# url1 = "https://xxxxxx"
# geturl = url1 + "?" + data1
# request1 = urllib2.Request(geturl)
# response1 = urllib2.urlopen(request1)
# print response1.read()


req = urllib2.Request("http://blog.csdn.net/cqcr")
try:
    urllib2.urlopen(req)
except urllib2.HTTPError,e:
    print e.code
    print e.reason