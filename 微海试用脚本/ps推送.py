# -*-encoding:utf-8 -*-
import paramiko
import os
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import sched
import HTMLTestRunner
import datetime


def serverConnect():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname='121.199.53.9',port=22,username='liuwei',password="123456")
    return ssh
ssh = serverConnect()
# 读取指定文本内容
stdin,stdout,stderr = ssh.exec_command('ls /www/wh_interface/backend/web/logs/')

# 读取文件列表
lists = stdout.readlines()
print(lists)
nowtime = time.strftime('%Y-%m-%d',time.localtime(time.time()))
print(nowtime)
for i in lists:
    if nowtime == '2017-12-14':
        stdin,stdout,stderr = ssh.exec_command("cat /www/wh_interface/backend/web/logs/" + i)
        text = stdout.readlines()
        print(text)
    # else:
    #     time.sleep(24*60*60)
        for a in text:
            if '"StatusCode":"N"' in a:  # i等于一行的内容
                # 文件加上时间戳
                # Nowtime = time.strftime("%Y_%m_%d%H_%M_%S")
                with open(u"C:\\Users\Administrator\Desktop\项目\error"+nowtime+".txt", 'a') as f:
                    f.write(a + '\n')




        # f.close()

def get_report_file(report_path):
    """获取最新的测试报告"""
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn:os.path.getmtime(os.path.join(report_path,fn)))
    print(u"最新测试生成的错误日志:"+lists[-1])
    # 找到最新生成的测试报告文件
    report_file = os.path.join(report_path,lists[-1])
    return report_file


def send_mail(sender, psw, receiver, smtpserver, report_file):
    # 发送最新的测试报告内容
    # 读取测试报告的内容
    with open(report_file,"rb") as f:
        mail_body = f.read()
    # 定义邮件内容
    msg = MIMEMultipart()
    body = MIMEText(mail_body, _subtype='txt', _charset='utf-8')
    Nowtime = time.strftime("%Y_%m_%d-%H:%M:%S")
    msg['Subject'] = u"截取错误信息" + Nowtime
    msg['from'] = sender
    msg['to'] = receiver
    # 加上时间戳
    msg['date'] = time.strftime('%a,%d%b%Y%H_%M_%S%z')
    msg.attach(body)
    # 添加附件
    att = MIMEText(open(report_file, "rb").read(), "base64", "utf-8")
    # att = MIMEMultipart()
    att['Content-Type'] = "application/octet-stream"
    att['Content-Disposition'] = 'attachment;filename = "report.txt"'
    msg.attach(att)
    # 登录邮箱
    smtp = smtplib.SMTP()
    # 链接邮箱服务器
    smtp.connect(smtpserver)
    # 输入用户名密码
    smtp.login(sender, psw)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print('test report email has send out!')


if __name__ == '__main__':
            # 生成测试报告的路径
            report_path = "C:\\Users\Administrator\Desktop\项目"
            # 获取最新的测试报告文件
            report_file = get_report_file(report_path)  # 3.获取最新的测试报告
            # 邮箱配置
            jieshouren = {'1063681467@qq.com', 'liuwei@zhehekeji.com'}
            for receiver1 in jieshouren:
                receiver = receiver1
                sender = 'liuwei@zhehekeji.com'
                psw = 'LWlw1234..++--'
            # 收件人多个时，中间用逗号隔开


            # receiver = 'liuwei@zhehekeji.com'
                smtp_server = "smtp.exmail.qq.com"
                send_mail(sender, psw, receiver, smtp_server,report_file)
