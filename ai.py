from format_data import get_io_data
# from sklearn import svm
from sklearn import tree


i, o = get_io_data('tweet_master.csv', 'stock_master.csv')


model = tree.DecisionTreeRegressor()
model.fit(i, o)

def predict(tweetCount, stockPrice, tickerNum):
                      #Tweets, Stock price, Stock ticker
  predict = model.predict([[tweetCount, stockPrice, tickerNum]])
  return predict[0]


#PREVIOUS DAY STOCK PRICE, PREVIOUS DAY TWEET COUNT, TICKERNUM -> TOMORROW STOCK PRICE

#    stock price, tweets, ticker num
# input_data = [[123.2, 5400, 3], [321.2, 10000, 1]]
# output_data = [120.31, 324.22]

