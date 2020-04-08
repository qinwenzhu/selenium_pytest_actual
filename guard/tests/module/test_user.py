# -*- coding:utf-8 -*-
# @Time: 2020/4/1 18:57
# @Author: wenqin_zhu
# @File: test_user.py
# @Software: PyCharm

import pytest

from guard.pages.components.group_tree import GroupTree
from guard.pages.user import UserPage


@pytest.mark.usefixtures("user_web")
class TestUser:

    @pytest.mark.usefixtures("close_alert")
    @pytest.mark.positive
    def test_create_peer_dep_from_Default(self, dep_name):
        # 测试从Default根分组创建同级分组
        UserPage(dep_name[0]).create_department_from_Default(dep_name[1])

        result = UserPage(dep_name[0]).judge_alert_info()
        assert "创建同级分组成功" == result

    @pytest.mark.positive
    @pytest.mark.usefixtures("close_alert", "del_sub_dep_name_to_user")
    def test_create_next_dep_from_user_defined(self, dep_name, sole_group_name):
        # 测试从用户自定义分组创建下一级分组
        UserPage(dep_name[0]).create_department_from_user_defined(group_name=sole_group_name, parent_name=dep_name[1], is_peer=False)

        result = UserPage(dep_name[0]).judge_alert_info()
        assert "创建下一级分组成功" == result

    @pytest.mark.positive
    @pytest.mark.usefixtures("close_alert", "del_dep_name_to_user")
    def test_create_peer_dep_from_user_defined(self, dep_name, sole_group_name):
        # 测试从用户自定义分组创建同级分组
        UserPage(dep_name[0]).create_department_from_user_defined(group_name=sole_group_name, parent_name=dep_name[1])

        result = UserPage(dep_name[0]).judge_alert_info()
        assert "创建同级分组成功" == result

    @pytest.mark.positive
    @pytest.mark.usefixtures("close_alert", "del_sub_dep_name_to_default")
    def test_create_next_dep_from_Default(self, dep_name, sole_group_name):
        # 测试从Default根分组创建下一级分组
        UserPage(dep_name[0]).create_department_from_Default(sole_group_name, is_peer=False)

        result = UserPage(dep_name[0]).judge_alert_info()
        assert "创建下一级分组成功" == result

    @pytest.mark.positive
    def test_search_dep_by_name(self, dep_name):
        # 测试group_tree的搜索功能
        GroupTree(dep_name[0]).search_dep_by_name(dep_name[1])

        # 断言搜索到的内容<前端缩略显示的>在dep_name字符串内
        result = GroupTree(dep_name[0]).judge_search_success(dep_name[1])
        # result = re.match('^[.]', result)
        assert result in dep_name[1]

    @pytest.mark.positive
    @pytest.mark.usefixtures("close_alert")
    def test_delete_peer_dep_from_Default(self, dep_name):
        UserPage(dep_name[0]).delete_department_by_name(parent_name=dep_name[1])

        result = UserPage(dep_name[0]).judge_alert_info()
        assert "删除分组成功" == result
