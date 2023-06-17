from flask import Flask
from ai import predict
from stocks import check_exist
from api import get_stock_info, get_stock_tweets
from apscheduler.schedulers.background import BackgroundScheduler
from get_info import update_info

#Backend app with endpoints to get specific information
app = Flask(__name__)

@app.route('/')
def home():
  return {'state': 'It is working!'}

@app.route('/search/<name>')
def search(name):
  search = check_exist(name)
  return f'{search}'


@app.route('/stock_info/<name>')
def stock_info(name):
  info = get_stock_info(name).drop(columns=['ticker'])
  info = info.values.tolist()
  return info

@app.route('/tweet_info/<name>')
def tweet_info(name):
  info = get_stock_tweets(name).drop(columns=['ticker'])
  info = info.values.tolist()
  return info

@app.route('/predict/<tweetCount>/<stockPrice>/<tickerNum>')
def getPrediction(tweetCount, stockPrice, tickerNum):
  prediction = predict(tweetCount, stockPrice, tickerNum)
  return f'{prediction}'


sched = BackgroundScheduler()
sched.add_job(update_info,'interval',hours=12)
sched.start()

app.run(host = "0.0.0.0")