#!/usr/bin/python3
# -*- coding:utf-8 -*-

'''
依赖接口demo
1、其中pushTeacherRemark依赖generateLessonReport接口返回的teacherRemarkFlag值作为请求参数，
   teacherRemarkFlag用例表示老师是否已经点评
2、generateLessonReport接口teacherRemarkFlag值依赖，辅导端老师调用pushTeacherRemarkMsg推送
   点评是否完成
'''

import os
import sys
import json
import pytest
import allure
import configparser
from lib.requestBase import RequestBase
from lib.assertion import Assertions
from lib.log import Logger

def generate_lesson_report_and_teacher_remake(request, data, url1, url2, **wk):        
    generate_lesson_report_result = request.get_json(params=data, url=url1, **wk)
    generate_lesson_report_teacherRemarkFlag = generate_lesson_report_result["data"]["teacherRemarkFlag"]
    data["teacherRemarkFlag"] = generate_lesson_report_teacherRemarkFlag
    teacher_remake_result = request.get_json(params=data, url=url2, **wk)
    teacher_remake_statusText = teacher_remake_result["statusText"]
    return generate_lesson_report_teacherRemarkFlag, teacher_remake_statusText


@allure.feature('英语课后日报')
class TestPytestDemoRelyApi(object):
    def setup(self):
        path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
        conf_path = path + "/conf/demo.conf"
        cf = configparser.ConfigParser()
        cf.read(conf_path)
        url_base = cf.get('english', 'url_base')
        self.log = Logger()
        self.request = RequestBase()
        self.assertion = Assertions()
        self.data = {\
            'userLid': '12614789456ceshijinbishangxian11',
            'lessonLid': '4e746cee84d24ea8bf354ceb722cabac'} 
        self.headers = {"Content-type":"application/json"}
        self.url1 = url_base + 'api/app/v1/lesson/report/generateLessonReport'
        self.url2 = url_base + 'api/app/v1/lesson/report/pushTeacherRemark'
        self.url3 = url_base + 'api/app/v1/lesson/report/pushTeacherRemarkMsg'

    @allure.story('test_lesson_report')
    @allure.severity('normal')
    @allure.step('生成课后日报')
    @allure.description('校验课后日报生成接口')
    def test_lesson_report(self):
        result = generate_lesson_report_and_teacher_remake(request=self.request, data=self.data, 
            url1=self.url1, url2=self.url2, headers=self.headers)
        self.log.debug("请求结果为{}".format(result))

        with allure.step("结果校验"):
            with allure.step("课后报告返回值{}".format(result[0])):
                self.assertion.assert_json_value(rq_json_value=result[0], ep_json_value=0)
            with allure.step("老师点评状态{}".format(result[1])):
                self.assertion.assert_json_value(rq_json_value=result[1], ep_json_value="OK")

    @allure.story('test_lesson_report1')
    @allure.severity('normal')
    @allure.step('生成课后日报')
    @allure.description('校验课后日报生成接口')
    def test_lesson_report1(self):
        data = {\
            "lessonLid": "4e746cee84d24ea8bf354ceb722cabac",
            "remarkTime": 1585388032555,
            "teacherName": "jinjin",
            "userLid": "12614789456ceshijinbishangxian11"}
        data = json.dumps(data)

        result1 = self.request.post_json(url=self.url3, data=data, headers=self.headers)
        self.log.debug("老师点评push接口返回结果:{}".format(result1))
        result2 = generate_lesson_report_and_teacher_remake(request=self.request, data=self.data, 
            url1=self.url1, url2=self.url2, headers=self.headers) 
        self.log.debug("日报老师点评返回结果:{}".format(result2))      

        with allure.step("结果校验"):
            with allure.step("老师点评push返回状态{}".format(result1["statusText"])):
                self.assertion.assert_json_value(rq_json_value=result1["statusText"], ep_json_value="OK")
            with allure.step("课后报告返回值{}".format(result2[0])):
                self.assertion.assert_json_value(rq_json_value=result2[0], ep_json_value=1)

    def teardown(self):
        pass


if __name__ == '__main__':
    pytest.main(['-v', 'test_report_and_remark.py'])
