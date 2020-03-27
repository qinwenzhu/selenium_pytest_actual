# -*- coding:utf-8 -*-
# @Time: 2020/3/26 11:34
# @Author: wenqin_zhu
# @File: test_tools.py
# @Software: PyCharm

import pytest
import os

from guard.tests.path import CommonPath

from guard.pages.components.menubar import MenubarPage
from guard.pages.tool import ToolPage


@pytest.mark.usefixtures("web_login_and_quit")
class TestTool:

    def test_check_all_face_property(self, web_login_and_quit):
        """ 测试人脸属性输出的属性字段 """
        MenubarPage(web_login_and_quit).click_nav_item("工具", "人脸属性检测")
        ToolPage(web_login_and_quit).check_face_property(f'{CommonPath.DATA_FOLDER}/face_property/seleniumbase.jpg')


        # sex_data = Tools.get_check_result_sex(sb)
        # age_data = Tools.get_check_result_age(sb)
        # phiz_data = Tools.get_check_result_phiz(sb)
        # mustache_data = Tools.get_check_result_mustache(sb)
        # glasse_data = Tools.get_check_result_glasse(sb)
        # mask_data = Tools.get_check_result_mask(sb)
        # helmet_data = Tools.get_check_result_helmet(sb)
        # hat_data = Tools.get_check_result_hat(sb)
        #
        # assert '性别:' == sex_data[0]
        # assert '年龄:' == age_data[0]
        # assert '表情:' == phiz_data[0]
        # assert '胡子:' == mustache_data[0]
        # assert '眼镜:' == glasse_data[0]
        # assert '口罩:' == mask_data[0]
        # assert '安全帽:' == helmet_data[0]
        # assert '帽子:' == hat_data[0]


if __name__ == '__main__':
    pytest.main()

