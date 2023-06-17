import pandas as pd
  
def get_io_data(tweetCSV, stockCSV):
  '''Read data, clean out irrelevant information, and format it to feed to our AI'''
  a = pd.read_csv(tweetCSV) 
  # a = a.drop(columns=['ticker'])
  tList = []
  for index, row in a.iterrows():
    if row['start'] != 4 and row['start'] != 5:
      tList.append([row['start'], row['tweet_count'], row['ticker']])
  
  b = pd.read_csv(stockCSV)
  # b = b.drop(columns=['ticker', 'Close', 'High', 'Low'])
  
  sList = []
  for index, row in b.iterrows():
    sList.append([row['Date'], row['Open'], row['ticker']])

  #
  return format_io(sList, tList)


def format_io(stocks, tweets):  
  '''FORMAT DATA FOR AI'''
  input_data = []
  output_data = []
  i = 0
  ticker = tweets[0][2] #AAPL
  tickerNum = 0 #STARTING NUMBER
  for tweet in tweets[:-1]:
    try:
      if ticker != stocks[i+1][2]: #AAPL != newTicker
        ticker = stocks[i+1][2]
        tickerNum += 1
        i += 1
        continue
    except:
      pass
    point = [tweet[1],stocks[i][1], tickerNum]
    
    try:
      output_data.append(stocks[i+1][1])
      input_data.append(point)
      i+= 1
    except:
      continue

  return input_data, output_data

