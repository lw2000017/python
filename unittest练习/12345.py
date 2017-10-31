# -*-encoding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
_user = "1063681467@qq.com"
_pwd = "lw200017..++--"
_to = "liuwei@zhehekeji.com"
msg = MIMEMultipart()
msg["Subject"]= "测试一下"
msg["From"] = _user
msg["To"] = _to
part = MIMEText("你好")
msg.attach(part)
try:
    s = smtplib.SMTP_SSL("smtp.qq.com",465)
    s.login(_user,_pwd)
    s.sendmail(_user,_to,msg.as_string())
    s.quit()
    print("完美")
except smtplib.SMTPException as e:
    print("shibai")