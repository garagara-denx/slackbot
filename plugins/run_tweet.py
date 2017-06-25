#coding: UTF-8

import os
import sys
from requests_oauthlib import OAuth1Session
import json
sys.path.append(os.pardir)
import twitterAPIkey_settings
from datetime import datetime
import codecs

sys.path.append(os.getcwd() + '/modules')

#自分のツイッターアカウントを取得
twitter = OAuth1Session(twitterAPIkey_settings.CONSUMER_KEY,
                        twitterAPIkey_settings.CONSUMER_SECRET,
                        twitterAPIkey_settings.ACCESS_TOKEN,
                        twitterAPIkey_settings.ACCESS_TOKEN_SECRET)

#ツイッターAPI
url_timeline = "https://api.twitter.com/1.1/statuses/home_timeline.json"
url_text = "https://api.twitter.com/1.1/statuses/update.json"
url_media = "https://upload.twitter.com/1.1/media/upload.json"

##タイムラインを取得して表示(Slack用)
def get_timeline():
  params = {}
  req = twitter.get(url_timeline, params = params)

  timeline = json.loads(req.text)
  print(timeline)

  for tweet in timeline:
      print("・" + tweet["text"])

  timeline_text = ''

  for tweet in timeline:
    userName = str(tweet["user"]["name"])
    text = str(tweet["text"])
    timeline_text += userName + " : " + text + '\r\n'

  return timeline_text

##ツイートする
def post_tweet(text):
  params = {"status": str(text)}
  req = twitter.post(url_text, params = params)

##ツイートする(テスト用)
def post_tweet_test():
  params = {"status": "テストだよ！"}
  req = twitter.post(url_text, params = params)

## 画像を投稿する
#故障中
def media_tweet(text, image_path):

  files = {"media" : open(image_path, 'rb')}
  req_media = twitter.post(url_media, files = files)

  print(req_media.status_code)

  # レスポンスを確認
  if req_media.status_code != 200:
      print ("画像アップデート失敗: %s", req_media.text)
      exit()

  # Media ID を取得
  media_id = json.loads(req_media.text)['media_id']

  # Media ID を付加してテキストを投稿
  params = {'status': text, "media_ids": [media_id]}
  req_media = twitter.post(url_text, params = params)

  # 再びレスポンスを確認
  if req_media.status_code != 200:
      print ("テキストアップデート失敗: %s", req_text.text)
      exit()

if __name__ == '__main__':
  print("test")