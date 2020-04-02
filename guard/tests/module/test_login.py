# -*- coding:utf-8 -*-
# @Time: 2020/3/17 10:05
# @Author: wenqin_zhu
# @File: test_login.py
# @Software: PyCharm


import pytest
from guard.pages.login import LoginPage
from guard.data.login_data import LoginData

from guard.tests.path import CommonPath

from utils.database import Database
from utils.handle_config import HandleConfig

@pytest.mark.positive
def test_login_success(login_and_quit):
    LoginPage(login_and_quit).login(*LoginData.success_login_data)

    # 断言 - 只要判断首页的某个指定元素存在，说明登录成功并进行页面跳转
    assert LoginPage(login_and_quit).get_login_success()

    # TODO 此处需要连接数据库动态判断当前登陆用户的别名
    # assert "祝文琴" == LoginPage(login_and_quit).login_success_info()


# @pytest.mark.parametrize("data", LoginData.login_data)
# @pytest.mark.negative
# def test_login_negative(login_and_quit, data):
#     LoginPage(login_and_quit).login(data["username"], data["password"])


if __name__ == '__main__':
    pytest.main()
