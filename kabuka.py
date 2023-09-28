# 教育訓練用題材
# 株価取得　時系列データ作成PG
# nakamori '23/6
#  input:株式銘柄コードF(複数銘柄)
#  output:株価時系列データF
#  create '23.xx.xx
#  s.nakamori
import os
import time
import glob
import pandas as pd
import openpyxl
import re
from bs4 import BeautifulSoup
import requests
from math import pi as ppi
import math
import csv
import datetime
import logging

# Pandas DataFrameを徹底解説
# https://ai-inter1.com/pandas-dataframe_basic/#st-toc-h-26

# ログの設定
# logging.basicConfig(filename='./app.log', level=logging.INFO,
#                     format='%(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(filename='./app.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
print("PG Start")

# ##########################
def printrem():
    print("##########################")
# ##########################
# csvデータ読込　銘柄コード
def read_csv():
    a = 0
    with open('./stocklst.csv', 'r') as f:
        reader = csv.reader(f)
        printrem()
        print(reader)

        ret = []
        for line in reader:
            ret.append(line)
            print(line)
        return ret
# ##########################
def convert_to_numeric(variable):
    if isinstance(variable, str) and variable.isnumeric():
        return int(variable)  # 文字列が数値の場合、int型に変換して返す
    elif isinstance(variable, str) and variable.replace('.', '', 1).isdigit():
        return float(variable)  # 文字列が浮動小数点数の場合、float型に変換して返す
    else:
        return variable  # 数値型でない場合はそのまま返す
# ##########################
# ファイルが無い時作成する
def create_file_if_not_exists(file_path):
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            # ファイルに初期データを書き込む場合は以下の行を追加します
            f.write("")
            logging.info(f"ファイル '{file_path}' が作成されました。")
# ##########################
# CSVに追記する
def append_to_csv(file_path, data):
    # CSVファイルを読み込む
    try:
        inid = pd.read_csv(file_path, encoding="SHIFT-JIS")
        existing_data = inid
    except pd.errors.EmptyDataError:
        logging.info("ファイルにデータがありません。")
        existing_data = pd.DataFrame()
        # existing_data = existing_data.drop(existing_data.index)
    except FileNotFoundError:
        logging.info('ファイルが見つかりません。')
        raise Exception("ファイルが見つかりません。")

    # existing_data = pd.read_csv(file_path)
    logging.info('data')
    logging.info(data)
# データをDataFrameに変換して追記する
    # new_data = pd.DataFrame(data)
    new_data = data
    logging.info('new_data')
    logging.info(new_data)

    updated_data = pd.concat([existing_data, new_data],
                             axis=0, ignore_index=True)

    # 追記した結果をCSVファイルに書き込む
# "shift-jis"出力
    updated_data.to_csv(file_path, index=False, encoding="shift-jis")

# ##########################
# みんかぶのウェブサイトから指定の株価を取得するためのサンプルコード
# https://www.youtube.com/watch?v=LgZ8Li97yoM
def get_stock_price(stock_code):
    # 株価情報を取得するURL
    url = f'https://minkabu.jp/stock/{stock_code}'

    # リクエストを送信してHTMLを取得
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    print(type(soup))
    print("---title---:", soup.title)

    # 株価を抽出
    # 文字’円’を’’に置換する
    stock_price = soup.find(
        'td', class_='ly_vamd_inner ly_colsize_9_fix fwb tar wsnw').text
    stock_name = soup.find(
        'div', class_='md_card_ti').text
    loc = stock_name.split("の")

    return loc[0] + "  " + stock_price
# ##########################

meigaralst = read_csv()

meigaralist = []
pricelist = []
namelist = []
dtnows = []

for i in meigaralst:
    price = get_stock_price(i[0])
    chars_to_exclude = "[円]"
    price = re.sub(chars_to_exclude, "", price)

    printrem()
    meigaralist.append(i[0])
    temp = price.split("  ")
    print("tt:", temp)
    # ","除去
    chars_to_exclude = ","
    temp[1] = re.sub(chars_to_exclude, "", temp[1])

    logging.debug('price')
    logging.debug(temp[1])

    pricelist.append(temp[1])
    # 改行コード除去
    chars_to_exclude = "\n"
    temp[0] = re.sub(chars_to_exclude, "", temp[0])

    namelist.append(temp[0])
    dtnows.append(datetime.datetime.now())

dtStoks = pd.DataFrame(
    {'datetime': dtnows, 'meigaraCD': meigaralist, 'name':  namelist, 'price': pricelist})

printrem()
print(dtStoks)

outFileName = './dtStoksnonullC.csv'
# 無効データ削除
dtStoksnonull = dtStoks.dropna(how="any")
# CSV書き出し
dtStoksnonull.to_csv('./dtStoksnonullB.csv')
# CSV書き出し追記
create_file_if_not_exists(outFileName)
append_to_csv(outFileName, dtStoks)

# --------------------------------------------

print("-------PG End------")
