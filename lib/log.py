#!/usr/bin/python3
# -*- coding:utf-8 -*-

import os
import logging
from logging import handlers

#在bash中部使用cat、tail等命令可以看到颜色标记
GREEN = '\033[0;29m%s\033[0m'
WHITE = '\033[0;37m%s\033[0m'
RED = '\033[0;31m%s\033[0m'
BLUE = '\033[0;34m%s\033[0m'

def create_file(filename):
    path = filename[0:filename.rfind('/')]
    if not os.path.isdir(path):
        os.makedirs(path)
    if not os.path.isfile(filename):
        fd = open(filename, mode='w', encoding='utf-8')
        fd.close()
    else:
        pass


class Logger(object):
    level_relations = {\
        'debug':logging.DEBUG,
        'info':logging.INFO,
        'warning':logging.WARNING,
        'error':logging.ERROR,
        'crit':logging.CRITICAL}

    def __init__(self, level='debug', filename='/log/log.log', format='[%(levelname)s - %(asctime)s] %(message)s'):
        self.logger = logging.getLogger()
        self.logger.setLevel(self.level_relations.get(level))#设置打印日志级别
        self.console = logging.StreamHandler()#往屏幕上输出
        self.format = format
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filename = path + filename
        create_file(filename)
        self.file = logging.FileHandler(filename=filename, encoding='utf-8', mode='a+')#往文件里写入

    def font_color(self, color):
        #日志级别颜色标记
        formtter = logging.Formatter(color % self.format)
        self.console.setFormatter(formtter)#设置屏幕上显示的格式
        self.file.setFormatter(formtter)
        self.logger.addHandler(self.console)#把对象加到logger里
        self.logger.addHandler(self.file)
 
    def debug(self, msg, color=WHITE):
        self.font_color(color)
        self.logger.debug(msg)
        self.logger.removeHandler(self.console)
        self.logger.removeHandler(self.file)
 
    def info(self, msg, color=GREEN):
        self.font_color(color)
        self.logger.info(msg)
        self.logger.removeHandler(self.console)
        self.logger.removeHandler(self.file)
 
    def warning(self, msg, color=BLUE):
        self.font_color(color)
        self.logger.warning(msg)
        self.logger.removeHandler(self.console)
        self.logger.removeHandler(self.file)
 
    def error(self, msg, color=RED):
        self.font_color(color)
        self.logger.error(msg)
        self.logger.removeHandler(self.console)
        self.logger.removeHandler(self.file)
 
    def critical(self, msg, color=RED):
        self.font_color(color)
        self.logger.critical(msg)
        self.logger.removeHandler(self.console)
        self.logger.removeHandler(self.file)

if __name__ == '__main__':
    log = Logger()
    log.debug("debug")
    log.info("info")
    log.error("error")
    log.warning("warning")
    log.critical("critical")



