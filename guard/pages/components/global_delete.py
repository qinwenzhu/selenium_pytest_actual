# -*- coding:utf-8 -*-
# @Time: 2020/4/15 19:52
# @Author: wenqin_zhu
# @File: global_delete.py
# @Software: PyCharm

from guard.pages.basepage import BasePage
from selenium.webdriver.common.by import By


class GlobalDelete(BasePage):
    """ 通用：系统页面删除dialog """

    def dialog_delete(self, is_delete=True):

        if is_delete:
            # 点击删除按钮
            # //div[@class="el-dialog__header"]
            CONFIRM_BTN = (By.XPATH, '//button//span[contains(text(), "删除")]')
            BasePage(self.driver).click_ele(CONFIRM_BTN)
        else:
            # 点击取消按钮
            CONFIRM_BTN = (By.XPATH,
                           '//button//span[contains(text(), "取消")]')
            BasePage(self.driver).click_ele(CONFIRM_BTN)
