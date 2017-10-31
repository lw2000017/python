# -*-encoding:utf-8 -*-
import unittest
import baidu
import HTMLTestRunner
testunit=unittest.TestSuite()
testunit.addTest(unittest.makeSuite(baidu.Baidu))
filename="E:\\python\\report\\"+u"测试报告正常"+"reselt.html"
fp=open(filename,"wb")
runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'测试报告',description=u"用例执行情况：")
runner.run(testunit)