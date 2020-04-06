# -*- coding:utf-8 -*-
# @Time: 2020/3/26 18:52
# @Author: wenqin_zhu
# @File: basepage.py
# @Software: PyCharm

# 导入日期
from datetime import datetime
# 所有浏览器共用的 WebDriver 类
from selenium.webdriver.remote.webdriver import WebDriver
# 导入显性等待
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 鼠标操作 ActionChains
from selenium.webdriver.common.action_chains import ActionChains
# 自定义 - win系统的窗口上传
from utils.win_upload import upload
# 自定义 - 导入日志
from utils.handle_log import HandleLog
# 自定义 - 导入公共路径
from guard.tests.path import CommonPath


# Basepage - 针对selenium框架中常用的元素操作进行二次封装
class BasePage:

    def __init__(self, driver: WebDriver):
        # 传入 driver - 指定类型为：WebDriver
        self.driver = driver
        self.log = HandleLog(r"{}/log.txt".format(CommonPath.LOG_FOLDER)).get_log()

    def wait_for_ele_to_be_visible(self, loc, img_describe="current", timeout=10, poll_frequency=0.5):
        """ 等待元素在页面中可见 """

        self.log.info(f"等待元素可见：{img_describe}页面的-{loc[-1]}元素")
        try:
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.visibility_of_element_located(loc))
        except TimeoutError:
            # 对当前页面进行截图
            self.save_web_screenshots(img_describe)
            self.log.info(f"等待元素可见失败!")
            raise

    def wait_for_ele_to_be_presence(self, loc, img_describe="current", timeout=10, poll_frequency=0.5):
        """ 等待元素在页面中存在"""

        self.log.info(f"等待元素存在：{img_describe}页面的-{loc[-1]}元素")
        try:
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.presence_of_element_located(loc))
        except TimeoutError:
            self.save_web_screenshots(img_describe)
            self.log.info(f"等待元素存在失败!")
            raise

    def get_ele_locator(self, loc, img_describe="current"):
        """ 获取元素 """

        self.log.info(f"获取元素定位：{img_describe}页面的{loc[-1]}元素")
        try:
            ele = self.driver.find_element(*loc)
        except Exception:
            self.save_web_screenshots(img_describe)
            self.log.info(f"元素定位失败！")
            raise
        else:
            return ele

    def get_text(self, loc, img_describe="current"):
        """ 获取元素的文本内容  前提：元素存在 """

        self.log.info(f"获取元素文本：{img_describe}页面的{loc[-1]}元素")
        try:
            self.wait_for_ele_to_be_presence(loc, img_describe)
        except Exception:
            self.save_web_screenshots(img_describe)
            self.log.info(f"获取元素文本失败！")
            raise
        else:
            ele = self.get_ele_locator(loc, img_describe)
            return ele.text

    def get_ele_attribute(self, loc, attr, img_describe="current"):
        """ 获取元素的属性  前提：元素存在 """

        self.log.info(f"获取元素属性：{img_describe}页面的{loc[-1]}元素")
        try:
            self.wait_for_ele_to_be_presence(loc, img_describe)
        except Exception:
            self.save_web_screenshots(img_describe)
            self.log.info(f"获取元素属性失败！")
            raise
        else:
            ele = self.get_ele_locator(loc, img_describe)
            return ele.get_attribute(attr)

    def update_input_text(self, loc, val, img_describe="current"):
        """ 文本框输入文本  前提：元素可见 """

        self.log.info(f"文本框输入文本：{img_describe}页面的{loc[-1]}元素")
        try:
            self.wait_for_ele_to_be_visible(loc, img_describe)
        except Exception:
            self.save_web_screenshots(img_describe)
            self.log.info(f"文本框输入文本失败！")
            raise
        else:
            ele = self.get_ele_locator(loc, img_describe)
            ele.send_keys(val)

    def upload_file(self, loc, filename=None, img_describe="current", flag=True, file_path=None, browser_type="chrome"):
        """
        文件上传
        :param loc: 元素定位
        :param val: input标签的type=file时传递的文件路径
        :param flag: 判断是否是input标签的文件上传还是win系统的窗口上传，默认True为input文件上传
        :param file_path: win窗口上传的文件路径
        :param browser_type: win窗口上传时打开的当前浏览器
        """

        self.log.info(f"文件上传：{img_describe}页面的-{loc[-1]}元素")
        if flag:
            try:
                # <input type=file /> input类型的上传操作
                ele = self.get_ele_locator(loc, img_describe)
            except Exception:
                self.save_web_screenshots(img_describe)
                self.log.info(f"文本上传失败！")
                raise
            else:
                # 进行文件上传
                ele.send_keys(filename)
        else:
            try:
                # windows窗口 的文件上传 - 调用utils共用类进行上传操作
                upload(file_path, browser_type)
            except Exception:
                self.save_web_screenshots(img_describe)
                self.log.info(f"文本上传失败！")
                raise

    def click_ele(self, loc, img_describe="current"):
        """ 点击元素，等待元素可见进行点击"""

        self.log.info(f"点击元素：{img_describe}页面的-{loc[-1]}元素")
        try:
            self.wait_for_ele_to_be_visible(loc, img_describe)
        except Exception:
            self.save_web_screenshots(img_describe)
            self.log.info(f"点击元素失败！")
            raise
        else:
            ele = self.get_ele_locator(loc, img_describe)
            ele.click()

    def mouse_move_ele(self, loc, img_describe="current"):
        """  鼠标移动到指定元素上 """

        self.log.info(f"鼠标移动到指定元素：{img_describe}页面的-{loc[-1]}元素")
        try:
            self.wait_for_ele_to_be_visible(loc, img_describe)
        except Exception:
            self.save_web_screenshots(img_describe)
            self.log.info(f"鼠标移动到元素失败！")
            raise
        else:
            ele = self.get_ele_locator(loc, img_describe)
            ActionChains(self.driver).move_to_element(ele).perform()

    def mouse_move_ele_and_click(self, loc1, loc2, pause_time=1, img_describe="current"):
        """  鼠标移动到指定元素上并进行列表的点击操作 """

        self.log.info(f"{img_describe}页面：鼠标移动到父级元素{loc1[-1]},操作子元素{loc2[-1]}元素")
        try:
            self.wait_for_ele_to_be_visible(loc1, img_describe)
            self.wait_for_ele_to_be_visible(loc2, img_describe)
        except Exception:
            self.save_web_screenshots(img_describe)
            self.log.info(f"鼠标移动到元素失败！")
            raise
        else:
            # 滑动到父元素
            ele = self.get_ele_locator(loc1, img_describe)
            # 操作列表中的子元素
            sub_ele = self.get_ele_locator(loc2, img_describe)
            ActionChains(self.driver).move_to_element(ele).pause(pause_time).click(sub_ele).perform()

    # def scroll_visibility_region(self, loc, img_describe="current"):
    #     """  滚动到元素可见区域 """
    #
    #     ele = self.get_ele_locator(loc, img_describe)
    #     self.driver.execute_script("arguments[0].scrollIntoView();", ele)

    def save_web_screenshots(self, img_describe):
        current_time_to_str = datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')
        file_name = f"{img_describe}_{current_time_to_str}.jpg"
        self.driver.save_screenshot(f"{CommonPath.SCREENSHOT_FOLDER}/{file_name}")
        self.log.info(f"页面截图保存位置：{file_name}")
