# -*- coding:utf-8 -*-
# @Time: 2020/3/30 18:52
# @Author: wenqin_zhu
# @File: user.py
# @Software: PyCharm


from guard.pages.basepage import BasePage
from guard.pages.components.group_tree import GroupTree


class UserPage(BasePage):

    def add_department_by_root_name(self, flag=True):
        if flag:
            GroupTree(self.driver).click_menu_by_name("Default", "创建同级")
        else:
            GroupTree(self.driver).click_menu_by_name("Default", "创建下一级")


if __name__ == '__main__':
    from selenium import webdriver
    from guard.pages.components.menubar import MenubarPage
    from guard.pages.login import LoginPage

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://10.151.3.96/login")
    LoginPage(driver).login("zhuwenqin", "888888")

    MenubarPage(driver).click_nav_item("配置", "用户管理")
    UserPage(driver).add_department_by_root_name()
