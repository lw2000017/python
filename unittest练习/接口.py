# -*-encoding:utf-8 -*-
# from flask import Flask
#
# app=Flask(__name__)
# @app.route("/user/<name>")
# def user(name):
#     return "<h1>hello %s !</h1>"%name
#
# if __name__ == '__main__':
#     app.run(debug=True)


import requests
import json

def test_ceshi():
    # url="http://hrsit1.haidilao.com:8000/PSIGW/RESTListeningConnector/PSFT_HR/EMPLOYEESYNCFROMWEIHAI.v1/HIRE"
    # headers={
    #     "Content-Type":"application/json; charset=UTF-8",
    #     "X-Requested-By": "WeiHai Recruiting"
    # }
    # data ={
    #     "PersonalData":
    #         [
    #             {
    #                 "FIRST_NAME": "世祥",
    #                 "LAST_NAME": "徐",
    #                 "SEX": "M",
    #                 "CITY": "北京",
    #                 "TrainerNid": "532925198107171110",
    #                 "C_BIRTH_TYPE": "I",
    #                 "BIRTHDATE": "1990-01-01",
    #                 "MAR_STATUS": "1",
    #                 "NATIVE_PLACE_CHN": "云南",
    #                 "HUKOU_TYPE_CHN": "农业户口",
    #                 "ETHNIC_GRP_CD": "汉族",
    #                 "PHONE": "15120001535",
    #                 "EMPL_TYPE": "1",
    #                 "ADDRESS1": "云南省大理白族自治州弥渡县苴力镇白邑村62号",
    #                 "NID_SPECIAL_CHAR": "532925198107171116",
    #                 "CMPNY_SENIORITY_DT": "2014-10-04",
    #                 "ADDRESS2": "北京市朝阳区国风北京地下层606",
    #                 "C_CRIME_FLAG": "N",
    #                 "DESCR254": "无",
    #                 "POLITICAL_STA_CHN": "群众",
    #                 "EMPLID_TO": "重新入职",
    #                 "CONTACT_NAME": "测试",
    #                 "RELATIONSHIP": "01",
    #                 "PHONE2": "13102011011",
    #                 "C_DRIV_DEGREE": "01",
    #                 "C_COMPUTER_FLAG": "01",
    #                 "DESCR254A": "无"
    #             }
    #         ],
    #     "JobData":
    #         [
    #             {
    #                 "HIRE_DT": "2014-10-04",
    #                 "PROBATION_PERIOD": "2",
    #                 "ACTION_REASON": "无",
    #                 "POSITION_NBR": "103850"
    #
    #             }
    #         ],
    #     "EducationData[BEGIN_DT]": "1990-01-01",
    #     "EducationData[END_DT]": "2000-01-01",
    #     "EducationData[SCHOOL_DESCR]": "这是一个测试学校",
    #     "EducationData[MAJOR_DESCR]": "这是一个测试专业",
    #     "EducationData[HIGHEST_EDUC_LVL]": "03",
    #     "EducationData[C_DEGREE]": "01",
    #     "EducationData[C_LEARN_TYPE]": "01",
    #
    #     "PriorWorkData[BUSINESS_DESCR]": "入职前的公司名称",
    #     "PriorWorkData[BEGIN_DT]": "2012-05-04",
    #     "PriorWorkData[END_DT]": "2014-07-08",
    #     "PriorWorkData[ENDING_TITLE]": "入职前的工作岗位及职务",
    #     "PriorWorkData[DESCR254]": "离职原因",
    #
    #     "DependentData[NAME_AC]": "员工家属名称",
    #     "DependentData[C_RELATIONSHIP3]": "09",
    #     "DependentData[NID_SPECIAL_CHAR]": "123456789012345678",
    #     "DependentData[C_CITY_DESC]": "hanghzhou",
    #     "DependentData[BUSINESS_DESCR]": "员工家属的工作单位",
    #     "DependentData[C_BIRTH_TYPE]": "I",
    #     "DependentData[BIRTHDATE]": "1989-02-02",
    #
    #     "DependentData": [
    #         {
    #             "NAME_AC": "员工家属名称",
    #             "C_RELATIONSHIP3": "09",
    #             "NID_SPECIAL_CHAR": "123456789012345678",
    #             "C_CITY_DESC": "hanghzhou",
    #             "BUSINESS_DESCR": "员工家属的工作单位",
    #             "C_BIRTH_TYPE": "I",
    #             "BIRTHDATE": "1989-02-02"
    #
    #         }
    #     ],
    #     "NearRelativesData": [
    #         {
    #             "EMPLID2": "10017870",
    #             "C_RELATIONSHIP4": "01"
    #
    #         }],
    #     "HealthCardData": [
    #         {
    #             "BEGIN_DT": "2017-01-01",
    #             "C_CITY_DESC": "hangzhou",
    #             "C_AMT": "200",
    #             "END_DT": "2018-01-01"
    #
    #         }],
    #     "BankCardData": [
    #         {
    #             "ACCOUNT_TYPE_PYE": "T",
    #             "BANK_CD": "12345678909",
    #             "C_ACCOUNT_ADDR": "zheshiyigedizhi,woshuoshijiushi",
    #             "ACCOUNT_EC_ID": "123456789098765431"
    #         }]
    # }
    # r=requests.post(url =url,json=data,headers=headers)
    # print(r.text)
    # print(r.status_code)
    url = "http://120.26.50.11:8601/admin/user/login"
    headers = {}
    data = {
        "login":"admin",
        "passwd":"123456",
        "rember":"1"
    }
    r = requests.post(url=url, json=data, headers=headers)
    print(r.text)
    print(r.status_code)
    try:
        if r.status_code==200:
            print("返回成功")
        else:
            print("fanhuishibai")
    except Exception as a :
        print("shiabia")
if __name__ == '__main__':
    test_ceshi()