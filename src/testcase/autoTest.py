# -*- coding:UTF-8 -*-
"""
说明：该文件为测试用例文件
      使用方法请阅读“python考试工程补充说明”
"""

from huawei.demo import OlympicsMedalSystem
from huawei import constants
import unittest


class Test(unittest.TestCase):

    def setUp(self):
        super(Test, self).setUp()
        self.Olympics = OlympicsMedalSystem()

    def tearDown(self):
        super(Test, self).tearDown()

    def testCase01(self):

        self.assertEqual(constants.S000, self.Olympics.init())


if __name__ == "__main__":
    unittest.main()
