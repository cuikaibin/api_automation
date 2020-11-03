#!/user/bin/python3
#encoding: utf-8

"""
File:
Anthor: cuikaibin
Date: 2020/9/4
"""

import os
import MySQLdb
import configparser
from lib.log import Logger


class db(object):
    """
    @summary 封装db模块
    """
    def __init__(self, table, charset='utf8'):
        path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        conf_path = path + "/conf/db.conf"
        cf = configparser.ConfigParser()
        cf.read(conf_path)

        self.host = cf.get('monkey_test_db', 'host')
        self.port = int(cf.get('monkey_test_db', 'port'))
        self.user = cf.get('monkey_test_db', 'user')
        self.passward = cf.get('monkey_test_db', 'passward')
        self.table = table
        self.charset = charset
        self.log = Logger()

    def db_execute(self, sql):
        """
        @summary 除查询外的操作使用该方案
        """
        db = MySQLdb.connect(host=self.host, port=self.port, user=self.user, passwd=self.passward, 
            db=self.table, charset=self.charset)
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
            self.log.error("'{}'sql语句执行失败".format(sql))
        db.close()

    def db_check(self, sql):
        """
        @summary 查询操作
        """
        db = MySQLdb.connect(host=self.host, port=self.port, user=self.user, passwd=self.passward, 
            db=self.table, charset=self.charset)
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            self.log.error('test')
        except:
            db.rollback()
            self.log.error("'{}'sql语句执行失败".format(sql))
            results = False
        db.close()
        return results


if __name__ == '__main__':
    sql = "select id from picture_book_brand where name='cuikaibin1_test'"
    print(db('picture_book_test').db_check(sql)[0][0])
            
        












