# -*- coding:utf-8 -*-
# @Time: 2020/3/25 11:26
# @Author: wenqin_zhu
# @File: conftest.py
# @Software: PyCharm


import pytest
import time
from selenium import webdriver

from utils.uuid_generate_unique_data import uuid_data

from guard.pages.login_backup import LoginPage
from guard.pages.tool import ToolPage
from guard.pages.components.menubar import MenubarPage
from guard.pages.user import UserPage


@pytest.fixture(scope="module")
def start_driver_and_quit():
    # 前置 - 启动会话窗口 后置 - 关闭
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def login_web(start_driver_and_quit):
    # 登录web网站
    start_driver_and_quit.get("http://10.151.3.96/login")
    LoginPage(start_driver_and_quit).login("zhuwenqin", "888888")
    yield start_driver_and_quit


""" ---------------------------- 用户管理 user ---------------------------- """
@pytest.fixture(scope="module")
def user_web(login_web):
    # 进入用户管理模块
    MenubarPage(login_web).click_nav_item("配置", "用户管理")
    yield login_web


@pytest.fixture(scope="class")
def dep_name(user_web):
    # 前置 - 准备分组名称
    group_name = f"UDN-{uuid_data()}"
    yield user_web, group_name
    # # 删除通过Default用户组创建的同级分组
    # UserPage(user_web).delete_department_by_name(parent_name=group_name)


@pytest.fixture
def close_alert(user_web):
    # 删除alert弹框
    yield
    UserPage(user_web).close_alert()


@pytest.fixture
def sole_group_name(dep_name):
    # 前置 - 分组名 - 只针对测试用例<保证数据唯一性>
    sole_group_name = f"UDN-{uuid_data()}"
    yield sole_group_name


@pytest.fixture
def del_sub_dep_name_to_default(dep_name, sole_group_name):
    yield
    # 删除Default分组的下一级分组
    UserPage(dep_name[0]).delete_department_by_name(sub_name=sole_group_name, is_peer=False)
    time.sleep(2)


@pytest.fixture
def del_dep_name_to_user(dep_name, sole_group_name):
    yield
    # 删除用户自定义分组
    UserPage(dep_name[0]).delete_department_by_name(parent_name=sole_group_name)
    time.sleep(2)


@pytest.fixture
def del_sub_dep_name_to_user(dep_name, sole_group_name):
    yield
    # 删除用户自定义分组的下一级分组
    UserPage(dep_name[0]).delete_department_by_name(sub_name=sole_group_name, parent_name=dep_name[1], is_peer=False)
    time.sleep(2)





# @pytest.fixture
# def add_dep_sole_name_and_del(dep_name):
#     # 前置 - 准备分组名称 - 只针对测试用例<保证数据唯一性>
#     sole_group_name = f"UDN-{uuid_data()}"
#     yield sole_group_name
#     # 删除通过Default用户组创建的父级分组下的同级分组
#     UserPage(dep_name[0]).delete_department_by_name(sub_name=sole_group_name, parent_name=dep_name[1])
#
#

#
#
# @pytest.fixture
# def del_sub_dep_by_default(dep_name):
#     # 前置 - 准备分组名称 - 只针对测试用例<保证数据唯一性>
#     sole_group_name = f"UDN-{uuid_data()}"
#     yield sole_group_name
#     # 删除通过Default用户组创建的下一级分组
#     UserPage(dep_name[0]).delete_department_by_name(sub_name=sole_group_name, parent_name="Default")


# @pytest.fixture
# def teardown_delete_dep(user_web):
#     # 前置 - 准备分组名称 - 只针对测试用例<保证数据唯一性>
#     sole_group_name = f"UDN-{uuid_data()}"
#     yield sole_group_name
#     UserPage(user_web).delete_department_by_name()






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
