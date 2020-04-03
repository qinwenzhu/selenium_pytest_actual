# -*- coding:utf-8 -*-
# @Time: 2020/4/3 16:05
# @Author: wenqin_zhu
# @File: uuid_generate_unique_data.py
# @Software: PyCharm


import uuid


def uuid_data():
    # 生成全球唯一的数据
    unique_datq = str(uuid.uuid1())
    return unique_datq
