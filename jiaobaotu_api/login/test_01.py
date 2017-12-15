# -*-encoding:utf-8 -*-
import requests
import json
def test_login(username,password):
    url = "http://hdl.zhehekeji.com:8075/mobileManage/login/index"
    headers = {
        # 'Access-Control-Allow-Origin':*,
        # 'Connection':'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8'
    }
    datas = {
        # 'login':username,
        # 'passwd':password,
        # 'remember':1
        'username': username,
        'password': password
    }
    r = requests.post(url=url,json=datas,headers=headers)
    print(r.text)
    # print(r.status_code)
if __name__ == '__main__':
    test_login(username = "测试门店1",password = "123456")

