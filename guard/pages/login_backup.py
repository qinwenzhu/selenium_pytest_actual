# -*- coding:utf-8 -*-
# @Time: 2020/3/17 10:17
# @Author: wenqin_zhu
# @File: login_backup.py
# @Software: PyCharm


# 该 WebDriver 是所有其他 Webdriver 的父类<包括chrome、firefox、ie等>
from selenium.webdriver.remote.webdriver import WebDriver

# 导入显性等待
from selenium.webdriver.support.wait import WebDriverWait
# 导入显性等待期望条件
from selenium.webdriver.support import expected_conditions as EC
# 导入元素的定位方式
from selenium.webdriver.common.by import By

import time

# 导入第三方验证码识别接口
from utils.chaojiying import Chaojiying_Client
import urllib.request

from guard.tests.path import CommonPath

# 导入封装类
from utils.ssh import SSH
from utils.handle_config import HandleConfig


class LoginPage(object):

    def __init__(self, driver: WebDriver):
        # 传入driver
        self.driver = driver

        # 实例化等待对象
        self.wait = WebDriverWait(self.driver, 20)

    def login(self, username, password, code=None, flag=False):
        """ 登录 """

        # 定位到用户名文本框
        USERNAME_INPUT = (By.CSS_SELECTOR, 'input[name="username"]')
        # 显性等待用户文本框可见
        self.wait.until(EC.visibility_of_element_located(USERNAME_INPUT))
        # 输入用户名
        self.driver.find_element(*USERNAME_INPUT).send_keys(username)

        # 定位到密码文本框
        PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[name="password"]')
        # 显性等待密码文本框可见
        self.wait.until(EC.visibility_of_element_located(PASSWORD_INPUT))
        # 输入密码
        self.driver.find_element(*PASSWORD_INPUT).send_keys(password)

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
            self.wait.until(EC.visibility_of_element_located(CAPTCHA_REFRESH_BUTTON))
            self.driver.find_element(*CAPTCHA_REFRESH_BUTTON).click()
            time.sleep(0.5)
            # 2、通过调用封装的方法从日志里获取当前登录页面的验证码
            code = self.get_captcha_from_k8s_log()
            # 定位到验证码文本框
            CODE_INPUT = (By.CSS_SELECTOR, 'input[name="verifyCode"]')
            self.wait.until(EC.visibility_of_element_located(CODE_INPUT))
            # 输入验证码
            self.driver.find_element(*CODE_INPUT).send_keys(code)
        elif flag == 'ceshi':
            print("请手动输入登录页面的验证码：")
            # 手动输入验证码
            code = input()
            # 定位到验证码文本框
            CODE_INPUT = (By.CSS_SELECTOR, 'input[name="verifyCode"]')
            self.wait.until(EC.visibility_of_element_located(CODE_INPUT))
            # 输入验证码
            self.driver.find_element(*CODE_INPUT).send_keys(code)
        else:
            # 2、通过调用第三方接口<cjy>识别当前验证码
            code = self.get_code_cjy()
            # 定位到验证码文本框
            CODE_INPUT = (By.CSS_SELECTOR, 'input[name="verifyCode"]')
            self.wait.until(EC.visibility_of_element_located(CODE_INPUT))
            # 输入验证码
            self.driver.find_element(*CODE_INPUT).send_keys(code)

        # 定位到登录按钮
        LOGIN_BUTTON = (By.XPATH, '//button//span[contains(text(), "登录")]')
        # 显性等待登录按钮可见
        self.wait.until(EC.visibility_of_element_located(LOGIN_BUTTON))
        # 点击登录
        self.driver.find_element(*LOGIN_BUTTON).click()

    def get_code_cjy(self):
        """ 通过调用第三方接口获取验证码"""
        CODE_IMG = (By.CSS_SELECTOR, '.code-pic > img')
        self.wait.until(EC.visibility_of_element_located(CODE_IMG))
        code_img_src = self.driver.find_element(*CODE_IMG).get_attribute("src")
        # 将获取到的图片地址保存到本地目录
        urllib.request.urlretrieve(code_img_src, f'{CommonPath.DATA_FOLDER}\cjy_get_code\get_current_code.jpg')

        # 调第三方接口_识别验证码
        cjy = Chaojiying_Client('18500379756', '123456', '9bf661c27903e244883b5af71ed0c5da')  # 用户中心>>软件ID 生成一个
        img = open(f'{CommonPath.DATA_FOLDER}\cjy_get_code\get_current_code.jpg', 'rb').read()  # 本地图片文件路径,有时WIN系统须要//
        result = cjy.PostPic(img, 1902)  # 1902 验证码类型
        print(f"-------第三方接口识别当前的验证码为：{result['pic_str']}-----------")
        return result['pic_str']

    def get_captcha_from_k8s_log(self):
        SSH_CONFIG = HandleConfig('D:\wenqin\web_automation\Selenium_pytest_actual\guard\config\ssh_config.yml').config
        ssh_config = SSH_CONFIG.get("ssh")
        ssh_config['hostname'] = "10.151.3.96"
        ssh = SSH(**ssh_config)
        oauth2_pod_name = ssh.execute_command(
            "kubectl get pods | grep oauth2 | awk '{print $1}'")
        captcha = ssh.execute_command(
            f"kubectl logs {oauth2_pod_name.rstrip()} --tail 2 | grep 生成验证码存入redis | awk -F ' ' '{{print $5}}'")
        return captcha.rstrip()

    def login_success_info(self):
        # 定位到首页
        LOGIN_SUCCESS_USERNAME = (By.CSS_SELECTOR, 'span[class="avatar-name"]')
        self.wait.until(EC.visibility_of_element_located(LOGIN_SUCCESS_USERNAME))
        print(f"当前登录用户的别名为：{self.driver.find_element(*LOGIN_SUCCESS_USERNAME).text}")

        "/monitor"
        return self.driver.find_element(*LOGIN_SUCCESS_USERNAME).text


if __name__ == '__main__':

    from selenium import webdriver

    driver = webdriver.Chrome()
    # driver.maximize_window()
    driver.get("http://10.151.3.96/login")

    # print(os.getcwd())
    # print(os.path.split(os.getcwd())[0])

    # 测试通过手动输入验证码进行登录
    # LoginPage(driver).login("zhuwenqin", "888888", flag=False)

    # 测试通过调用第三方接口智能识别验证码进行登录
    # LoginPage(driver).login("zhuwenqin", "888888", flag=True)

    # 测试ssh连接服务器进行验证码获取来进行登录
    # LoginPage(driver).login("zhuwenqin", "888888")
