# -*- coding: utf-8 -*-
# @Time    : 2018/7/25 上午10:46
# @Author  : WangJuan
# @File    : Config.py

import configparser
from lib.log import Logger
import os


class Config:
    # titles:
    TITLE_DEBUG = "english"
    TITLE_DB = "monkey_test_db"
    TITLE_AI = "test_monkey_ai"
    TITLE_OA = "test_platform_oa"
    TITLE_TECH_DB = "monkey_test_tech_db"
    TITLE_Grow = "test_grow_url"

    # values:
    # [debug\release]
    VALUE_URL_BASE = "url_base"

    #[monkey_test_db/monkey_test_tech_db]
    VALUE_DB_HOST = "host"
    VALUE_DB_PORT = "port"
    VALUE_DB_USER = "user"
    VALUE_DB_PASSWORD = "password"
    VALUE_DB_CHARSET = "charset"

    # [test_monkey_ai]
    VALUE_AI_URL_BASE = "url_base"
    VALUE_AI_URL_BASE_SMS = "url_base_sms"

    # [test_monkey_oa]
    VALUE_OA_URL_BASE = "url_base"

    #[test_grow_url]
    Value_Grow_Base = "test_base_url"

    def __init__(self):
        """
        初始化
        """
        self.log = Logger()
        self.config = configparser.RawConfigParser()
        # self.log = Log.MyLog()
        # path
        try:
            PATH_LIST = os.getcwd().split("\\")
            self.log.info('执行路径为:{}'.format(PATH_LIST))
            PATH = "\\".join(PATH_LIST[:PATH_LIST.index('mts')+1])
        except Exception:
            PATH_LIST = os.getcwd().split("/")
            self.log.info('执行路径为:{}'.format(PATH_LIST))
            PATH = "/".join(PATH_LIST[:PATH_LIST.index('mts')+1])
        self.log.info('跟路径为:{}'.format(PATH))
        try:
            self.conf_path = os.path.join(PATH, 'conf\conf.ini')
            os.stat(self.conf_path)
        except Exception:
            self.conf_path = os.path.join(PATH, 'conf/conf.ini')
            os.stat(self.conf_path)
        if not os.path.exists(self.conf_path):
            raise FileNotFoundError("请确保配置文件存在！")

        self.config.read(self.conf_path, encoding='utf-8')

        self.db_host = self.get_conf(Config.TITLE_DB, Config.VALUE_DB_HOST)
        self.db_port = self.get_conf(Config.TITLE_DB, Config.VALUE_DB_PORT)
        self.db_user = self.get_conf(Config.TITLE_DB, Config.VALUE_DB_USER)
        self.db_password = self.get_conf(Config.TITLE_DB, Config.VALUE_DB_PASSWORD)
        self.db_charset = self.get_conf(Config.TITLE_DB, Config.VALUE_DB_CHARSET)

        self.tech_db_host = self.get_conf(Config.TITLE_TECH_DB, Config.VALUE_DB_HOST)
        self.tech_db_port = self.get_conf(Config.TITLE_TECH_DB, Config.VALUE_DB_PORT)
        self.tech_db_user = self.get_conf(Config.TITLE_TECH_DB, Config.VALUE_DB_USER)
        self.tech_db_password = self.get_conf(Config.TITLE_TECH_DB, Config.VALUE_DB_PASSWORD)
        self.tech_db_charset = self.get_conf(Config.TITLE_TECH_DB, Config.VALUE_DB_CHARSET)

        self.url_base = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_URL_BASE)

        self.ai_url_base = self.get_conf(Config.TITLE_AI, Config.VALUE_AI_URL_BASE)
        self.ai_url_base_sms = self.get_conf(Config.TITLE_AI, Config.VALUE_AI_URL_BASE_SMS)

        self.oa_url_base = self.get_conf(Config.TITLE_OA, Config.VALUE_OA_URL_BASE)

        self.grow_url_base = self.get_conf(Config.TITLE_Grow, Config.Value_Grow_Base)


    def get_conf(self, title, value):
        """
        配置文件读取
        :param title:
        :param value:
        :return:
        """
        return self.config.get(title, value)

    def set_conf(self, title, value, text):
        """
        配置文件修改
        :param title:
        :param value:
        :param text:
        :return:
        """
        self.config.set(title, value, text)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)

    def add_conf(self, title):
        """
        配置文件添加
        :param title:
        :return:
        """
        self.config.add_section(title)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)


if __name__ == '__main__':
    conf = Config()
    print()