from util.http_base import *

class NbService(BaseHttp):
    def __init__(self, env="test"):
        """
        初始化方法
        各个接口方法封装中需要的公共内容
        """
        BaseHttp.__init__(self, env=env)

    # ------------------ v1.0 ------------------- #
    def get_your_request(self, request_params):
        """
        GET /v1/your/request
        获取配置
        请求参数：request_params(假如需要传get请求的参数)
        :return: 无
        """
        url = '57ce4182905e887f7b8b456c/api/channel/followers'
        response = self.get_re(url=url, params=request_params)
        return response

    def get_your_request_2(self, request_params):
        """
        GET /v1/your/request
        获取配置
        请求参数：request_params(假如需要传get请求的参数)
        :return: 无
        """
        url = '/search_api/'
        response = self.get_re(url=url, params=request_params)
        return response

    def post_your_request(self, data):
        url = '/v1/your/request'
        response = self.post_re(url=url,body=data)
        return response


