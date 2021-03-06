# -*- coding:utf-8 -*-
# @Time: 2020/3/26 11:34
# @Author: wenqin_zhu
# @File: test_tool.py
# @Software: PyCharm

import time
import pytest
import re
from guard.pages.classes.share_path import SharePath
from guard.datas.tool.tool_data import FacePropertyData as FPD
from guard.pages.components.menubar import MenubarPage
from guard.pages.tool import ToolPage
from guard.pages.components.global_dialog import GlobalDialog


@pytest.mark.usefixtures("login_web")
class TestTool:

    @pytest.mark.positive
    @pytest.mark.usefixtures("tool_close_one_to_one_face_compare")
    def test_one_to_one_face_compare(self, login_web):
        """ 测试1:1人脸验证功能 """
        MenubarPage(login_web).click_nav_item("工具", "1:1人脸验证")
        ToolPage(login_web).one_to_one_face_compare(r"{}/tool/img_one_to_one/img1.jpg".format(SharePath.DATA_FOLDER), r"{}/tool/img_one_to_one/img2.jpg".format(SharePath.DATA_FOLDER))

        result = ToolPage(login_web).get_face_compare_result()
        assert '评分参考' == result

    @pytest.mark.positive
    @pytest.mark.parametrize("data", FPD.score_detection_data_negative)
    @pytest.mark.usefixtures("tool_close_one_img_quality")
    def test_score_detection(self, login_web, data):
        """ 测试人脸质量分数检测功能 """
        MenubarPage(login_web).click_nav_item("工具", "质量分数检测")
        ToolPage(login_web).check_one_img_quality(r'{}/tool/img_score_detection/{}'.format(SharePath.DATA_FOLDER, data["img_path"]))

        result = ToolPage(login_web).get_face_score_detection_result()
        assert re.match(r'\d+ .\d+%', result)

    @pytest.mark.negative
    @pytest.mark.usefixtures("tool_close_one_img_quality")
    def test_negative_score_detection(self, login_web):
        """ 测试上传大于16M的图片 - 系统支持上传小于16M的图片 """
        MenubarPage(login_web).click_nav_item("工具", "质量分数检测")
        time.sleep(3)
        ToolPage(login_web).check_one_img_quality(f"{SharePath.DATA_FOLDER}/tool/img_score_detection/size_greater_16M.jpg")

        result = GlobalDialog(login_web).judge_alert_info()
        assert "上传图片大小不能超过 16MB!" in result

    @pytest.mark.positive
    @pytest.mark.usefixtures("tool_close_face_score_detection")
    def test_face_property(self, login_web):
        """ 测试人脸属性输出的属性字段 """
        MenubarPage(login_web).click_nav_item("工具", "人脸属性检测")
        ToolPage(login_web).check_face_property(f'{SharePath.DATA_FOLDER}/tool/img_face_property/normal.jpg')

        face_sex = ToolPage(login_web).get_facial_attribute_by_name("性别")
        face_age = ToolPage(login_web).get_facial_attribute_by_name("年龄")
        face_phiz = ToolPage(login_web).get_facial_attribute_by_name("表情")
        face_mustache = ToolPage(login_web).get_facial_attribute_by_name("胡子")
        face_glasse = ToolPage(login_web).get_facial_attribute_by_name("眼镜")
        face_mask = ToolPage(login_web).get_facial_attribute_by_name("口罩")
        face_helmet = ToolPage(login_web).get_facial_attribute_by_name("安全帽")
        face_hat = ToolPage(login_web).get_facial_attribute_by_name("帽子")

        assert ("性别" in face_sex) and ("年龄" in face_age) and ("表情" in face_phiz) and ("胡子" in face_mustache) and (
                    "眼镜" in face_glasse) and ("口罩" in face_mask) and ("安全帽" in face_helmet) and ("帽子" in face_hat)

    @pytest.mark.negative
    @pytest.mark.usefixtures("tool_close_face_score_detection")
    @pytest.mark.parametrize("data", FPD.face_data_negative)
    def test_negative_face_property(self, login_web, data):
        """ 测试上传不同属性的人脸照片检测出对应的人脸属性 """
        MenubarPage(login_web).click_nav_item("工具", "人脸属性检测")
        ToolPage(login_web).check_face_property(f'{SharePath.DATA_FOLDER}/tool/img_face_property/{data["img_path"]}')

        face_sex = ToolPage(login_web).get_facial_attribute_by_name("性别")
        face_age = ToolPage(login_web).get_facial_attribute_by_name("年龄")
        face_phiz = ToolPage(login_web).get_facial_attribute_by_name("表情")
        face_mustache = ToolPage(login_web).get_facial_attribute_by_name("胡子")
        face_glasse = ToolPage(login_web).get_facial_attribute_by_name("眼镜")
        face_mask = ToolPage(login_web).get_facial_attribute_by_name("口罩")
        face_helmet = ToolPage(login_web).get_facial_attribute_by_name("安全帽")
        face_hat = ToolPage(login_web).get_facial_attribute_by_name("帽子")

        assert (data["sex"] in face_sex) and (data["age"] in face_age) and (data["phiz"] in face_phiz) and (
                data["mustache"] in face_mustache) and (data["glasse"] in face_glasse) and (
                       data["mask"] in face_mask) and (data["helmet"] in face_helmet) and (data["hat"] in face_hat)


if __name__ == '__main__':
    pytest.main()
