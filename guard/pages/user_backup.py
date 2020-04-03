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
        """
        从根部门 - Default 下创建 同级 / 下一级 分组
        :param flag: 判断是创建同级分组还是下一级分组
        :return: 当前需要创建的分组类别
        """
        if flag:
            GroupTree(self.driver).click_menu_by_name("Default", "创建同级")
            title_name = "创建同级"
        else:
            GroupTree(self.driver).click_menu_by_name("Default", "创建下一级")
            title_name = "创建下一级"
        return title_name

    # def delete_department_by_root_name(self, group_name, flag=True, confirm=True):
    #     """
    #     通过组名称删除分组
    #     :param group_name: 组名称
    #     :param flag: 判断是删除同级分组还是下一级分组
    #     :param confirm: 判断是点击删除还是点击取消按钮 True默认创建点击删除按钮
    #     :return:
    #     """
    #     print(group_name)
    #     GroupTree(self.driver).click_menu_by_name(group_name, "删除")
    #     if flag:
    #         GroupTree(self.driver).click_group_by_name(group_name)
    #     else:
    #         # GroupTree(self.driver).click_group_by_name(parent_name)
    #         pass
    #
    #     if confirm:
    #         # 点击确认
    #         CONFIRM_BTN = (By.XPATH, '//span[contains(text(),"删除")]/parent::div/following-sibling::div[@class="el-dialog__footer"]//span[contains(text(),"删除")]')
    #         BasePage(self.driver).click_ele(CONFIRM_BTN)
    #     else:
    #         # 点击取消
    #         CONFIRM_BTN = (By.XPATH,
    #                        '//span[contains(text(),"删除")]/parent::div/following-sibling::div[@class="el-dialog__footer"]//span[contains(text(),"取消")]')
    #         BasePage(self.driver).click_ele(CONFIRM_BTN)


    # def add_department_by_user_defined_name(self, dep_name, flag=True):
    #     """
    #     从 用户新建的parent分组 下创建 同级 / 下一级 分组
    #     :param flag: 判断是创建同级分组还是下一级分组 True默认创建同级
    #     :return: 当前需要创建的分组类别
    #     """
    #     if flag:
    #         GroupTree(self.driver).click_menu_by_name(dep_name, "创建同级")
    #         title_name = "创建同级"
    #     else:
    #         GroupTree(self.driver).click_menu_by_name(dep_name, "创建下一级")
    #         title_name = "创建下一级"
    #     return title_name

    def create_department_group(self, group_name, til_name, confirm=True):
        """
        方法封装：用于创建 同级/下一级 分组
        :param dep_name: 部分分组名称
        :param til_name: dialog弹框中的标题 - 作为识别打开的当前弹框页面
        :param confirm: 判断是点击确定还是点击取消按钮 True默认创建点击确定按钮
        :return:
        """
        # 定位input框
        # //span[contains(text(), "创建同级")]/parent::div/following-sibling::div[@class="el-dialog__body"]//input
        INPUT_TEXT = (By.XPATH, f'//span[contains(text(),"{til_name}")]/parent::div/following-sibling::div[@class="el-dialog__body"]//input')
        BasePage(self.driver).update_input_text(INPUT_TEXT, group_name)

        if confirm:
            # 点击确认
            CONFIRM_BTN = (By.XPATH, f'//span[contains(text(),"{til_name}")]/parent::div/following-sibling::div[@class="el-dialog__footer"]//span[contains(text(),"确定")]')
            BasePage(self.driver).click_ele(CONFIRM_BTN)
        else:
            # 点击取消
            CONFIRM_BTN = (By.XPATH,
                           f'//span[contains(text(),"{til_name}")]/parent::div/following-sibling::div[@class="el-dialog__footer"]//span[contains(text(),"取消")]')
            BasePage(self.driver).click_ele(CONFIRM_BTN)

    # def view_details(self, dep_name):
    #     """ 查看当前分组的详情信息 """
    #     GroupTree(self.driver).click_menu_by_name(dep_name, "详情")
    #     DETAIL_GTOUP_TEXT = (By.XPATH, '//span[contains(text(),"详情")]/parent::div/following-sibling::div[@class="el-dialog__body"]//div[@class="right"]//span[1]')
    #     # 查看详情 - 返回当前分组的名称
    #     return BasePage(self.driver).get_text(DETAIL_GTOUP_TEXT)
    #
    # def rename_dep_group(self, dep_name, val, confirm=True):
    #     """ 重命名分组 """
    #     GroupTree(self.driver).click_menu_by_name(dep_name, "重命名")
    #     DETAIL_GTOUP_TEXT = (By.XPATH, '//span[contains(text(),"编辑")]/parent::div/following-sibling::div[@class="el-dialog__body"]//input')
    #     BasePage(self.driver).update_input_text(DETAIL_GTOUP_TEXT, val)
    #     if confirm:
    #         # 点击确认
    #         CONFIRM_BTN = (By.XPATH, '//span[contains(text(),"编辑")]/parent::div/following-sibling::div[@class="el-dialog__footer"]//span[contains(text(),"确定")]')
    #         BasePage(self.driver).click_ele(CONFIRM_BTN)
    #     else:
    #         # 点击取消
    #         CONFIRM_BTN = (By.XPATH,
    #                        '//span[contains(text(),"编辑")]/parent::div/following-sibling::div[@class="el-dialog__footer"]//span[contains(text(),"取消")]')
    #         BasePage(self.driver).click_ele(CONFIRM_BTN)
    #
    # def delete_dep_by_name(self, group_name, flag=True, confirm=True):
    #     """
    #     通过组名称删除分组
    #     :param group_name: 组名称
    #     :param flag: 判断是删除同级分组还是下一级分组
    #     :param confirm: 判断是点击删除还是点击取消按钮 True默认创建点击删除按钮
    #     :return:
    #     """
    #     print(group_name)
    #     GroupTree(self.driver).click_menu_by_name(group_name, "删除")
    #     if flag:
    #         GroupTree(self.driver).click_group_by_name(group_name)
    #     else:
    #         # GroupTree(self.driver).click_group_by_name(parent_name)
    #         pass
    #
    #     if confirm:
    #         # 点击确认
    #         CONFIRM_BTN = (By.XPATH, '//span[contains(text(),"删除")]/parent::div/following-sibling::div[@class="el-dialog__footer"]//span[contains(text(),"删除")]')
    #         BasePage(self.driver).click_ele(CONFIRM_BTN)
    #     else:
    #         # 点击取消
    #         CONFIRM_BTN = (By.XPATH,
    #                        '//span[contains(text(),"删除")]/parent::div/following-sibling::div[@class="el-dialog__footer"]//span[contains(text(),"取消")]')
    #         BasePage(self.driver).click_ele(CONFIRM_BTN)


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
