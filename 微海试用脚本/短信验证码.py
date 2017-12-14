# -*-encoding:utf-8 -*-
import http.client
import urllib.parse


host = "106.ihuyi.com"
sms_send_uri = "/webservice/sms.php?method=Submit"

zhanghao = "C15760153"
password = "b3a4a3fb50e9863a9a3e79dd4d4c25c7"

def send_sms(text,mobile):
    params = urllib.parse.urlencode(
        {
            'account': zhanghao,
            'password': password,
            'content': text,
            'mobile': mobile,
            'format': 'json'
        }
    )
    headers = {
        'Content-type': 'application/x-www-form-urlencoded',
        'Accept': 'text/plain'
    }
    conn = http.client.HTTPConnection(host,port=80,timeout=30)
    conn.request('POST',sms_send_uri,params,headers)
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    return response_str

if __name__ == '__main__':
    mobile = '15836889160'
    text = "您的验证码是：123456。请不要把验证码泄露给其他人。"
    print(send_sms(text,mobile))