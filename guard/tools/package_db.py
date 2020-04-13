# -*- coding:utf-8 -*-
# @Time: 2020/4/13 17:50
# @Author: wenqin_zhu
# @File: package_db.py
# @Software: PyCharm


from guard.tests.path import CommonPath
from utils.handle_config import HandleConfig
from utils.handle_database import HandleDB


def query_result_by_database(sql, args=None):
    # 调用数据库查询结果
    DB_CONFIG = HandleConfig(r'{}\db_config.yml'.format(CommonPath.CONFIG_FOLDER)).config
    db_config = DB_CONFIG.get("database")
    db_config['host'] = "10.151.3.96"

    db = HandleDB(host=db_config['host'], username=db_config['user'],
                  password=db_config['password'], port=db_config['port'], database="senseguard")
    return db.select_database(sql, args)
