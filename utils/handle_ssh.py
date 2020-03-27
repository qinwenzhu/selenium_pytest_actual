# -*- coding:utf-8 -*-
# @Time: 2020/3/19 15:42
# @Author: wenqin_zhu
# @File: handle_ssh.py
# @Software: PyCharm


import paramiko


class HandleSSH:

    def __init__(self):
        pass

    def connect_to_server(self, hostname):
        # 创建SSH对象
        ssh = paramiko.SSHClient()

        # 允许连接不在 know_hosts 文件中的主机
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # 连接服务器
        ssh.connect(hostname="10.151.3.96", port=22, username="root", pkey="Nebula123$%^")

        # 执行命令
        ssh.exec_command("命令行代码")

        # 关闭连接
        ssh.close()
