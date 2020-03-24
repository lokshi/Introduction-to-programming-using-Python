import tushare as ts
import openpyxl
import pandas as pd
import time
from openpyxl import load_workbook

#获取数据
ts.set_token('d97bb22c93b7bea7380f0931405ddce310d7f1836cce55731089cb99')
pro=ts.pro_api()
# df=pro.ncov_num(level=2,fields="ann_date,confirmed_num,confirmed_num_now,suspected_num_now,cured_num,dead_num")
df=pro.ncov_num(level=2)
df.rename(columns={'ann_date':'发布日期','area_name':'地区名称','parent_name':'上一级地区','level':'级别','confirmed_num':'累计确诊人数','suspected_num':'累计疑似人数','confirmed_num_now':'现有确诊人数','suspected_num_now':'现有疑似人数','cured_num':'累计治愈人数','dead_num':'累计死亡人数'},inplace=True) #修改表头
df.to_excel('d:\cov_num2.xlsx')

#打开获取到本地的数据文件
