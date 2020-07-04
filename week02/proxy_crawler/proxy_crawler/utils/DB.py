# ****************************
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/4 15:44
# Author = kissene_xie
# @File    : DB
# ****************************
import os

__author__ = 'kissene_xie'

import pymysql
import configparser


class SQLManager(object):
    # 初始化实例的时候调用connect方法连接数据库
    def __init__(self, config):
        self.conn = None
        self.cursor = None
        self.connect(config)

    # 连接数据库
    def connect(self, config):
        self.conn = pymysql.connect(
            host=config['host'],
            port=int(config['port']),
            database=config['db'],
            user=config['user'],
            password=config['pwd'],
            charset=config['charset']
        )
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 查询多条数据sql是sql语句，args是sql语句的参数
    def get_list(self, sql, args=None):
        self.cursor.execute(sql, args)
        result = self.cursor.fetchall()
        return result

    # 查询单条数据
    def get_one(self, sql, args=None):
        self.cursor.execute(sql, args)
        result = self.cursor.fetchone()
        return result

    # 执行单条SQL语句
    def moddify(self, sql, args=None):
        self.cursor.execute(sql, args)
        self.conn.commit()

    # 执行多条SQL语句
    def multi_modify(self, sql, args=None):
        self.cursor.executemany(sql, args)
        self.conn.commit()

    # 关闭数据库
    def close(self):
        self.cursor.close()
        self.conn.close()

    # 进入with语句自动执行
    def __enter__(self):
        return self

    # 退出with语句自动执行
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


if __name__ == "__main__":
    sql_ver = 'select VERSION()'

    cp = configparser.ConfigParser()
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_file = os.path.join(BASE_DIR, 'DB_config', 'setting.cfg')
    if os.path.exists(config_file):
        cp.read(config_file)
        info = cp.items('mysql')
        db = SQLManager(dict(info))
        with db as d:
            r = db.get_one(sql_ver)
            print(r)
    else:
        raise FileNotFoundError('未发现配置文件！~ {}'.format(config_file))

