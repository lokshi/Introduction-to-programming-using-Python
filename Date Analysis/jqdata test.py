#!usr/bin/python3
# -*- coding:utf-8 -*-
"""
@project = JoinQuant
@file = Test2
@author = Lok Shi
@create_time = 2018/12/28 15:31
"""


from jqdatasdk import *
auth('13710833445', '000999')
# 查询是否连接成功
is_auth = is_auth()
print(is_auth)

#查看当前jqdatasdk版本
print(__version__)

# 查询当日剩余可调用条数
print (get_query_count())

# # get_all_securities - 获取所有标的信息
# print (get_all_securities(types=['futures'], date=None))
#
# # 将所有股票列表转换成数组
# stocks = list(get_all_securities(['stock']).index)
# print(stocks)
#
# # 获得所有指数列表
# print (get_all_securities(['index']))
#
# # 获得所有基金列表
# df = get_all_securities(['fund'])
# print (df)
#
# # 获取所有期货列表
# print(get_all_securities(['futures']))
#
# # 获得etf基金列表
# df = get_all_securities(['etf'])
# print (df)
#
# # 获得lof基金列表
# df = get_all_securities(['lof'])
# print (df)
#
# # 获得分级A基金列表
# df = get_all_securities(['fja'])
# print (df)
#
# # 获得分级B基金列表
# df = get_all_securities(['fjb'])
# print(df)
#
# # 获得2015年10月10日还在上市的所有股票列表
# print(get_all_securities(date='2020-04-05'))
#
# # 获得2015年10月10日还在上市的 etf 和 lof 基金列表
# print (get_all_securities(['etf', 'lof'], '2020-04-05'))

# print (get_future_contracts('JD'))


df = get_extras('futures_sett_price', ['JD9999.XDCE'], end_date='2020-01-01')
df.to_excel('d:\jd9999.xlsx')