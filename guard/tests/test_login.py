# -*- coding:utf-8 -*-
# @Time: 2020/3/17 10:05
# @Author: wenqin_zhu
# @File: test_login.py
# @Software: PyCharm


import pytest
from guard.pages.login import LoginPage
from guard.data.login_data import LoginData


@pytest.mark.positive
def test_login_success(login):
    LoginPage(login).login(*LoginData.success_login_data)

    # 断言 - 只要判断首页的某个指定元素存在，说明登录成功并进行页面跳转
    # assert LoginPage(login).is_login_success()

    # TODO 此处需要连接数据库动态判断当前登陆用户的别名
    # sql = "SELECT * FROM senseguard. WHERE =%s;"
    # query_result_by_database(sql)
    # result = LoginPage(login).login_success_info()
    # assert  ==


# @pytest.mark.parametrize("data", LoginData.login_data)
# @pytest.mark.negative
# def test_login_negative(login, data):
#     LoginPage(login).login(data["username"], data["password"])


if __name__ == '__main__':
    pytest.main()
