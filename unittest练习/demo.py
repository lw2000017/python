# -*-encoding:utf-8 -*-
import requests


username="15836889160"
code="430553"
exc_url="http://121.199.53.9:8051/user/login"
datalist={"phone":username,"code":code}
head = {'Content-Type':'application/Json'}
response =requests.post(exc_url,data= datalist,json=head)
result =response.text
print(result)