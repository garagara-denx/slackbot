# -*- coding: utf-8 -*-

import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import slackAPIkey_settings

# botアカウントのトークンを指定
API_TOKEN = slackAPIkey_settings.API_TOKEN

# デフォルトの返事
DEFAULT_REPLY = "う～ん、よくわかんない！"

# プラグインスクリプトを置いてあるサブディレクトリ名のリスト
PLUGINS = ['plugins']