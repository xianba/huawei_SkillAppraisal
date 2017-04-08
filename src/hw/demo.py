# -*- coding:UTF-8 -*-
"""
说明：该文件为考试工程主体文件
      使用方法请阅读“python考试工程补充说明”
"""


import constants

class OlympicsMedalSystem:
    '''
    说明：
    （1）考生需要根据考题要求，实现相应的接口。可以根据需要增加变量或方法。
    （2）constants.py文件中已经预定义了一些常量值，测试用例会引用这些常量。涉及到这些常量，考生应该直接引用。
    （3）接口返回成功或失败代码时，请直接返回预定义的常量。如：return constants.E001
    '''


    def init(self):
        '''
        系统初始化
        :return: 返回操作成功或失败的代码
        '''

        return constants.S000


    def input_medal_record(self, time, country, player, subject, medal):
        '''
        录入竞赛成绩
        :param time: 系统时间(int)
        :param country: 国家(string)
        :param player: 运动员名字(string)
        :param subject: 运动项目(int)
        :param medal: 奖牌级别(int)
        :return: 返回操作成功或失败的代码
        '''

        return constants.S001


    def cancel_medal_record(self, time, player, subject):
        '''
        取消成绩
        :param time: 系统时间(int)
        :param player: 运动员名字(string)
        :param subject: 运动项目(int)
        :return: 返回操作成功或失败的代码
        '''

        return constants.S002


    def query_country_medal_rankings(self):
        '''
        查询国家奖牌排行榜
        :param time: 系统时间(int)
        :return: ret: 返回操作成功或失败的代码
        :return: info: 返回排名信息，格式为列表，列表的元素为字典，结构如下所示：
        [
        {
            'country': 'China',     #国家
            'gold': 58              #金牌
            'silver': 58            #银牌
            'bronze': 12,           #铜牌
            'ranking': 1,           #排名
        }
        ]

        '''
        ret = constants.S003
        info = list()

        return ret, info
