# -*- coding:utf-8 -*-
# @Time: 2020/3/30 19:15
# @Author: wenqin_zhu
# @File: group_tree.py
# @Software: PyCharm


from selenium.webdriver.common.by import By
from guard.pages.basepage import BasePage


class GroupTree(BasePage):

    def click_group_by_name(self, group_name):
        """ 通过 组名称<如：Default> 点击元素 """
        # //div[@title="Default"]
        GROUP_NAME = (By.XPATH, f'//div[@title="{group_name}"]')
        BasePage(self.driver).click_ele(GROUP_NAME)

    def click_menu_by_name(self, group_name, menu_name):
        """ 通过 组名称<如：Default> 点击对应的 menu菜单<如：创建同级> """
        # 先获取到指定group上对应的icon并滑动到该元素
        # //div[@title="Default"]/parent::div/following-sibling::div[contains(text(), "︙")]
        GROUP_ICON = (By.XPATH, f'//div[@title="{group_name}"]/parent::div/following-sibling::div[contains(text(), "︙")]')
        BasePage(self.driver).mouse_move_ele(GROUP_ICON)

        # 等待该元素出现后，进行点击操作
        # //div[@id="menu"]//li[@class="menu" and contains(text(), "创建同级")]
        GROUP_MENU_NAME = (By.XPATH, f'//div[@id="menu"]//li[@class="menu" and contains(text(), "{menu_name}")]')
        BasePage(self.driver).mouse_move_ele_and_click(GROUP_ICON, GROUP_MENU_NAME)
