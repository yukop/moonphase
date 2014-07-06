# -*- coding: utf-8 -*-
import tweepy
import ConfigParser
import datetime
import pytz
from astral import *

config = ConfigParser.ConfigParser()
config.readfp(open('twitter.conf'))
consumer_token = config.get('Twitter', 'consumer_token')
consumer_secret = config.get('Twitter', 'consumer_secret')
key = config.get('Twitter', 'key')
secret = config.get('Twitter', 'secret')

auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.secure = True
auth.set_access_token(key, secret)

api = tweepy.API(auth, secure=True, api_root='/1.1')

a = Astral()
city_name = 'Tokyo'
a.solar_depression = 'civil'
city = a[city_name]
timezone = city.timezone

one_day = datetime.timedelta(days=1)
tomorrow = datetime.datetime.now() + one_day

sun = city.sun(date=datetime.datetime.now(), local=True)
sun1 = city.sun(date=tomorrow, local=True)

moonphase = a.moon_phase(datetime.datetime.now(), None)
if moonphase == 0:
  meter = "■■■■■■■■■■■■■■"
elif moonphase == 1:
  meter = "■■■■■■■■■■■■■□"
elif moonphase == 2:
  meter = "■■■■■■■■■■■■□□"
elif moonphase == 3:
  meter = "■■■■■■■■■■■□□□"
elif moonphase == 4:
  meter = "■■■■■■■■■■□□□□"
elif moonphase == 5:
  meter = "■■■■■■■■■□□□□□"
elif moonphase == 6:
  meter = "■■■■■■■■□□□□□□"
elif moonphase == 7:
  meter = "■■■■■■■□□□□□□□"
elif moonphase == 8:
  meter = "■■■■■■□□□□□□□□"
elif moonphase == 9:
  meter = "■■■■■□□□□□□□□□"
elif moonphase == 10:
  meter = "■■■■□□□□□□□□□□"
elif moonphase == 11:
  meter = "■■■□□□□□□□□□□□"
elif moonphase == 12:
  meter = "■■□□□□□□□□□□□□"
elif moonphase == 13:
  meter = "■□□□□□□□□□□□□□"
elif moonphase == 14:
  meter = "□□□□□□□□□□□□□□"
elif moonphase == 15:
  meter = "□□□□□□□□□□□□□■"
elif moonphase == 16:
  meter = "□□□□□□□□□□□□■■"
elif moonphase == 17:
  meter = "□□□□□□□□□□□■■■"
elif moonphase == 18:
  meter = "□□□□□□□□□□■■■■"
elif moonphase == 19:
  meter = "□□□□□□□□□■■■■■"
elif moonphase == 20:
  meter = "□□□□□□□□■■■■■■"
elif moonphase == 21:
  meter = "□□□□□□□■■■■■■■"
elif moonphase == 22:
  meter = "□□□□□□■■■■■■■■"
elif moonphase == 23:
  meter = "□□□□□■■■■■■■■■"
elif moonphase == 24:
  meter = "□□□□■■■■■■■■■■"
elif moonphase == 25:
  meter = "□□□■■■■■■■■■■■"
elif moonphase == 26:
  meter = "□□■■■■■■■■■■■■"
elif moonphase == 27:
  meter = "□■■■■■■■■■■■■■"
elif moonphase == 28:
  meter = "■■■■■■■■■■■■■■"

if moonphase > 29:
  tweet = "うーん。計算できなかったみたい。"
else:
  tweet = 'きょうの月齢は' + str(moonphase) + 'だよ。' + city_name + 'の日没は' + str(sun['sunset'].strftime("%H時%M分%S秒")) + 'くらい、明日の日の出は' + str(sun1['sunrise'].strftime("%H時%M分%S秒")) + 'くらいだよ。' + meter

status = tweet
api.update_status(status)