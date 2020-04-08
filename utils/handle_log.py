# -*- coding: utf-8 -*-
# @Time: 2019/7/24 22:35
# @Author: wenqin_zhu
# @File: handle_log.py
# @software: PyCharm

import logging


""" 日志等级
'DEBUG': 打印全部的日志
'INFO': 打印info,warning,error,critical级别的日志
'WARNING': 打印warning,error,critical级别的日志
'ERROR': 打印error,critical级别的日志
'CRITICAL': 打印critical级别
"""


class HandleLog:
    """ 封装日志操作 """

    def __init__(self, path_to_log=None):

        self.logger = logging.getLogger("")
        # 设置收集日志的等级
        self.logger.setLevel(logging.DEBUG)

        # 定义日志输出到控制台 并设置输出日志的等级
        console = logging.StreamHandler()
        console.setLevel(logging.ERROR)

        # 定义日志输出到文件 并设置输出日志的等级
        log_file = logging.FileHandler(path_to_log, encoding='utf-8')
        log_file.setLevel(logging.DEBUG)

        # 设置日志输出格式
        formatter = logging.Formatter('[%(asctime)s] - %(levelname)s - %(message)s')
        console.setFormatter(formatter)
        log_file.setFormatter(formatter)

        # 添加内容到日志句柄中
        self.logger.addHandler(console)
        self.logger.addHandler(log_file)

    def get_log(self):
        return self.logger

    def info(self, message):
        self.logger.info(message)

    def debug(self, message):
        self.logger.debug(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)


if __name__ == '__main__':
    log = HandleLog("log.txt").get_log()
    log.debug('debug')
    log.info('info')
    log.warning('warning')
    log.error('error')
    log.critical('严重')
