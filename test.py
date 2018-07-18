from futuquant import *
import pandas as pd
import numpy as np
import mysql.connector
import sqlite3
import matplotlib.pyplot as plt
import pylab as pl

def get_stockID(stockCode):
    quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
    lines = quote_ctx.get_stock_basicinfo(Market.HK, SecurityType.STOCK)
    df = lines[1]
    stockId = (df.loc[df['code'] == stockCode])['stock_id'].to_string(index = False) 
    quote_ctx.close()
    return stockId

cMysql = mysql.connector.connect(
         user='root',
         password='root',
         host='127.0.0.1',
         database='scrapy')
cursorMysql = cMysql.cursor()

sql = "SELECT * FROM aastock;"

cursorMysql.execute(sql)

results = cursorMysql.fetchall()

stockID = get_stockID('HK.'+results[0][2][0:5])

connSqlite = sqlite3.connect("D:\\ft_hist_data\\hist_hk\hknor_kl_day_0.db")

cursorSqlite = connSqlite.cursor()

sql2 = "SELECT date(time_desc) FROM KLData where stock_id = %s limit 10;" % stockID
sql3 = "SELECT close_price FROM KLData where stock_id = %s limit 10;" % stockID

cursorSqlite.execute(sql2)

x = cursorSqlite.fetchall()

tDate = []
cPrice = []

for a in x:
    tDate.append(a[0])


cursorSqlite.execute(sql3)
y = cursorSqlite.fetchall()

for b in y:
    cPrice.append(b[0])

print(tDate)
print(cPrice)
