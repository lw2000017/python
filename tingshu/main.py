# -*-encoding:utf-8 -*-
import unittest
import os

# 用例的路径
# case_path = os.path.join(os.getcwd(),"test_login")

case_path = os.path.join(os.getcwd(),"test_login")


# def all_case():
#     discover = unittest.defaultTestLoader.discover(case_path,pattern = "ts*.py",top_level_dir = None)
#     print(discover)
#     return discover

def all_case():
    # 确定跑哪些脚本
    discover = unittest.defaultTestLoader.discover(case_path,pattern="ts*.py",top_level_dir=None)
    # 打印脚本的名称
    print(discover)

    return discover


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(all_case())