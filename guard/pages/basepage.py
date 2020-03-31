# -*- coding:utf-8 -*-
# @Time: 2020/3/26 18:52
# @Author: wenqin_zhu
# @File: basepage.py
# @Software: PyCharm

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.win_upload import upload


class BasePage:
    """  针对selenium框架中常用的元素操作进行二次封装 Basepage"""

    def __init__(self, driver: WebDriver):
        self.driver = driver
        # self.driver.maximize_window()

    def wait_for_ele_to_be_visible(self, loc, timeout=10, poll_frequency=0.5):
        """ 等待元素在页面中可见 """
        WebDriverWait(self.driver, timeout, poll_frequency).until(EC.visibility_of_element_located(loc))

    def wait_for_ele_to_be_presence(self, loc, timeout=20, poll_frequency=0.5):
        """ 等待元素在页面中存在"""
        WebDriverWait(self.driver, timeout, poll_frequency).until(EC.presence_of_element_located(loc))

    def get_ele_locator(self, loc):
        """ 获取元素 """
        return self.driver.find_element(*loc)

    def get_text(self, loc):
        """ 等待元素存在，获取文本内容 """
        self.wait_for_ele_to_be_presence(loc)
        ele = self.get_ele_locator(loc)
        return ele.text

    def update_input_text(self, loc, val):
        """ 文本框输入文本  等待元素可见并对文本框进行输入操作"""
        self.wait_for_ele_to_be_visible(loc)
        ele = self.get_ele_locator(loc)
        ele.send_keys(val)

    def upload_file(self, loc, val, flag=None, file_path=None, browser_type="chrome"):
        """ 文件上传 """
        if flag is None:
            # <input type=file /> input类型的上传操作
            ele = self.get_ele_locator(loc)
            ele.send_keys(val)
        elif flag == "win":
            # windows窗口 的文件上传 - 调用utils共用类进行上传操作
            upload(file_path, browser_type)

    def click_ele(self, loc):
        """ 点击元素，等待元素可见进行点击"""
        self.wait_for_ele_to_be_visible(loc)
        ele = self.get_ele_locator(loc)
        ele.click()
