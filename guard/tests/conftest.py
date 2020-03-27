# -*- coding:utf-8 -*-
# @Time: 2020/3/25 11:26
# @Author: wenqin_zhu
# @File: conftest.py
# @Software: PyCharm


import pytest
from selenium import webdriver

from guard.pages.login_backup import LoginPage


@pytest.fixture(scope="session", autouse=True)
def web_login_and_quit():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://10.151.3.96/login")
    LoginPage(driver).login("zhuwenqin", "888888")
    yield driver
    # driver.quit()


