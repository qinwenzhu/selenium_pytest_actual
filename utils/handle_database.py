# -*- coding:utf-8 -*-
# @Time: 2020/4/13 15:53
# @Author: wenqin_zhu
# @File: handle_database.py
# @Software: PyCharm


import pymysql


class HandleDB(object):
    """ 封装数据库操作 """

    def __init__(self, host, username, password, database, port=3306):
        """
        初始化数据库信息并创建数据库连接
        :param host: 连接数据库主机 如：10.151.3.96
        :param username: 数据库登录用户名
        :param password: 数据库登录密码
        :param database: 连接的数据库名称 如：senseguard
        :param port: 数据库端口，默认为：3306
        """
        # self.conn_db = pymysql.connect(host, username, password, database, port, charset='utf8')
        self.conn_db = pymysql.connect(host, username, password, database, port, charset='utf8', cursorclass=pymysql.cursors.DictCursor)
        # 建立游标,并设置数据库返回数据的数据类型:返回类型为字典类型
        self.cursor = self.conn_db.cursor()

    def select_database(self, sql, args=None, is_more=False):
        self.cursor.execute(sql, args=args)
        self.conn_db.commit()
        if is_more:
            return self.cursor.fetchall()
        else:
            return self.cursor.fetchone()

    def close(self):
        # 关闭游标
        self.cursor.close()
        # 关闭数据库连接
        self.conn_db.close()


if __name__ == '__main__':

    # mobile = '18999990262'
    # sql_1 = "SELECT * FROM member WHERE MobilePhone=%s"
    # sql_2 = "SELECT * FROM member LIMIT 0, 10;"

    do_mysql = HandleDB(host="10.151.3.96", username="root", password="UVlY88m9suHLsthK", database="senseguard", port=30446)

    #  调用封装的数据库查询方法
    # 方式-：查询动态传入参数的
    time_zone = "TimeZone-a1fceba3-1afe-46"
    sql1 = 'SELECT * FROM senseguard.info_time_zone WHERE time_zone_name=%s;'
    print(sql1)
    db_result1 = do_mysql.select_database(sql1, args=(time_zone, ), is_more=False)
    print(db_result1)

    # 方式二：查询表内所有
    sql2 = 'SELECT * FROM senseguard.info_time_zone;'
    db_result2 = do_mysql.select_database(sql2, is_more=True)
    print(sql2)
    print(db_result2)
