# -*- coding:utf-8 -*-
# @Time: 2020/3/24 19:46
# @Author: wenqin_zhu
# @File: tool.py
# @Software: PyCharm


from selenium.webdriver.common.by import By

from guard.pages.basepage import BasePage


class ToolPage(BasePage):

    def check_face_property(self, path):
        """ 人脸属性检测 """

        # 图片上传按钮
        IMAGE_UPLOAD_INPUT = (By.CSS_SELECTOR, 'input[type="file"]')
        BasePage(self.driver).upload_file(IMAGE_UPLOAD_INPUT, path)

        # 点击检测
        CHECK_CONTENT_FACE_BUTTON = (By.CSS_SELECTOR, '.app-tools-content-face-detectbtn')
        BasePage(self.driver).click_ele(CHECK_CONTENT_FACE_BUTTON)

    def get_check_result_sex(self):
        CHECK_CONTENT_FACE_RESULT = '//div[@class="app-tools-content-detection-right"]//li[1]//span'
        CHECK_CONTENT_SEX = '//div[@class="app-tools-content-detection-right"]//li[1]'
        BasePage(self.driver).get_ele_locator(CHECK_CONTENT_FACE_RESULT)
        self.find_element(CHECK_CONTENT_FACE_RESULT, By.XPATH)
        self.find_element(CHECK_CONTENT_SEX, By.XPATH)
        data_text = [self.get_text(CHECK_CONTENT_FACE_RESULT), self.get_text(CHECK_CONTENT_SEX)]
        return data_text
    #
    # def get_check_result_age(self):
    #     CHECK_CONTENT_FACE_RESULT = '//div[@class="app-tools-content-detection-right"]//li[2]//span'
    #     CHECK_CONTENT_AGE = '//div[@class="app-tools-content-detection-right"]//li[2]'
    #     self.find_element(CHECK_CONTENT_FACE_RESULT, By.XPATH)
    #     self.find_element(CHECK_CONTENT_AGE, By.XPATH)
    #     data_text = [self.get_text(CHECK_CONTENT_FACE_RESULT), self.get_text(CHECK_CONTENT_AGE)]
    #     return data_text
    #
    # def get_check_result_phiz(self):
    #     CHECK_CONTENT_FACE_RESULT = '//div[@class="app-tools-content-detection-right"]//li[3]//span'
    #     CHECK_CONTENT_PHIZ = '//div[@class="app-tools-content-detection-right"]//li[3]'
    #     self.find_element(CHECK_CONTENT_FACE_RESULT, By.XPATH)
    #     self.find_element(CHECK_CONTENT_PHIZ, By.XPATH)
    #     data_text = [self.get_text(CHECK_CONTENT_FACE_RESULT), self.get_text(CHECK_CONTENT_PHIZ)]
    #     return data_text
    #
    # def get_check_result_mustache(self):
    #     CHECK_CONTENT_FACE_RESULT = '//div[@class="app-tools-content-detection-right"]//li[4]//span'
    #     CHECK_CONTENT_MUSTACHE = '//div[@class="app-tools-content-detection-right"]//li[4]'
    #     self.find_element(CHECK_CONTENT_FACE_RESULT, By.XPATH)
    #     self.find_element(CHECK_CONTENT_MUSTACHE, By.XPATH)
    #     data_text = [self.get_text(CHECK_CONTENT_FACE_RESULT), self.get_text(CHECK_CONTENT_MUSTACHE)]
    #     return data_text
    #
    # def get_check_result_glasse(self):
    #     CHECK_CONTENT_FACE_RESULT = '//div[@class="app-tools-content-detection-right"]//li[5]//span'
    #     CHECK_CONTENT_GLASSE = '//div[@class="app-tools-content-detection-right"]//li[5]'
    #     self.find_element(CHECK_CONTENT_FACE_RESULT, By.XPATH)
    #     self.find_element(CHECK_CONTENT_GLASSE, By.XPATH)
    #     data_text = [self.get_text(CHECK_CONTENT_FACE_RESULT), self.get_text(CHECK_CONTENT_GLASSE)]
    #     return data_text
    #
    # def get_check_result_mask(self):
    #     CHECK_CONTENT_FACE_RESULT = '//div[@class="app-tools-content-detection-right"]//li[6]//span'
    #     CHECK_CONTENT_MASK = '//div[@class="app-tools-content-detection-right"]//li[6]'
    #     self.find_element(CHECK_CONTENT_FACE_RESULT, By.XPATH)
    #     self.find_element(CHECK_CONTENT_MASK, By.XPATH)
    #     data_text = [self.get_text(CHECK_CONTENT_FACE_RESULT), self.get_text(CHECK_CONTENT_MASK)]
    #     return data_text
    #
    # def get_check_result_helmet(self):
    #     CHECK_CONTENT_FACE_RESULT = '//div[@class="app-tools-content-detection-right"]//li[7]//span'
    #     CHECK_CONTENT_HELMET = '//div[@class="app-tools-content-detection-right"]//li[7]'
    #     self.find_element(CHECK_CONTENT_FACE_RESULT, By.XPATH)
    #     self.find_element(CHECK_CONTENT_HELMET, By.XPATH)
    #     data_text = [self.get_text(CHECK_CONTENT_FACE_RESULT), self.get_text(CHECK_CONTENT_HELMET)]
    #     return data_text
    #
    # def get_check_result_hat(self):
    #     CHECK_CONTENT_FACE_RESULT = '//div[@class="app-tools-content-detection-right"]//li[8]//span'
    #     CHECK_CONTENT_HAT = '//div[@class="app-tools-content-detection-right"]//li[8]'
    #     self.find_element(CHECK_CONTENT_FACE_RESULT, By.XPATH)
    #     self.find_element(CHECK_CONTENT_HAT, By.XPATH)
    #     data_text = [self.get_text(CHECK_CONTENT_FACE_RESULT), self.get_text(CHECK_CONTENT_HAT)]
    #     return data_text

    # # 1:1人脸验证
    # def check_face_validation(self, path1, path2):
    #     IMAGE_UPLOAD_INPUT_L = '.app-tools-content-pics .imageselsect-container:first-child > input[type="file"]'
    #     IMAGE_UPLOAD_INPUT_R = '.app-tools-content-pics .imageselsect-container:last-child > input[type="file"]'
    #
    #     BasePage.upload_file_by_image_path(self, IMAGE_UPLOAD_INPUT_L, path1)
    #     self.sleep(1)
    #     BasePage.upload_file_by_image_path(self, IMAGE_UPLOAD_INPUT_R, path2)
    #     self.sleep(3)
    #     CHECK_CONTENT_FACE_BUTTON = '.app-tools-content-pics-vsbtn'
    #     self.slow_click(CHECK_CONTENT_FACE_BUTTON)
    #
    # def get_check_face_result(self):
    #     CHECK_CONTENT = '.app-tools-content-pics-vsbtn-popover > strong'
    #     self.find_element(CHECK_CONTENT)
    #     return self.get_text(CHECK_CONTENT)

    # # 质量分数检测
    # def check_image_quality(self, path):
    #     IMAGE_UPLOAD_INPUT = 'input[type="file"]'
    #     BasePage.upload_file_by_image_path(self, IMAGE_UPLOAD_INPUT, path)
    #
    #     CHECK_CONTENT_DETECTION_BUTTON = '.app-tools-content-detection-detectbtn'
    #     self.slow_click(CHECK_CONTENT_DETECTION_BUTTON)
    #
    # def get_check_content_detection_result(self):
    #     CHECK_CONTENT_DETECTION_BUTTON_RESULT = '.app-tools-content-detection-detectbtn > span'
    #     CHECK_CONTENT_DETECTION_RESULT = '.app-tools-content-detection-detectresult'
    #     self.find_element(CHECK_CONTENT_DETECTION_RESULT)
    #     return self.get_text(CHECK_CONTENT_DETECTION_BUTTON_RESULT)


if __name__ == '__main__':
    # 读取配置文件
    # SSH_CONFIG_FILE = HandleConfig('../config/ssh_config.yml').config
    # print(SSH_CONFIG_FILE)

    from selenium import webdriver

    driver = webdriver.Chrome()
    # driver.get("http://10.151.3.96/login")
    # LoginPage(driver).login("zhuwenqin", "888888")
    # LoginPage(driver).get_captcha_from_k8s_log()
