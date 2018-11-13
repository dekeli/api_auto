#coding:utf-8
import unittest
from api_call.your_service import NbService
from hamcrest import *
from util.check_response import ResponseCheck

class Test(unittest.TestCase):

    # 每次方法前执行
    def setUp(self):
        # 建议存放一些公有变量、做数据初始化或者数据准备
        self.nb_o = NbService()
        self.response_o = ResponseCheck()
        self.xx_id = ""  # 示例：某个ID，在下面test_case中使用
        self.request_params = {"tmoffset": -8, "time": "1541683952993", "channelId": "57ce7f9c7732d6dab5ea16b6",
                               "orderBy": "subscribeTime", "ordering": 'DESC', "page": 1, "per-page": 20,
                               "searchKey": 'qun2',
                               "subscribeStatus": "SUBSCRIBED,UNSUBSCRIBED"}

    # 每次方法后执行，一般用不到
    def tearDown(self):
        pass

    def test_get_your_request(self):
        res = self.nb_o.get_your_request(request_params=self.request_params)
        res_code = res.status_code # 返回状态码
        assert res_cde == 200
        res_body = res.text # 返回内容
        print(res)
        # dict_o = self.response_o(res, 200,"jshdjshdj")
        # print(dict_o)
        # 断言：假设返回结果有以下字段
        # assert_that(dict_o, has_key("id"))
        # assert_that(dict_o, has_key("number"))




