# -*- coding:utf-8 -*-
# @Time: 2020/4/13 17:50
# @Author: wenqin_zhu
# @File: call_database.py
# @Software: PyCharm


from guard.tools.share_path import SharePath
from utils.handle_config import HandleConfig
from utils.handle_database import HandleDB


class CallDb:

    # 调用数据库查询结果
    DB_CONFIG = HandleConfig(r'{}\db_config.yml'.format(SharePath.CONFIG_FOLDER)).config
    db_config = DB_CONFIG.get("database")
    # db_config['host'] = "10.151.3.96"
    db_config['host'] = "10.151.3.111"

    # 连接数据库
    db = HandleDB(host=db_config['host'], username=db_config['user'],
                  password=db_config['password'], port=db_config['port'], database="senseguard")

    def query_result_by_database(self, sql, args=None):
        # 返回查询结果
        return self.db.select_database(sql, args)
