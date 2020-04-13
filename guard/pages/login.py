# -*- coding:utf-8 -*-
# @Time: 2020/3/17 10:17
# @Author: wenqin_zhu
# @File: login.py
# @Software: PyCharm


# 导入元素的定位方式
from selenium.webdriver.common.by import By

import time

# 导入第三方验证码识别接口
from utils.chaojiying import Chaojiying_Client
import urllib.request

# 导入封装类
from utils.ssh import SSH
from utils.handle_config import HandleConfig

# 导入共用路径
from guard.tools.share_path import SharePath

# 导入二次封装selenium框架的 BasePage类
from guard.pages.basepage import BasePage


class LoginPage(BasePage):

    def login(self, username, password, code=None, flag=False):
        """ 登录 """

        # 定位到用户名文本框
        USERNAME_INPUT = (By.CSS_SELECTOR, 'input[name="username"]')
        # 输入用户名 - 等待元素可见并输入文本
        BasePage(self.driver).update_input_text(USERNAME_INPUT, username, "登录")

        # 定位到密码文本框
        PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[name="password"]')
        # 输入密码
        BasePage(self.driver).update_input_text(PASSWORD_INPUT, password, "登录")

        # 定位到验证码文本框
        CODE_INPUT = (By.CSS_SELECTOR, 'input[name="verifyCode"]')

        """ 
        # TODO 获取验证码的方式
        1、通过日志获取验证码
        2、通过第三方识别验证码
        3、本地测试时通过手动的在控制台输入验证码来进行网页的登录<不推荐>
        """
        if flag is False:
            # 由于多人同时操作自动化环境，会导致获取到的日志里的验证码不是当前用户的登录页面的验证码
            # 优化方案：先对登录也的验证码进行刷新操作，然后去日志获取验证码
            CAPTCHA_REFRESH_BUTTON = (By.CSS_SELECTOR, 'div.verify-code > div.refresh > i')
            BasePage(self.driver).click_ele(CAPTCHA_REFRESH_BUTTON, "登录")
            time.sleep(0.2)

            # 2、通过调用封装的方法从日志里获取当前登录页面的验证码
            code = self.get_captcha_from_k8s_log()

            # if code is None:
            #     # 获取到错误信息的元素定位
            #     CAPTCHA_ERROR_TEXT = (By.XPATH, '//div[@class="el-form-item__error"]')
            #     error_text = BasePage(self.driver).get_text(CAPTCHA_ERROR_TEXT, "登录")
            #     while error_text in "验证码不正确":
            #         code = self.get_captcha_from_k8s_log()

            BasePage(self.driver).update_input_text(CODE_INPUT, code, "登录")
        elif flag == 'ceshi':
            # 手动输入验证码
            print("请手动输入登录页面的验证码：")
            code = input()
            BasePage(self.driver).update_input_text(CODE_INPUT, code, "登录")
        else:
            # 2、通过调用第三方接口<cjy>识别当前验证码
            code = self.get_code_cjy()
            BasePage(self.driver).update_input_text(CODE_INPUT, code, "登录")

        # 定位到登录按钮
        LOGIN_BUTTON = (By.XPATH, '//button//span[contains(text(), "登录")]')
        BasePage(self.driver).click_ele(LOGIN_BUTTON, "登录")

    def login_success_info(self):
        # 登录成功，页面中的个人信息和当前登陆用户一致
        LOGIN_SUCCESS_USERNAME = (By.CSS_SELECTOR, 'span[class="avatar-name"]')
        result_text = BasePage(self.driver).get_text(LOGIN_SUCCESS_USERNAME)
        print(f"当前登录用户的别名为：{result_text}")             # "/monitor"
        return result_text

    # def is_login_success(self):
    #     # 判断登录是否成功
    #
    #     LOGIN_SUCCESS_USERNAME = (By.CSS_SELECTOR, 'span[class="avatar-name"]')
    #     text_result = BasePage(self.driver).get_text(LOGIN_SUCCESS_USERNAME)
    #     if text_result is None:
    #         return True
    #     else:
    #         return False

        # BasePage(self.driver).wait_for_ele_to_be_presence(LOGIN_SUCCESS_USERNAME)
        # if BasePage(self.driver).get_ele_locator(LOGIN_SUCCESS_USERNAME):
        #     return True
        # else:
        #     return False

    # def get_error_username(self):
    #     # 用户名错误信息
    #     LOGIN_ERROR_USERNAME = (By.XPATH, '//input[@name="username"]/parent::div/following-sibling::div')
    #     return BasePage(self.driver).get_text(LOGIN_ERROR_USERNAME)
    #
    # def get_error_password(self):
    #     # 用户名错误信息
    #     LOGIN_ERROR_USERNAME = (By.XPATH, '//input[@name="username"]/parent::div/following-sibling::div')
    #     return BasePage(self.driver).get_text(LOGIN_ERROR_USERNAME)

    def get_code_cjy(self):
        """ 通过调用第三方接口获取验证码"""
        CODE_IMG = (By.CSS_SELECTOR, '.code-pic > img')
        BasePage(self.driver).wait_for_ele_to_be_visible(CODE_IMG, "登录")
        code_img_src = BasePage(self.driver).get_ele_locator(CODE_IMG).get_attribute("src")
        # 将获取到的图片地址保存到本地目录
        urllib.request.urlretrieve(code_img_src, r'{}\cjy_read_code\save_cur_code.jpg'.format(SharePath.DATA_FOLDER))

        # 调第三方接口_识别验证码
        cjy = Chaojiying_Client('18500379756', '123456', '9bf661c27903e244883b5af71ed0c5da')  # 用户中心>>软件ID 生成一个
        img = open(r'{}\cjy_read_code\save_cur_code.jpg'.format(SharePath.DATA_FOLDER), 'rb').read()  # 本地图片文件路径,有时WIN系统须要//
        result = cjy.PostPic(img, 1902)  # 1902 验证码类型
        print(f"-------第三方接口识别当前的验证码为：{result['pic_str']}-----------")
        return result['pic_str']

    def get_captcha_from_k8s_log(self):
        SSH_CONFIG = HandleConfig(r'{}\ssh_config.yml'.format(SharePath.CONFIG_FOLDER)).config
        ssh_config = SSH_CONFIG.get("ssh")
        ssh_config['hostname'] = "10.151.3.96"
        ssh = SSH(**ssh_config)
        oauth2_pod_name = ssh.execute_command(
            "kubectl get pods | grep oauth2 | awk '{print $1}'")
        captcha = ssh.execute_command(
            f"kubectl logs {oauth2_pod_name.rstrip()} --tail 2 | grep 生成验证码存入redis | awk -F ' ' '{{print $5}}'")
        return captcha.rstrip()


if __name__ == '__main__':

    from selenium import webdriver

    driver = webdriver.Chrome()
    driver.get("http://10.151.3.96/login")

    # 测试通过手动输入验证码进行登录
    # LoginPage(driver).login("zhuwenqin", "888888", flag=False)

    # 测试通过调用第三方接口智能识别验证码进行登录
    # LoginPage(driver).login("zhuwenqin", "888888", flag=True)

    # 测试ssh连接服务器进行验证码获取来进行登录
    LoginPage(driver).login("zhuwenqin", "888888")
