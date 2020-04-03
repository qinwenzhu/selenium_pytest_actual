# -*- coding:utf-8 -*-
# @Time: 2020/3/25 11:26
# @Author: wenqin_zhu
# @File: conftest.py
# @Software: PyCharm


import pytest
from selenium import webdriver

from utils.uuid_generate_unique_data import uuid_data

from guard.pages.login_backup import LoginPage
from guard.pages.tool import ToolPage
from guard.pages.components.menubar import MenubarPage
from guard.pages.components.group_tree import GroupTree
from guard.pages.user import UserPage


@pytest.fixture(scope="session")
def start_driver_and_quit():
    # 前置 - 启动会话窗口 后置 - 关闭
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def login_web(start_driver_and_quit):
    # 登录web网站
    start_driver_and_quit.get("http://10.151.3.96/login")
    LoginPage(start_driver_and_quit).login("zhuwenqin", "888888")
    yield start_driver_and_quit


""" ---------------------------- 用户管理 user ---------------------------- """
@pytest.fixture(scope="class")
def user_web(login_web):
    # 进入用户管理模块
    MenubarPage(login_web).click_nav_item("配置", "用户管理")
    yield login_web


@pytest.fixture
def user_management(user_web):
    # 前置 - 准备分组名称 后置 - 删除同级分组
    group_name = f"UDN-{uuid_data()}"
    yield user_web, group_name
    UserPage(user_web).delete_dep_by_name(group_name)


@pytest.fixture
def user_del_sub_dep_group(user_web):
    # 前置 - 准备分组名称 后置 - 删除下一级分组
    group_name = f"UDN-{uuid_data()}"
    yield user_web, group_name
    UserPage(user_web).delete_dep_by_name(group_name, flag=False)


# @pytest.fixture(scope="class")
# def add_user_and_delete_user(user_management):
#     # 从Default创建同级分组
#     group_name = uuid_data()
#     til_name = UserPage(user_management[0]).add_department_by_root_name()
#     UserPage(user_management[0]).create_department_group(group_name, til_name)
#     yield group_name
#     UserPage(user_management[0]).delete_dep_by_name(group_name)


""" ---------------------------- 登录 login ---------------------------- """
@pytest.fixture(scope="class")
def login(start_driver_and_quit):
    start_driver_and_quit.get("http://10.151.3.96/login")
    yield start_driver_and_quit


""" ---------------------------- 工具 tool ---------------------------- """
@pytest.fixture(scope="function")
def tool_close_one_to_one_face_compare(login_web):
    # 后置：关闭当前窗口 - 1:1人脸验证
    yield
    ToolPage(login_web).close_tool_current_win("tools-face-verification")


@pytest.fixture
def tool_close_one_img_quality(login_web):
    # 后置：关闭当前窗口 - 质量分数检测
    yield
    ToolPage(login_web).close_tool_current_win("tools-score-detection")


@pytest.fixture
def tool_close_face_score_detection(login_web):
    # 后置：关闭当前窗口 - 人脸属性检测
    yield
    ToolPage(login_web).close_tool_current_win("tools-test-detection")
