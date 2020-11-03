#!/user/bin/python3
#encoding: utf-8

"""
File:request_base.py 
Anthor: cuikaibin
Date: 2020/5/12
"""

import traceback
import operator
from lib.log import Logger

class Assertions:
    """
    @summary  封装assert模块
    """
    def __init__(self):
        self.log = Logger()

    def assert_status_code(self, rq_status_code, ep_status_code):
        """
        @summary  校验返回状态码
        @param    rq_status_code  nu  实际请求码
        @param    ep_status_code  nu  期望请求码
        """
        # try:
        #     assert rq_status_code == ep_status_code
        #     return True
        # except Exception:
        #     self.log.error('请求status_code返回值是{},和预期结果{}不符合'.format(rq_status_code, ep_status_code))
        #     return False
        self.log.info('请求status_code返回值是:{},预期结果是:{}'.format(rq_status_code, ep_status_code))
        assert rq_status_code == ep_status_code
    
    def assert_json_value(self, rq_json_value, ep_json_value):
        """
        @summary  校验json中键对应的值是否正确
        @param    rq_json_value  任意类型的值  实际值
        @param    ep_json_value  任意类型的值  期望值
        """        
        # try:
        #     assert rq_json_value == ep_json_value
        #     return True
        # except Exception as e:
        #     self.log.error('请求返回值为{},和预期结果{}不符合'.format(rq_json_value, ep_json_value))
        #     return False
        self.log.info('请求返回值为:{},预期结果为:{}'.format(rq_json_value, ep_json_value))
        assert rq_json_value == ep_json_value

    def assert_json_list_len(self, rq_json_list_len, ep_json_list_len, sumbol):
        """
        @summary  校验json中键对应list的长度
        @param    rq_json_list_len  nu  实际长度
        @param    ep_json_list_len  nu  期望长度
        @param    sumbol 比较运算符  
        """ 
        mappings = {'<':operator.lt,
            '<=':operator.le,
            '>':operator.gt,
            '>=':operator.ge,
            '==':operator.eq,
            '!=':operator.ne}
        # try:
        #     assert mappings[sumbol](rq_json_list_len, ep_json_list_len)
        #     return True
        # except Exception:
        #     self.log.error('请求结果返回长度为{},期望结果为{},不符合预期'.format(rq_json_list_len, ep_json_list_len))
        #     return False
        self.log.info('请求结果返回长度为:{},期望结果为:{}'.format(rq_json_list_len, ep_json_list_len))
        assert mappings[sumbol](rq_json_list_len, ep_json_list_len)

    def assert_json_value_not_null(self, rq_json_value):
        """
        @summary  校验json中键对应的值是否为空
        @param    rq_json_value  任意格式  实际值
        """
        # try:
        #     assert rq_json_value != null
        #     return True
        # except Exception as e:
        #     self.log.error('请求结果返回值为空,不符合预期')
        #     return False
        self.log.info('字段返回值为:{}'.format(rq_json_value))
        assert rq_json_value != ''


if __name__ == '__main__':
    Assertions().assert_status_code(rq_status_code=200, ep_status_code=200)








