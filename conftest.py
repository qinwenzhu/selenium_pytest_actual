# -*- coding:utf-8 -*-
# @Time: 2020/3/25 11:26
# @Author: wenqin_zhu
# @File: conftest.py
# @Software: PyCharm


import pytest
import time
from selenium import webdriver

from guard.pages.timezone import TimezonePage
from guard.tools.get_uuid_data import uuid1_data, uuid4_data
from guard.tools.get_current_time import get_current_time

from guard.pages.login import LoginPage
from guard.pages.tool import ToolPage
from guard.pages.components.menubar import MenubarPage
from guard.pages.user import UserPage
from guard.pages.classes.share_path import SharePath
from utils.handle_config import HandleConfig
from utils.handle_database import HandleDB
from guard.pages.classes.run_env import get_run_env


@pytest.fixture(scope="session")
def connect_mysql_and_close():
    # 前置 - 连接数据库 后置 - 关闭连接
    # 读取数据库配置文件中的配置信息
    DB_CONFIG = HandleConfig(r'{}\db_config.yml'.format(SharePath.CONFIG_FOLDER)).config
    db_config = DB_CONFIG.get("database")
    # 通过读取配置文件获取到当前运行环境的ip
    db_config['hostname'] = get_run_env()["host"]       # db_config['host'] = "10.151.3.96"
    # 连接数据库
    database = HandleDB(host=db_config['hostname'], username=db_config['user'],
                  password=db_config['password'], port=db_config['port'], database="senseguard")
    print("数据库连接成功！")
    yield database
    # 关闭游标、关闭数据库
    database.close()


@pytest.fixture(scope="module")
def start_driver_and_quit():
    # 前置 - 启动会话窗口 后置 - 关闭
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def login_web(start_driver_and_quit):
    # 成功登录网站
    start_driver_and_quit.get(f'http://{get_run_env()["host"]}/login')      # start_driver_and_quit.get("http://10.151.3.96/login")
    LoginPage(start_driver_and_quit).login(f'{get_run_env()["username"]}', f'{get_run_env()["password"]}')          # LoginPage(start_driver_and_quit).login("zhuwenqin", "888888")
    yield start_driver_and_quit


""" ---------------------------- 时间条件 timezone ---------------------------- """
@pytest.fixture(scope="module")
def timezone_web(login_web):
    # 进入时间条件模块
    MenubarPage(login_web).click_nav_item("配置", "时间条件")
    yield login_web


@pytest.fixture(scope="class")
def timezone_name(login_web):
    # 创建类时间条件名称，通过该时间条件添加时间段
    sole_time_name = f"TIME-{get_current_time()}"
    yield sole_time_name
    TimezonePage(login_web).delete_or_rename_timezone_name(sole_time_name)


@pytest.fixture(scope="class")
def holiday_name(login_web):
    # 创建假期名称 - 删除假期
    sole_time_name = f"H-{get_current_time()}"
    yield sole_time_name
    TimezonePage(login_web).delete_or_rename_holidays_or_workday(sole_time_name)


@pytest.fixture(scope="class")
def workday_name(login_web):
    # 创建特殊工作日名称 - 删除特殊工作日
    sole_time_name = f"W-{get_current_time()}"
    yield sole_time_name
    TimezonePage(login_web).delete_or_rename_holidays_or_workday(sole_time_name)


@pytest.fixture
def sole_time_name():
    # 创建类时间条件名称，通过该时间条件添加时间段
    sole_time_name = f"ABD-{uuid1_data()}"
    yield sole_time_name


@pytest.fixture
def sole_short_time_name(login_web):
    # 获取当前时间 - 超出字段名称
    sole_short_time_name = f"ABD-{get_current_time()}"
    yield sole_short_time_name


""" ---------------------------- 用户管理 user ---------------------------- """
@pytest.fixture(scope="module")
def user_web(login_web):
    # 进入用户管理模块
    MenubarPage(login_web).click_nav_item("配置", "用户管理")
    yield login_web


@pytest.fixture(scope="class")
def dep_name(user_web):
    # 前置 - 准备分组名称
    group_name = f"UDN-{uuid4_data()}"
    yield user_web, group_name
    # 删除通过Default用户组创建的同级分组
    # UserPage(user_web).delete_department_by_name(parent_name=group_name)


@pytest.fixture
def close_alert(user_web):
    # 删除alert弹框
    yield
    UserPage(user_web).close_alert()


@pytest.fixture
def sole_group_name():
    # 前置 - 分组名 - 只针对测试用例<保证数据唯一性>
    sole_group_name = f"UDN-{uuid4_data()}"
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


""" ---------------------------- 登录 login ---------------------------- """
@pytest.fixture(scope="class")
def login(start_driver_and_quit):
    start_driver_and_quit.get(f'http://{get_run_env()["host"]}/login')               # start_driver_and_quit.get("http://10.151.3.96/login")
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
