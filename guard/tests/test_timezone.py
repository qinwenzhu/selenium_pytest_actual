# -*- coding:utf-8 -*-
# @Time: 2020/4/13 14:19
# @Author: wenqin_zhu
# @File: test_timezone.py
# @Software: PyCharm

import re
import time
import pytest
from guard.pages.timezone import TimezonePage
from guard.pages.components.global_dialog import GlobalDialog


@pytest.mark.usefixtures("timezone_web")
class TestTimezone:

    @pytest.mark.positive
    def test_add_timezone(self, connect_mysql_and_close, timezone_web, timezone_name):
        # 测试添加时间条件
        TimezonePage(timezone_web).add_timezone_name(timezone_name)

        # 断言
        sql = "SELECT * FROM senseguard.info_time_zone WHERE time_zone_name=%s;"
        time.sleep(2)
        result = connect_mysql_and_close.select_database(sql, args=(timezone_name, ))
        print(f"数据库查询结果为：{result}")
        assert timezone_name == result["time_zone_name"]

    @pytest.mark.positive
    def test_add_timezone_section(self, connect_mysql_and_close, timezone_web, timezone_name):
        # 通过选择 指定的时间条件名称 创建时间段
        TimezonePage(timezone_web).add_timezone_section_by_timezone_name(timezone_name)

        # 断言
        result = TimezonePage(timezone_web).assert_timezone_section()
        assert re.match(r'\d+:\d+-\d+:\d', result)

    @pytest.mark.positive
    def test_create_holidays(self, connect_mysql_and_close, timezone_web, holiday_name):
        # 测试添加假期
        TimezonePage(timezone_web).create_holidays("添加假期", holiday_name, num=1)

        # 断言
        sql = "SELECT * FROM senseguard.info_holiday WHERE holiday_name=%s;"
        time.sleep(2)
        result = connect_mysql_and_close.select_database(sql, args=(holiday_name, ))
        print(f"数据库查询结果为：{result}")
        assert holiday_name == result["holiday_name"]

    @pytest.mark.positive
    def test_create_workday(self, connect_mysql_and_close, timezone_web, workday_name):
        # 测试添加特殊工作日
        TimezonePage(timezone_web).create_workday("添加特殊工作日", workday_name, num=1)

        # 断言
        sql = "SELECT * FROM senseguard.info_holiday WHERE holiday_name=%s;"
        time.sleep(2)
        result = connect_mysql_and_close.select_database(sql, args=(workday_name, ))
        print(f"数据库查询结果为：{result}")
        assert workday_name == result["holiday_name"]

    @pytest.mark.negative
    def test_add_timezone_and_beyond(self, timezone_web, sole_time_name):
        # 测试添加事件条件的超出指定字符长度
        TimezonePage(timezone_web).add_timezone_name(sole_time_name)

        # 断言
        result = GlobalDialog(timezone_web).judge_alert_info()
        assert "请输入最多40个字符的时间条件名称" == result

    @pytest.mark.negative
    def test_add_holidays_negative_conflict(self, timezone_web, sole_short_time_name):
        # 测试添加假期与页面现有的假期时间冲突
        TimezonePage(timezone_web).create_holidays("添加假期", sole_short_time_name)

        # 断言
        result = GlobalDialog(timezone_web).judge_alert_info()
        assert "创建的假期与已有的假期有冲突，请检查后重新设置" == result

    @pytest.mark.negative
    def test_add_workday_negative_conflict(self, timezone_web, sole_short_time_name):
        # 测试添加特殊工作日与页面现有的工作日时间冲突
        TimezonePage(timezone_web).create_workday("添加特殊工作日", sole_short_time_name)

        # 断言
        result = GlobalDialog(timezone_web).judge_alert_info()
        assert "创建的特殊工作日与已有的特殊工作日有冲突，请检查后重新设置" == result
