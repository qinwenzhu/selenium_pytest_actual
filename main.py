# -*- coding:utf-8 -*-
# @Time: 2020/4/7 14:06
# @Author: wenqin_zhu
# @File: main.py.py
# @Software: PyCharm


import pytest

if __name__ == '__main__':
    # pytest.main()
    pytest.main(["-s", "-v", "--html=outputs/html/web_report.html", "--alluredir=outputs/allure/allure_report"])
