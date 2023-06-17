import requests
import yfinance as yf
import pandas as pd
import datetime


def get_stock_info(ticker):
  '''Retrieves stock data and formats it'''
  info = yf.download(tickers=ticker,
                  period="1wk",
                  interval="1d",
                  ignore_tz=True,
                  prepost=False)
  if(info.empty):
    raise Exception
  info = info.drop(columns=['Volume', 'Adj Close'])
  info['ticker'] = ticker
  
  dList = []
  dIntList = []
  for i in info.head().index:
    y, m, d = str(i).split('-')
    d = d.split()[0]
    dt = datetime.datetime(int(y), int(m), int(d))
    dList.append(dt.weekday())
    dIntList.append(dt.year * 10000 + dt.month * 100 + dt.day)

  info['Date'] = dList
  info['DateInt'] = dIntList
  info.drop(index=info.index[0], axis=0, inplace=True)
  return info

def get_stock_tweets(ticker):
  '''Retrieves twitter data and formats it'''
  headers = {
    'Authorization':
    'Bearer AAAAAAAAAAAAAAAAAAAAAMJulgEAAAAA7xfR9wRueDPmDSzSlcny1DJyQGM%3DaeF3XqIVtVIN7Cq0nd5GNbu9PCWGVIgF5KOKUW9Wt7dvdn65OS'
  }
  r = requests.get(
    f'https://api.twitter.com/2/tweets/counts/recent?query={ticker}&granularity=day',
    headers=headers)
  r = r.json()['data']
  
  for i in r:
    dict = i
    dict['start'] = dict['start'][0:10]
    y, m, d = dict['start'].split('-')
    dt = datetime.datetime(int(y), int(m), int(d))
    dict['start'] = dt.weekday()
    dict['DateInt'] = (dt.year * 10000 + dt.month * 100 + dt.day)
    
  r[0]['tweet_count'] += r[-1]['tweet_count']
  r.pop(-1)
  a = pd.DataFrame(r)
  a = a.drop(columns=['end'])
  a['ticker'] = ticker

  return a
