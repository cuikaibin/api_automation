#!/user/bin/python3
#encoding: utf-8

"""
File:request_base.py 
Anthor: cuikaibin
Date: 2020/5/12
"""

import os
import sys
import json
import traceback
import requests
from lib.log import Logger

class RequestBase(object):
    """
    @summary 封装request模块
    """
    def __init__(self):
        self.log = Logger()
        #self.cookid = dict(anonymid=jk63khrk-y97r4p; _r01_=1; ln_uact=mr_mao_hacker@163.com)

    def get_json(self, **kw):
        """
        @summary  get请求返回结果处理为json
        @param    kw    request请求的参数
        @return   返回处理后的请求结果 
        """
        try:
            request = requests.get(**kw)
            result = request.json()
            self.log.info('GET请求返回json为:\n{}'.format(result))
            return result
        except Exception:
            self.log.error('发送GET请求,json结果解析失败，错误堆栈:\n{}'.format(traceback.format_exc()))

    def post_json(self, **kw):
        """
        @summary  post请求返回结果处理为json
        @param    kw    request请求的参数 
        @return   返回处理后的请求结果        
        """
        try:
            request = requests.post(**kw)
            result = request.json()
            self.log.info('POST请求返回json为:\n{}'.format(result))
            return result
        except Exception as e:
            self.log.error('发送POST请求,并将结果解析json失败,错误堆栈:\n{}'.format(traceback.format_exc()))

    def get_status_code(self, **kw):
        """
        @summary  get请求状态码
        @param    kw    request请求的参数 
        @return   返回处理后的请求结果       
        """
        try:
            request = requests.get(**kw)
            result = request.status_code
            self.log.info('GET请求返回status_code为:\n{}'.format(result))
            return result
        except Exception:
            self.log.error('发送GET请求,并获取请求状态失败,错误堆栈:\n{}'.format(traceback.format_exc()))

    def post_status_code(self, **kw):
        """
        @summary  post请求状态码
        @param    kw    request请求的参数 
        @return   返回处理后的请求结果        
        """
        try:
            request = requests.post(**kw)
            result = request.status_code
            self.log.info('POST请求返回status_code为:\n{}'.format(result))
            return result
        except Exception:
            self.log.error('发送POST请求,并获取请求状态失败,错误堆栈:\n{}'.format(traceback.format_exc()))

    def get_text(self, **kw):
        """
        @summary  get请求返回结果处理为text
        @param    kw    request请求的参数
        @return   返回处理后的请求结果 
        """
        try:
            request = requests.get(**kw)
            result = request.text
            self.log.info('GET请求返回text为:\n{}'.format(result))
            return result
        except Exception:
            self.log.error('发送GET请求,并将结果解析text失败,错误堆栈:\n{}'.format(traceback.format_exc()))

    def post_text(self, **kw):
        """
        @summary  post请求返回结果处理为text
        @param    kw    request请求的参数 
        @return   返回处理后的请求结果 
        """
        try:
            request = requests.post(**kw)
            result = request.text
            self.log.info('POST请求返回text为:\n{}'.format(result))
            return result
        except Exception:
            self.log.error('发送POST请求,并将结果解析text失败,错误堆栈:\n{}'.format(traceback.format_exc()))

    def post_multipart(self, url, files):
        """
        @summary  post请求表单上传
        @param    url  str  请求url
        @param    file 文件存储路径 
        @return   返回处理后的请求结果 
        """
        try:
            files = {'file': (file, 'rb')}
            result = requests.post(url=url, files=files)
            return result
        except Exception:
            self.log.error('POST表单上产失败,错误堆栈:\n{}'.format(traceback.format_exc()))

    def delete_json(self, **kw):
        """
        @summary  delete请求返回结果处理为json
        @param    kw    request请求的参数
        @return   返回处理后的请求结果 
        """
        try:
            request = requests.delete(**kw)
            result = request.json()
            self.log.info('delete请求返回json为:\n{}'.format(result))
            return result
        except Exception:
            self.log.error('发送delete请求,json结果解析失败，错误堆栈:\n{}'.format(traceback.format_exc()))


if __name__ == '__main__':
    data = {\
        'userLid': '12614789456ceshijinbishangxian11',
        'lessonLid': '4e746cee84d24ea8bf354ceb722cabac'} 
    #request_data = json.dumps(data)
    headers = {"Content-type":"application/json"}
    request =  RequestBase()
    url = 'https://test-monkeyabc.xueersi.com/api/app/v1/lesson/report/generateLessonReport'
    result = request.get_json(url=url, params=data, headers=headers)
    print (result)




