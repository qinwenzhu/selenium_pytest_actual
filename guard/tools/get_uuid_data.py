# -*- coding:utf-8 -*-
# @Time: 2020/4/3 16:05
# @Author: wenqin_zhu
# @File: get_uuid_data.py
# @Software: PyCharm


import uuid


def uuid1_data():
    # 生成全球唯一的数据
    unique_datq = str(uuid.uuid1())
    return unique_datq


def uuid4_data():
    # 生成全球唯一的数据
    unique_datq = str(uuid.uuid4())
    return unique_datq


if __name__ == '__main__':
    print(uuid4_data())
    print(uuid1_data())
