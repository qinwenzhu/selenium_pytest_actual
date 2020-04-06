# -*- coding: utf-8 -*-
# @Time: 2019/7/24 22:35
# @Author: wenqin_zhu
# @Email: zhuwneqin528@163.com
# @File: do_log.py
# @software: PyCharm

import logging

from method_interface_auto_02.scripts.constants import LOG_ASSERT_ACT_DIR, LOG_ASSERT_DAY_DIR


class DoLog:
    """
    封装日志操作类
    """
    def __init__(self, logger_name):

        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.DEBUG)

        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)

        # 通过 LOG_ASSERT_ACT_DIR, LOG_ASSERT_DAY_DIR 两个参数动态选择创建动态日志文件的方式
        fh = logging.FileHandler(LOG_ASSERT_DAY_DIR, encoding='utf-8')
        fh.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - [%(name)s] - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)

        self.logger.addHandler(ch)
        self.logger.addHandler(fh)

        # self.logger.removeHandler(fh)
        # self.logger.removeHandler(ch)

    def get_log(self):
        return self.logger


if __name__ == '__main__':
    my_log = DoLog("日志收集器自定义名称").get_log()
    my_log.debug("这是 debug 信息")
    my_log.info("这是 info 信息")
    my_log.warning("这是 warning 信息")
    my_log.error("这是 error 信息")
    my_log.critical("这是 critical 信息")
