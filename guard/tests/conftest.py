# -*- coding:utf-8 -*-
# @Time: 2020/3/25 11:26
# @Author: wenqin_zhu
# @File: conftest.py
# @Software: PyCharm


import pytest
from selenium import webdriver

from guard.pages.login_backup import LoginPage
from guard.pages.tool import ToolPage
from guard.pages.components.menubar import MenubarPage
from guard.pages.user import UserPage

# 系统公共
@pytest.fixture(scope="class")
def web_login_and_quit():
    driver = webdriver.Chrome()
    driver.get("http://10.151.3.96/login")
    LoginPage(driver).login("zhuwenqin", "888888")
    yield driver
    driver.quit()

# 登录
@pytest.fixture(scope="class")
def login_and_quit():
    driver = webdriver.Chrome()
    driver.get("http://10.151.3.96/login")
    yield driver
    driver.quit()


""" 工具 tool """
@pytest.fixture(scope="function")
def tool_close_one_to_one_face_compare(web_login_and_quit):
    # 后置：关闭当前窗口 - 1:1人脸验证
    yield
    ToolPage(web_login_and_quit).close_tool_current_win("tools-face-verification")


@pytest.fixture
def tool_close_one_img_quality(web_login_and_quit):
    # 后置：关闭当前窗口 - 质量分数检测
    yield
    ToolPage(web_login_and_quit).close_tool_current_win("tools-score-detection")


@pytest.fixture
def tool_close_face_score_detection(web_login_and_quit):
    # 后置：关闭当前窗口 - 人脸属性检测
    yield
    ToolPage(web_login_and_quit).close_tool_current_win("tools-test-detection")


""" 用户管理 user """
@pytest.fixture(scope="class")
def user_comm(web_login_and_quit):
    # 进入用户管理模块
    MenubarPage(web_login_and_quit).click_nav_item("配置", "用户管理")
    yield web_login_and_quit
