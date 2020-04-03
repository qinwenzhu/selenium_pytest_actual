# -*- coding:utf-8 -*-
# @Time: 2020/3/26 18:52
# @Author: wenqin_zhu
# @File: basepage.py
# @Software: PyCharm

# 所有浏览器共用的 WebDriver 类
from selenium.webdriver.remote.webdriver import WebDriver
# 显性等待
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 鼠标操作 ActionChains
from selenium.webdriver.common.action_chains import ActionChains
# win系统的窗口上传封装的函数
from utils.win_upload import upload


class BasePage:

    """
    针对selenium框架中常用的元素操作进行二次封装 Basepage
    """

    def __init__(self, driver: WebDriver):
        # 传入 driver 实例化参数
        self.driver = driver

    def wait_for_ele_to_be_visible(self, loc, timeout=10, poll_frequency=0.5):
        """ 等待元素在页面中可见 """
        try:
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.visibility_of_element_located(loc))
        except TimeoutError:
            raise

    def wait_for_ele_to_be_presence(self, loc, timeout=20, poll_frequency=0.5):
        """ 等待元素在页面中存在"""
        try:
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.presence_of_element_located(loc))
        except TimeoutError:
            raise

    def get_ele_locator(self, loc):
        """ 获取元素 """
        try:
            ele = self.driver.find_element(*loc)
        except Exception:
            raise
        else:
            return ele

    def get_text(self, loc):
        """ 等待元素存在，获取文本内容 """
        try:
            ele = self.get_ele_locator(loc)
        except Exception:
            raise
        else:
            return ele.text

    def update_input_text(self, loc, val):
        """ 文本框输入文本  等待元素可见并对文本框进行输入操作"""
        try:
            self.wait_for_ele_to_be_visible(loc)
        except Exception:
            raise
        else:
            ele = self.get_ele_locator(loc)
            ele.send_keys(val)

    def upload_file(self, loc, val=None, flag=None, file_path=None, browser_type="chrome"):
        """
        文件上传
        :param loc: 元素定位
        :param val: input标签的type=file时传递的文件件路径
        :param flag: 判断是否是input标签的文件上传还是win系统的窗口上传
        :param file_path: win窗口上传的文件路径
        :param browser_type: win窗口上传的当前浏览器
        """
        if flag is None:
            try:
                # <input type=file /> input类型的上传操作
                ele = self.get_ele_locator(loc)
            except Exception:
                raise
            else:
                ele.send_keys(val)
        elif flag == "win":
            try:
                # windows窗口 的文件上传 - 调用utils共用类进行上传操作
                upload(file_path, browser_type)
            except Exception:
                print("文件路径不正确！")

    def click_ele(self, loc):
        """ 点击元素，等待元素可见进行点击"""
        try:
            self.wait_for_ele_to_be_visible(loc)
        except Exception:
            raise
        else:
            ele = self.get_ele_locator(loc)
            ele.click()

    def mouse_move_ele(self, loc):
        """  鼠标移动到指定元素上 """
        try:
            self.wait_for_ele_to_be_visible(loc)
        except Exception:
            raise
        else:
            ele = self.get_ele_locator(loc)
            ActionChains(self.driver).move_to_element(ele).perform()

    def mouse_move_ele_and_click(self, loc1, loc2, pause_time=0.2):
        """  鼠标移动到指定元素上并进行列表的点击操作 """
        try:
            self.wait_for_ele_to_be_visible(loc1)
            self.wait_for_ele_to_be_visible(loc2)
        except Exception:
            raise
        else:
            ele = self.get_ele_locator(loc1)
            sub_ele = self.get_ele_locator(loc2)
            ActionChains(self.driver).move_to_element(ele).pause(pause_time).click(sub_ele).perform()

    def scroll_visibility_region(self, loc):
        """  滚动到元素可见区域 """
        ele = self.get_ele_locator(loc)
        self.driver.execute_script("arguments[0].scrollIntoView();", ele)
