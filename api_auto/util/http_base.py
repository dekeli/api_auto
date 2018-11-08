# coding=utf-8


__author__ = ""

# 该模块封装属于当前服务的http基本操作
import json, urllib
import requests
from config_file.config_test import ConIni


class BaseHttp(object):
    def __init__(self, env=None):
        """
        :param env: 指定配置文件中的环境名称
        """
        self.env = env

        # 读配置文件，获取host等配置
        my_cfg = ConIni.PPD[env]

        # 声明默认的http对象（声明后才有具体实例）、header（设置后才生效)等
        self.host = my_cfg["host"]

        self.header = my_cfg["header"]

        self.port = my_cfg["port"]

    def get_url(self, url):
        """
        url地址前面需要带上'/'
        :param url:
        """
        if self.port:
            url = self.host + ":" + self.port + url
        else:
            url = self.host + url
        return url

    def get_re(self, url, params=None):
        url = self.get_url(url)
        headers = self.header
        response = requests.get(url, params=params, headers=headers).json()
        return response

    def post_re(self, url, body=None):
        url = self.get_url(url)
        headers = self.header
        if body != None:
            body = json.dumps(body)
        response = requests.post(url, body, headers)
        return response

    def patch_re(self, url, body=None):
        url = self.get_url(url)
        headers = self.header
        if body != None:
            body = json.dumps(body)
        response = requests.patch(url, body, headers)
        return response

    def put_re(self, url, body=''):
        url = self.get_url(url)
        headers = self.header
        body = json.dumps(body)
        response = requests.put(url, body, headers)
        return response

    def delete_re(self, url, body=''):
        url = self.get_url(url)
        headers = self.header
        if body == '':
            response = requests.delete(url)
        else:
            body = json.dumps(body.get())
            response = requests.delete(url, body, headers)
        return response
