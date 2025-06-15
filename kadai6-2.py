# ■ 参照するオープンデータ
# オープンデータ名: HeartRails Express API
# 概要:
#   株式会社ハートレイルズが提供する、日本の地理・交通情報に関する無料のWeb API群。
#   今回はこの中から、指定した路線名に属する駅の一覧を取得する機能を利用する。
# ■ エンドポイントと機能
# エンドポイント: http://express.heartrails.com/api/json
# 機能:
#   GETリクエストで、methodパラメータに 'getStations' を指定し、
#   lineパラメータに路線名を渡すことで、その路線の駅データをJSON形式で取得する。
#   (例: JR山手線、JR総武線など)
# ■ 使い方
#   以下のURLにアクセスすることで、JR山手線の駅一覧が取得できる。
#   http://express.heartrails.com/api/json?method=getStations&line=JR山手線

import requests
import pandas as pd

# HeartRails Express APIのエンドポイントURL
API_URL  = "http://express.heartrails.com/api/json"

params = {
    "method": "getStations",
    "line":"JR総武線",
}

response = requests.get(API_URL, params=params)
# Process the response
data = response.json()

stations = data['response']['station']

df = pd.DataFrame(stations)

print(df)