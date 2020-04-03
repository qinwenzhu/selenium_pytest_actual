# -*- coding:utf-8 -*-
# @Time: 2020/4/1 18:57
# @Author: wenqin_zhu
# @File: test_user.py
# @Software: PyCharm

import pytest

from guard.pages.user import UserPage


@pytest.mark.usefixtures("user_management")
class TestUser:

    pass

    # def test_create_equal_department(self, user_management):
    #     """ 测试从根<Default>部门创建同级部门
    #             add_department_by_root_name(flag=True)
    #     """
    #     # 创建分组名称 flag为True<默认创建同级，如果为False，则为创建下一级>
    #     title_name = UserPage(user_management[0]).add_department_by_root_name()
    #     # 传递title名称和分组名称
    #     UserPage(user_management[0]).create_department_group(group_name=user_management[1], til_name=title_name)
    #
    # def test_create_next_department(self, user_management):
    #     """ 测试在根<Default>部门创建下一级部门
    #             add_department_by_root_name(flag=True)
    #     """
    #     # 创建分组名称 flag为True<默认创建同级，如果为False，则为创建下一级>
    #     title_name = UserPage(user_management[0]).add_department_by_root_name(flag=False)
    #     UserPage(user_management[0]).create_department_group(group_name=user_management[1], til_name=title_name)



