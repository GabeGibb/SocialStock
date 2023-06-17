from api import get_stock_info, get_stock_tweets
import pandas as pd
from datetime import datetime
from stocks import stocks

def update_info():
  '''Get data from existsing stock tickers for both stock and tweet info, saving them to csv files.'''
  dt = datetime.now()
  x = dt.weekday()
  # print(x)
  if x != 6:
    return
    
  list = []
  for ticker in stocks.keys():
    list.append(get_stock_info(ticker))
  z = pd.concat(list)
  z.to_csv('stock_master.csv', mode='a', index=False, header=False)
  
  
  list = []
  for ticker in stocks.keys():
    list.append(get_stock_tweets(ticker))
  z = pd.concat(list)
  z.to_csv('tweet_master.csv', mode = 'a', index=False, header=False)

# update_info()

