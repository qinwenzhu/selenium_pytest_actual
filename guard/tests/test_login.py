# -*- coding:utf-8 -*-
# @Time: 2020/3/17 10:05
# @Author: wenqin_zhu
# @File: test_login.py
# @Software: PyCharm


import pytest
from guard.pages.login import LoginPage
from guard.datas.login_data import LoginData


@pytest.mark.positive
def test_login_success(login):
    LoginPage(login).login(*LoginData.success_login_data)

    # 断言 - 只要判断首页的某个指定元素存在，说明登录成功并进行页面跳转
    assert LoginPage(login).is_login_success()

# @pytest.mark.parametrize("datas", LoginData.login_data)
# @pytest.mark.negative
# def test_login_negative(login, datas):
#     LoginPage(login).login(datas["username"], datas["password"])


if __name__ == '__main__':
    pytest.main()
