# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 17:09:59 2020

@author: faisal
"""
 
import pandas as pd
import numpy as np
from yahoofinancials import YahooFinancials

tickers = ['MSFT', 'ORCL', 'AAPL', 'AMD', 'GOOGL', 'NVDA']
tickers_list = []

def create_df (tickers_lst, fromdate, todate):
    for ticker in tickers:
        yf_obs = YahooFinancials (ticker)
        json_obj = yf_obs\
                                    .get_historical_price_data\
                                    (fromdate, todate, 'daily')
        normal = pd.json_normalize(data = json_obj[ticker], \
                                   record_path = 'prices')
        normal['symbol'] = ticker
        normal['simple return'] = normal['adjclose'].pct_change()
        normal['log return'] = np.log(normal['adjclose']/normal['adjclose'].shift(1))
        tickers_list.append(normal)

    tickers_df = pd.concat(tickers_list)
    return tickers_df

df = create_df(tickers, '2010-01-01', '2019-12-31')
print (df)