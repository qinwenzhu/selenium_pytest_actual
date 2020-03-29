# -*- coding:utf-8 -*-
# @Time: 2020/3/17 15:31
# @Author: wenqin_zhu
# @File: login_data.py
# @Software: PyCharm


class LoginData:

    # 正向用例数据
    success_login_data = ("zhuwenqin", "888888")

    # 反向异常测试数据
    login_data = [
        {"username": "", "password": ""}
    ]
