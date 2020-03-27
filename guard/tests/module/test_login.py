# -*- coding:utf-8 -*-
# @Time: 2020/3/17 10:05
# @Author: wenqin_zhu
# @File: test_login.py
# @Software: PyCharm


import pytest
from guard.pages.login_backup import LoginPage


def test_login_success(web_login_and_quit):
    assert "祝文琴" == LoginPage(web_login_and_quit).login_success_info()


if __name__ == '__main__':
    pytest.main()
