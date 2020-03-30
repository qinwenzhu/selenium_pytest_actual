# -*- coding:utf-8 -*-
# @Time: 2020/3/26 11:34
# @Author: wenqin_zhu
# @File: test_tools.py
# @Software: PyCharm


import pytest

# 导入正则表达式
import re

from guard.tests.path import CommonPath
from guard.data.face_property.face_property_data import FacePropertyData as FPD

from guard.pages.components.menubar import MenubarPage
from guard.pages.tool import ToolPage


@pytest.mark.usefixtures("web_login_and_quit")
class TestTool:

    @pytest.mark.positive
    def test_one_to_one_face_compare(self, web_login_and_quit, tool_close_one_to_one_face_compare):
        """ 测试1:1人脸验证功能 """
        MenubarPage(web_login_and_quit).click_nav_item("工具", "1:1人脸验证")
        ToolPage(web_login_and_quit).one_to_one_face_compare(f"{CommonPath.DATA_FOLDER}/face_property/have_glasse.jpg",
                                                           f"{CommonPath.DATA_FOLDER}/face_property/woman_no_mustache_no_glasse_no_mask.jpg")
        result = ToolPage(web_login_and_quit).get_face_compare_result()
        assert '评分参考' == result

    # @pytest.mark.positive
    # def test_score_detection(self, web_login_and_quit, tool_close_one_img_quality):
    #     """ 测试人脸质量分数检测功能 """
    #     MenubarPage(web_login_and_quit).click_nav_item("工具", "质量分数检测")
    #     ToolPage(web_login_and_quit).check_one_img_quality(f"{CommonPath.DATA_FOLDER}/face_property/have_glasse.jpg")
    #
    #     result = ToolPage(web_login_and_quit).get_face_score_detection_result()
        # assert re.match(r'\d+.\d+%', result)

    @pytest.mark.positive
    def test_face_property(self, web_login_and_quit, tool_close_face_score_detection):
        """ 测试人脸属性输出的属性字段 """
        MenubarPage(web_login_and_quit).click_nav_item("工具", "人脸属性检测")
        ToolPage(web_login_and_quit).check_face_property(f'{CommonPath.DATA_FOLDER}/face_property/seleniumbase.jpg')
        face_sex = ToolPage(web_login_and_quit).get_face_result_sex()
        face_age = ToolPage(web_login_and_quit).get_face_result_age()
        face_phiz = ToolPage(web_login_and_quit).get_face_result_phiz()
        face_mustache = ToolPage(web_login_and_quit).get_face_result_mustache()
        face_glasse = ToolPage(web_login_and_quit).get_face_result_glasse()
        face_mask = ToolPage(web_login_and_quit).get_face_result_mask()
        face_helmet = ToolPage(web_login_and_quit).get_face_result_helmet()
        face_hat = ToolPage(web_login_and_quit).get_face_result_hat()

        assert "性别" in face_sex
        assert "年龄" in face_age
        assert "表情" in face_phiz
        assert "胡子" in face_mustache
        assert "眼镜" in face_glasse
        assert "口罩" in face_mask
        assert "安全帽" in face_helmet
        assert "帽子" in face_hat

    @pytest.mark.parametrize("data", FPD.face_data_negative)
    @pytest.mark.negative
    def test_negative_face_property(self, web_login_and_quit, tool_close_face_score_detection, data):
        """ 测试上传不同属性的人脸照片检测出对应的人脸属性 """
        MenubarPage(web_login_and_quit).click_nav_item("工具", "人脸属性检测")
        ToolPage(web_login_and_quit).check_face_property(f'{CommonPath.DATA_FOLDER}/face_property/{data["img_path"]}')
        face_sex = ToolPage(web_login_and_quit).get_face_result_sex()
        face_age = ToolPage(web_login_and_quit).get_face_result_age()
        face_phiz = ToolPage(web_login_and_quit).get_face_result_phiz()
        face_mustache = ToolPage(web_login_and_quit).get_face_result_mustache()
        face_glasse = ToolPage(web_login_and_quit).get_face_result_glasse()
        face_mask = ToolPage(web_login_and_quit).get_face_result_mask()
        face_helmet = ToolPage(web_login_and_quit).get_face_result_helmet()
        face_hat = ToolPage(web_login_and_quit).get_face_result_hat()

        assert data["sex"] in face_sex
        assert data["age"] in face_age
        assert data["phiz"] in face_phiz
        assert data["mustache"] in face_mustache
        assert data["glasse"] in face_glasse
        assert data["mask"] in face_mask
        assert data["helmet"] in face_helmet
        assert data["hat"] in face_hat


if __name__ == '__main__':
    pytest.main()

