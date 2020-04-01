# -*- coding:utf-8 -*-
# @Time: 2020/3/30 18:52
# @Author: wenqin_zhu
# @File: user.py
# @Software: PyCharm


from selenium.webdriver.common.by import By

from guard.pages.basepage import BasePage
from guard.pages.components.group_tree import GroupTree


class UserPage(BasePage):

    def add_department_by_root_name(self, flag=True):
        """ 从根部门<Default>下创建分组 """
        if flag:
            GroupTree(self.driver).click_menu_by_name("Default", "创建同级")
            title_name = "创建同级"
        else:
            GroupTree(self.driver).click_menu_by_name("Default", "创建下一级")
            title_name = "创建下一级"
        return title_name

    def create_department_group(self, til_name, val):
        """ 创建同级/下一级分组 方法 """
        # 定位input框
        # //span[contains(text(), "创建同级")]/parent::div/following-sibling::div[@class="el-dialog__body"]//input
        INPUT_TEXT = (By.XPATH, f'//span[contains(text(), "{til_name}")]/parent::div/following-sibling::div[@class="el-dialog__body"]//input')
        BasePage(self.driver).update_input_text(INPUT_TEXT, val)

        # 点击确认
        CONFIRM_BTN = (By.XPATH, f'//span[contains(text(), "{til_name}")]/parent::div/following-sibling::div[@class="el-dialog__footer"]//span[contains(text(), "确定")]')
        BasePage(self.driver).click_ele(CONFIRM_BTN)


if __name__ == '__main__':

    from selenium import webdriver
    from guard.pages.components.menubar import MenubarPage
    from guard.pages.login import LoginPage

    driver = webdriver.Chrome()
    driver.get("http://10.151.3.96/login")
    LoginPage(driver).login("zhuwenqin", "888888")

    MenubarPage(driver).click_nav_item("配置", "用户管理")
    title_name = UserPage(driver).add_department_by_root_name(flag=False)
    UserPage(driver).create_department_group(title_name, "分组名称")
