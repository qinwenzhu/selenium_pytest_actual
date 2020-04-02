# -*- coding:utf-8 -*-
# @Time: 2020/4/1 18:57
# @Author: wenqin_zhu
# @File: test_user.py
# @Software: PyCharm

import pytest

# 生成随机数
import uuid

from guard.pages.user import UserPage


@pytest.mark.usefixtures("web_login_and_quit", "user_comm")
class TestUser:

    def test_create_equal_department(self, web_login_and_quit):
        """ 测试从根<Default>部门创建同级部门
                add_department_by_root_name(flag=True)
        """
        # 创建分组名称 flag为True<默认创建同级，如果为False，则为创建下一级>
        title_name = UserPage(web_login_and_quit).add_department_by_root_name()
        UserPage(web_login_and_quit).create_department_group(title_name, f"UDN-{uuid.uuid1()}")

    def test_create_next_department(self, web_login_and_quit):
        """ 测试从根<Default>部门创建下一级部门
                add_department_by_root_name(flag=True)
        """
        # 创建分组名称 flag为True<默认创建同级，如果为False，则为创建下一级>
        title_name = UserPage(web_login_and_quit).add_department_by_root_name(flag=False)
        UserPage(web_login_and_quit).create_department_group(title_name, f"SUDN-{uuid.uuid1()}")


