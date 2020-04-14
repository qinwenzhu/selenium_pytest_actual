# -*- coding:utf-8 -*-
# @Time: 2020/4/10 16:09
# @Author: wenqin_zhu
# @File: timezone.py
# @Software: PyCharm
import time

from selenium.webdriver.common.by import By

from guard.pages.basepage import BasePage


class TimezonePage(BasePage):

    def dialog_info_com(self, til_name, val, confirm=True):
        """
        封装dialog弹框
        :param til_name: 弹框标题
        :param val: 传入input输入框值
        :param confirm: dialog按钮选项。默认确定
        """

        INPUT_TEXT = (By.XPATH, f'//div[@class="timezone-rename-dialog-header"]//span[contains(text(), "{til_name}")]/ancestor::div[@class="el-dialog__header"]/following-sibling::div[@class="el-dialog__body"]//input')
        BasePage(self.driver).update_input_text(INPUT_TEXT, val, img_describe="时间条件")

        if confirm:
            CONFIRM_BUTTON = (By.XPATH,
                              f'//div[@class="timezone-rename-dialog-header"]//span[contains(text(), "{til_name}")]/ancestor::div[@class="el-dialog__header"]/following-sibling::div[@class="el-dialog__footer"]//span[contains(text(), "确定")]')
            BasePage(self.driver).click_ele(CONFIRM_BUTTON)
        else:
            CANCEL_BUTTON = (By.XPATH,
                             f'//div[@class="timezone-rename-dialog-header"]//span[contains(text(), "{til_name}")]/ancestor::div[@class="el-dialog__header"]/following-sibling::div[@class="el-dialog__footer"]//span[contains(text(), "取消")]')
            BasePage(self.driver).click_ele(CANCEL_BUTTON)

    def check_time(self):
        """ 封装时间控件 """

        # 定位到时间控件并通过鼠标操作
        TIME_CONTROL = (By.XPATH, '//div[contains(@class, "el-date-range-picker") and contains(@style, "position")]//td[contains(@class, "today")]')
        BasePage(self.driver).mouse_move_ele(TIME_CONTROL)

        # 滑动时间控件点击对应的日期
        TIME_TODAY = (By.XPATH, '//div[contains(@class, "el-date-range-picker") and contains(@style, "position")]//div[contains(@class,"is-left")]//td[contains(@class, "today")]')
        BasePage(self.driver).mouse_move_ele_and_click(TIME_CONTROL, TIME_TODAY)

        TODAY_TEXT = (By.XPATH, '//div[contains(@class, "el-date-range-picker") and contains(@style, "position")]//div[contains(@class,"is-left")]//td[contains(@class, "today")]//span')
        today_text = BasePage(self.driver).get_text(TODAY_TEXT)
        if int(today_text) >= 28:
            # 结束时间为下月1号
            today_text = "1"
            TIME_END = (By.XPATH, f'//div[contains(@class, "el-date-range-picker") and contains(@style, "position")]//div[contains(@class,"is-right")]//td//span[contains(text(),{today_text})]')
        else:
            # 结束时间为今天的后两天
            today_text = str(int(today_text)+2)
            # 默认选择结束时间为 day+2
            TIME_END = (By.XPATH, f'//div[contains(@class, "el-date-range-picker") and contains(@style, "position")]//div[contains(@class,"is-left")]//td//span[contains(text(),{today_text})]')
        BasePage(self.driver).mouse_move_ele_and_click(TIME_CONTROL, TIME_END)

    def operation_timezone_by_name(self, name, flag):
        """
        通过时间条件名称 重命名/删除 该条记录
        :param name: 当前选择的名称，包括：时间条件名称、假期、特殊工作日
        :param flag: 判断是 重命名还是删除
        """
        # 定位时间条件名称定位表达式
        SELECT_TIMEZONE = (By.XPATH, f'//div[@role="tablist"]//button/span[contains(text(), "{name}")]')
        BasePage(self.driver).mouse_move_ele(SELECT_TIMEZONE)

        if flag == "重命名":
            ELE_LOC = (By.XPATH,
                       '//div[@role="tooltip"  and contains(@style, "position")]//span[contains(text(), "重命名")]')
            BasePage(self.driver).mouse_move_ele(SELECT_TIMEZONE, ELE_LOC)

            # 执行重命名操作
            self.dialog_info_com("重命名时间条件", "UPDATE" + name)

        elif flag == "删除":
            ELE_LOC = (By.XPATH,
                       '//div[@role="tooltip"  and contains(@style, "position")]//span[contains(text(), "删除")]')
            BasePage(self.driver).mouse_move_ele(SELECT_TIMEZONE, ELE_LOC)

            # TODO 执行删除操作
            # 删除

    def add_timezone_name(self, val):
        """
        添加时间条件
        :param val: 时间条件的名称
        """
        # icon的识别率不高，强制等待2s
        time.sleep(2)
        # 定位到添加时间条件的按钮
        ICON = (By.XPATH, '//span[contains(text(), "时间条件名称")]/i')
        BasePage(self.driver).click_ele(ICON)

        # 调用封装方法 - 添加时间条件名称
        self.dialog_info_com("添加时间条件", val)

    def add_timezone_section_by_timezone_name(self, timezone_name):
        """ 添加时间段 """

        # 定位时间条件名称定位表达式
        SELECT_TIMEZONE = (By.XPATH, f'//div[@role="tablist"]//button/span[contains(text(), "{timezone_name}")]')

        # 元素滚动到页面可见区域
        BasePage(self.driver).scroll_visibility_region(SELECT_TIMEZONE)
        time.sleep(5)
        # ele = BasePage(self.driver).get_ele_locator(SELECT_TIMEZONE)
        # self.driver.execute_script("arguments[0].scrollIntoView();", ele)
        # BasePage(self.driver).click_ele(SELECT_TIMEZONE)

        # 选择指定的时间条件添加对应的时间段
        ICON = (By.XPATH, '//span[contains(text(), "时间段")]/i')
        BasePage(self.driver).click_ele(ICON)

    def create_holidays(self, tile_name, val):
        """
        添加假期
        :param tile_name: 动态传入定位表达式的标题名称
        :param val: 假期名称
        """

        # 点击 - 未定义假期 - 按钮
        SET_HOLIDAY = (By.XPATH, '//span[contains(text(), "未定义假期")]')
        BasePage(self.driver).click_ele(SET_HOLIDAY)

        # 调用封装方法 - 添加假期
        self.dialog_info_com(tile_name, val)
        # 点击 - 设定日期 - 按钮
        SET_TIME = (By.XPATH, '//header[contains(text(), "假期定义")]/following-sibling::div//span[contains(text(), "设定日期")]')
        BasePage(self.driver).click_ele(SET_TIME)
        # 调用封装方法 - 选择假期的时间区间
        self.check_time()

    def create_workday(self, tile_name, val):
        """
        添加特殊工作日
        :param tile_name: 动态传入定位表达式的标题名称
        :param val: 特殊工作日名称
        """

        # 点击 - 未定义工作日 - 按钮
        SET_HOLIDAY = (By.XPATH, '//span[contains(text(), "未定义工作日")]')
        BasePage(self.driver).click_ele(SET_HOLIDAY)

        # 调用封装方法 - 添加特殊工作日
        self.dialog_info_com(tile_name, val)
        # 点击 - 设定日期 - 按钮
        SET_TIME = (By.XPATH, '//header[contains(text(), "特殊工作日定义")]/following-sibling::div//span[contains(text(), "设定日期")]')
        BasePage(self.driver).click_ele(SET_TIME)
        # 调用封装方法 - 选择特殊工作日的时间区间
        self.check_time()

    def assert_timezone_section(self):
        # 判断给当前时间条件下的时间段是否成功添加
        # CHECK_CON_RESULT = (By.XPATH, '//div[@class="el-tab-pane" and @style=""]')
        CHECK_CON_RESULT = (By.XPATH, '//div[@class="el-tab-pane" and @style=""]//div[contains(@class, "el-row")]//span[contains(text(), ":")]')
        return BasePage(self.driver).get_text(CHECK_CON_RESULT)


if __name__ == '__main__':
    from selenium import webdriver
    from guard.pages.components.menubar import MenubarPage
    from guard.pages.login import LoginPage

    driver = webdriver.Chrome()
    driver.get("http://10.151.3.96/login")
    LoginPage(driver).login("zhuwenqin", "888888")

    MenubarPage(driver).click_nav_item("配置", "时间条件")

    # TimezonePage(driver).add_timezone_name("input输入框内容")

    TimezonePage(driver).create_holidays("添加假期", "假期名称1")
    TimezonePage(driver).create_workday("添加特殊工作日", "工作日名称1")
    TimezonePage(driver).add_timezone_name("timezone1")


