# -*- coding:utf-8 -*-
# @Time: 2020/4/10 16:09
# @Author: wenqin_zhu
# @File: timezone.py
# @Software: PyCharm


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

    def add_timezone_name(self, val):
        """
        添加时间条件
        :param val: 时间条件的名称
        """
        # 定位到添加时间条件的按钮
        ICON = (By.XPATH, '//span[contains(text(), "时间条件名称")]/i')
        BasePage(self.driver).click_ele(ICON)

        # 调用封装方法 - 添加时间条件名称
        self.dialog_info_com("添加时间条件", val)

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
        SET_TIME = (By.XPATH, '//span[contains(text(), "设定日期")]')
        BasePage(self.driver).click_ele(SET_TIME)
        # 调用封装方法 - 选择假期的时间区间
        self.check_time()


if __name__ == '__main__':
    from selenium import webdriver
    from guard.pages.components.menubar import MenubarPage
    from guard.pages.login import LoginPage

    driver = webdriver.Chrome()
    driver.get("http://10.151.3.96/login")
    LoginPage(driver).login("zhuwenqin", "888888")

    MenubarPage(driver).click_nav_item("配置", "时间条件")

    # TimezonePage(driver).add_timezone_name("input输入框内容")

    # TimezonePage(driver).create_holidays("添加假期", "假期名称")
