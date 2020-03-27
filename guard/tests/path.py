# -*- coding:utf-8 -*-
# @Time: 2020/3/19 14:33
# @Author: wenqin_zhu
# @File: path.py
# @Software: PyCharm

import os


class CommonPath:

    # 获取当前文件的绝对路径
    current_path = os.path.abspath(__file__)
    """ 通过 os.path.split() 对路径进行分割获取到项目的根目录   os.path.split()   当前目录为3级，需要分割3次 """
    PRO_PATH = os.path.split(os.path.split(os.path.split(os.path.abspath(__file__))[0])[0])[0]

    # 定位到 config 目录
    CONFIG_FOLDER = f"{PRO_PATH}/guard/config"

    # 定位到 data 目录
    DATA_FOLDER = f"{PRO_PATH}/guard/data"
