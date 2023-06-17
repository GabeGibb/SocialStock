# stocks = {'AAPL': 0, 'TSLA': 1, 'NFLX': 2, 'MCD': 3, 'MSFT': 4, 'NKE': 5, 'PEP': 6, 'META': 7, 'NVDA': 8, 'AMZN' : 9 }
stocks = {'TSLA': 0, 'NVDA': 1, 'MSFT': 2, 'AAPL': 3, "META": 4, 'GOOGL': 5, 'AMZN': 6, 'AMD': 7, 'GOOG': 8, 'BABA': 9, 'MU': 10, 'COST': 11, 'UNH': 12, 'XOM': 13, 'JNJ': 14, 'ABNB': 15, 'NFLX': 16, 'SCHW': 17, 'AI': 18, 'LLY': 19}

def check_exist(name):
  stock = stocks[name.upper()]
  return stock

