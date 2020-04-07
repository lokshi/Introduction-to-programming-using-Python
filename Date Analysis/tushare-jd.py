import tushare as ts
import openpyxl
import pandas as pd
import time
from openpyxl import load_workbook

#获取数据
pro = ts.pro_api('8334c8fbee17f385a1ee4f2419818439ba5f99b611059a6ed2c3c8c7')

#获取CU1811合约20180101～20181113期间的行情
df = pro.fut_daily(ts_code='JD.DCE', start_date='20150101', end_date='20200407')

df.to_excel('d:\jd.xlsx')

#print(df)
