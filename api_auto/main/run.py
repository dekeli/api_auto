#coding:utf-8
import unittest
from unit_test.test_unnitest import Test
from util import HTMLTestRunner

class Runmain():

    def run_case(self):
        suite = unittest.TestSuite()

        # 2种用法：第二种suite.addTests()
        suite.addTests(map(Test, ["test_get_your_request", "XXXXXX"]))


        # 输出结果：测试结果直接输出在控制台
        # unittest.TextTestRunner().run(suite)

        # 输出结果：将测试结果以report.html形式生成
        st = open('../report/report.html','wb')
        HTMLTestRunner.HTMLTestRunner(stream=st,title=u'接口自动化测试报告',description=u'测试者：songyaqi').run(suite)


if __name__ == '__main__':
    run = Runmain()
    run.run_case()
