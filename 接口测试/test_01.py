# -*-encoding:utf-8 -*-
import requests
import json

def test_test():
    url="http://120.26.50.11:8601/admin/user/login"
    headers={}
    data={
        "login":"admin",
        "passwd":"123456",
        "remember":"1"
    }
    r=requests.post(url=url,data=data,headers=headers)
    print(r.text)
    print(r.status_code)

if __name__ == '__main__':
    test_test()