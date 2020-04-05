import tushare as ts
import openpyxl
import pandas as pd
import time
from openpyxl import load_workbook

#获取数据
ts.set_token('d97bb22c93b7bea7380f0931405ddce310d7f1836cce55731089cb99')
pro = ts.pro_api()
df = pro.fut_basic(exchange='DCE', fut_type='1', fields='ts_code,symbol,name,list_date,delist_date')

print(df)

