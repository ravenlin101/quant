from futuquant import *
import pandas as pd
import numpy as np
def get_stockId(stockCode):
    quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
    lines = quote_ctx.get_stock_basicinfo(Market.HK, SecurityType.STOCK)
    df = lines[1]
    stockId = (df.loc[df['code'] == stockCode])['stock_id'].to_string(index = False) 
    quote_ctx.close()
    return stockId
