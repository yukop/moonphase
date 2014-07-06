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
tokyo = a[city_name]
timezone = tokyo.timezone

jstnow = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
one_day = datetime.timedelta(days=1)
tomorrow = jstnow + one_day

day1 = tokyo.sun(date=jstnow, local=True)
day2 = tokyo.sun(date=tomorrow, local=True)

moonphase = a.moon_phase(jstnow, None)
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
  tweet = meter + ' ' + jstnow.strftime("%-m月%-d日") + 'の月齢は' + str(moonphase) + 'くらいだよ。' + city_name + 'の日没はだいたい' + str(day1['sunset'].strftime("%-H時%-M分%-S秒")) + '、明日の日の出はだいたい' + str(day2['sunrise'].strftime("%-H時%-M分%-S秒")) + 'だよ。'

status = tweet
api.update_status(status)