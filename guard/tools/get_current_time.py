# -*- coding: utf-8 -*-
# @time: 2020/4/13 22:23 
# @Author: wenqinzhu
# @Email: zhuwenqin_vendor@sensetime.com
# @file: get_current_time.py
# @software: PyCharm

import time


def get_current_time():
    # 获取当前时间
    return time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))


if __name__ == '__main__':
    print(type(get_current_time()))
