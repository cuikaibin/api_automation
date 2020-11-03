#!/usr/bin/python3
# -*- coding:utf-8 -*-

'''
单接口demo 
'''

import os
import sys
import pytest
import allure
import configparser
from lib.requestBase import RequestBase
from lib.assertion import Assertions
from lib.Config import Config


@allure.feature('英语课后日报')
class TestPytestDemo(object):
    def setup(self):
        #allure.environment(host="172.6.12.27", test_vars=paras)
        #调试单个case使用该路径
        cf = Config()
        url_base = cf.url_base
        self.data = {\
            'userLid': '12614789456ceshijinbishangxian11',
            'lessonLid': '4e746cee84d24ea8bf354ceb722cabac'} 
        self.url = url_base + 'api/app/v1/lesson/report/generateLessonReport'
        self.headers = {"Content-type":"application/json"}
        self.assertion = Assertions()
        self.request = RequestBase()

    @allure.story('test_lesson_report')
    @allure.severity('normal')
    @allure.step('生成课后日报')
    @allure.description('校验课后日报生成接口')
    def test_lesson_report(self):
        result = self.request.get_json(url=self.url, params=self.data, headers=self.headers)
        status_code = self.request.get_status_code(url=self.url, params=self.data, headers=self.headers)
        with allure.step("结果校验"):
            with allure.step("接口返回状态{}".format(status_code)):
                self.assertion.assert_status_code(rq_status_code=status_code, ep_status_code=200)
            with allure.step("coursewareList长度{}".format(len(result["data"]["coursewareList"]))):
                self.assertion.assert_json_list_len(rq_json_list_len=len(result["data"]["coursewareList"]),
                    ep_json_list_len=1, sumbol=">=")

    @allure.story('test_lesson_report1')
    @allure.severity('normal')
    @allure.step('生成课后日报')
    @allure.description('校验课后日报生成接口')
    def test_lesson_report1(self):
        result = self.request.get_json(url=self.url, params=self.data, headers=self.headers)
        status_code = self.request.get_status_code(url=self.url, params=self.data, headers=self.headers)
        with allure.step("结果校验"):
            with allure.step("接口返回状态{}".format(status_code)):
                self.assertion.assert_status_code(rq_status_code=status_code, ep_status_code=200)
            with allure.step("coursewareList长度{}".format(len(result["data"]["coursewareList"]))):
                self.assertion.assert_json_list_len(rq_json_list_len=len(result["data"]["coursewareList"]),
                    ep_json_list_len=1, sumbol="==")

    def teardown(self):
        pass


if __name__ == '__main__':
    pytest.main(['-v', 'test_englist_lesson_report.py'])

