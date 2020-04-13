# -*- coding:utf-8 -*-
# @Time: 2020/4/13 19:48
# @Author: wenqin_zhu
# @File: com_dialog.py
# @Software: PyCharm

from selenium.webdriver.common.by import By
from guard.pages.basepage import BasePage


class CommDialog(BasePage):
    """ 通用：系统弹框 """

    def judge_alert_info(self):
        # 定位alert弹框的文本
        INFO_TEXT = (By.XPATH, '//div[@role="alert"]//p')
        # 强制等待元素可见
        BasePage(self.driver).wait_for_ele_to_be_visible(INFO_TEXT)
        return BasePage(self.driver).get_text(INFO_TEXT)

    def close_alert(self):
        # 关闭alert弹框
        CLOSE_BTN = (By.XPATH, '//div[@role="alert"]//i[contains(@class, "el-icon-close")]')
        BasePage(self.driver).click_ele(CLOSE_BTN)
