# coding: utf-8

import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import run_tweet
from slackbot.bot import respond_to
from slackbot.bot import listen_to

# Slackに投稿した内容をツイートする
@respond_to(r'^tweet\s+\S.*')
def tweet(message):
    # Slackに投稿されたメッセージを取り出す
    text = message.body['text']

    # Slackに投稿された文字列のうち"tweet "以降の文字列を取り出しwordに格納する
    # cmdに"tweet ",wordに投稿されるツイートの本文が入る
    cmd, word = text.split(None, 1)
    run_tweet.post_tweet(word)
    msg = 'ツイートしたよ！\n```' + word + '```'
    message.reply(msg)

# ツイッターからタイムラインを取得してSlack上に表示
@respond_to(r'timeline')
def get_timeline(message):
    timeline = run_tweet.get_timeline()
    msg = 'たいむらいん取って来たよ！\n```' + timeline + '```'
    message.reply(msg)

# お寿司食べたい！
@listen_to(r'[sS][uU][sS][hH][iI]|寿司|すし|スシ')
def sushi_listen(message):
    message.send('お寿司たべたい！')      # ただの投稿


@respond_to(r'[sS][uU][sS][hH][iI]|寿司|すし|スシ')
def sushi_respond(message):
    message.send('お寿司たべたい！')      # ただの投稿

@respond_to(r'.?chinchin*|.?ちんちん')
def chinchin_respond(message):
    message.send('おちんちん！')