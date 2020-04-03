# -*- coding:utf-8 -*-
# @Time: 2020/3/30 18:52
# @Author: wenqin_zhu
# @File: user.py
# @Software: PyCharm


from selenium.webdriver.common.by import By

from guard.pages.basepage import BasePage
from guard.pages.components.group_tree import GroupTree


class UserPage(BasePage):

    def create_dep_group(self, group_name, til_name, parent_name="Default", confirm=True):
        """
        方法封装：创建 同级/下一级 分组
        :param parent_name: 父级分组名称
        :param group_name: 部分分组名称
        :param til_name: dialog弹框中的标题 - 作为识别打开的当前弹框页面
        :param confirm: 判断是点击确定还是点击取消按钮 True默认创建点击确定按钮
        :return:
        """
        GroupTree(self.driver).click_group_by_name(parent_name)
        # 组名称input框
        GROUP_INPUT = (By.XPATH, f'//span[contains(text(),"{til_name}")]/parent::div/following-sibling::div[@class="el-dialog__body"]//input')
        BasePage(self.driver).update_input_text(GROUP_INPUT, group_name)
        if confirm:
            # 点击确认
            CONFIRM_BTN = (By.XPATH, f'//span[contains(text(),"{til_name}")]/parent::div/following-sibling::div[@class="el-dialog__footer"]//span[contains(text(),"确定")]')
            BasePage(self.driver).click_ele(CONFIRM_BTN)
        else:
            # 点击取消
            CONFIRM_BTN = (By.XPATH, f'//span[contains(text(),"{til_name}")]/parent::div/following-sibling::div[@class="el-dialog__footer"]//span[contains(text(),"取消")]')
            BasePage(self.driver).click_ele(CONFIRM_BTN)

    def create_department_from_Default(self, flag=True):
        if flag:
            """ 从Default目录下创建同级分组 """
            self.create_dep_group("Default", "创建同级")
        else:
            """ 从Default目录下创建下一级分组 """
            self.create_dep_group("Default", "创建下一级")


    # def create_sub_department_from_Default(self):





    pass


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
