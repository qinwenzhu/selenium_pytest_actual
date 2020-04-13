# -*- coding:utf-8 -*-
# @Time: 2020/4/13 14:19
# @Author: wenqin_zhu
# @File: test_timezone.py
# @Software: PyCharm
import time

import pytest

from guard.pages.timezone import TimezonePage
from guard.tools.call_database import query_result_by_database
from guard.pages.components.global_dialog import GlobalDialog


@pytest.mark.usefixtures("timezone_web")
class TestTimezone:

    @pytest.mark.positive
    def test_add_timezone(self, timezone_web, sole_short_time_name):
        # 测试添加时间条件
        TimezonePage(timezone_web).add_timezone_name(sole_short_time_name)

        print(sole_short_time_name)
        # 断言
        sql = "SELECT * FROM senseguard.info_time_zone WHERE time_zone_name=%s;"
        result = query_result_by_database(sql, args=(sole_short_time_name, ))
        print(f"数据库查询结果为：{result}")
        # time.sleep(10)
        assert sole_short_time_name in result["time_zone_name"]

    @pytest.mark.positive
    def test_create_holidays(self, timezone_web, sole_time_name):
        # 测试添加假期
        TimezonePage(timezone_web).create_holidays("添加假期", sole_time_name)

        # 断言
        # sql = "SELECT * FROM senseguard.info_time_zone WHERE time_zone_name=%s;"
        # result = query_result_by_database(sql, args=(sole_time_name,))
        # print(f"数据库查询结果为：{result}")
        # # time.sleep(10)
        # assert sole_time_name in result["time_zone_name"]

    @pytest.mark.positive
    def test_create_workday(self, timezone_web, sole_time_name):
        # 测试添加特殊工作日
        TimezonePage(timezone_web).create_workday("添加特殊工作日", sole_time_name)

        # 断言
        # sql = "SELECT * FROM senseguard.info_time_zone WHERE time_zone_name=%s;"
        # result = query_result_by_database(sql, args=(sole_time_name,))
        # print(f"数据库查询结果为：{result}")
        # # time.sleep(10)
        # assert sole_time_name in result["time_zone_name"]

    @pytest.mark.negative
    def test_add_timezone_and_beyond(self, timezone_web, sole_time_name):
        # 测试添加事件条件的超出指定字符长度
        TimezonePage(timezone_web).add_timezone_name(sole_time_name)

        result = GlobalDialog(timezone_web).judge_alert_info()
        # 断言
        assert "请输入最多40个字符的时间条件名称" == result
