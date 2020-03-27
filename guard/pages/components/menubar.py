# -*- coding:utf-8 -*-
# @Time: 2020/3/16 11:21
# @Author: wenqin_zhu
# @File: menubar.py
# @Software: PyCharm

from selenium.webdriver.remote.webdriver import WebDriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 导入鼠标操作
from selenium.webdriver.common.action_chains import ActionChains


class MenubarPage(object):

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def click_nav_item(self, menu_text, sub_menu_text=None):
        """
        封装导航栏组件：传入的参数是一级还是二级导航
        :param menu_text: 菜单文本<导航文本的唯一性>
        :param sub_menu_text: 子菜单文本
        :return:
        """

        if menu_text == "工具":
            MENU_TEXT = (By.XPATH, f'//div[text()="{menu_text}"]')
            SUB_MENU_TEXT = (By.XPATH, f'//li[text()="{sub_menu_text}"]')
        else:
            MENU_TEXT = (By.XPATH, f'//em[text()="{menu_text}"]')
            SUB_MENU_TEXT = (By.XPATH, f'//em[text()="{sub_menu_text}"]')

        if sub_menu_text is not None:
            # 通过移动到一级目录然后点击二级目录
            self.wait.until(EC.visibility_of_element_located(MENU_TEXT))
            menu_ele = self.driver.find_element(*MENU_TEXT)
            ActionChains(self.driver).move_to_element(menu_ele).perform()

            # self.wait.until(EC.visibility_of_element_located(SUB_MENU_TEXT))
            self.wait.until(EC.presence_of_element_located(SUB_MENU_TEXT))
            sub_menu_ele = self.driver.find_element(*SUB_MENU_TEXT)
            ActionChains(self.driver).move_to_element(menu_ele).click(sub_menu_ele).perform()

        else:
            # 选择指定的一级目录
            self.wait.until(EC.visibility_of_element_located(MENU_TEXT))
            self.driver.find_element(*MENU_TEXT).click()


if __name__ == '__main__':

    from selenium import webdriver
    from guard.pages.login_backup import LoginPage
    import time

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://10.151.3.96/login")
    LoginPage(driver).login("zhuwenqin", "888888", flag=False)

    # 测试点击存在二级导航的
    MenubarPage(driver).click_nav_item("工具", "人脸属性检测")

    time.sleep(10)

    # 测试点击只存在一级导航
    MenubarPage(driver).click_nav_item("看板")
