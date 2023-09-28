# 教育訓練用題材
# 株価取得　時系列データ作成PG
# nakamori '23/6
#  input:株式銘柄コードF(複数銘柄)
#  output:株価時系列データF
#  create '23.xx.xx
#  s.nakamori 

from tqdm import tqdm
import re
from bs4 import BeautifulSoup
import requests
from math import pi as ppi
import math
import csv
import datetime
import logging
import numpy as np
# Pandas DataFrameを徹底解説
# https://ai-inter1.com/pandas-dataframe_basic/#st-toc-h-26

# ログの設定
# logging.basicConfig(filename='./app.log', level=logging.INFO,
#                     format='%(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(filename='./app.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class User:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)

import sys
# -------------------------------------------
# プログレスバー
for _x in tqdm(range(10**7)):
    pass
# -------------------------------------------
# https: // www.youtube.com/watch?v = LTH3vNcMgsk
sales2020 = [400239,56213,542490]
sales2019 = [489028, 400123, 442489]

for cur, pre in zip(sales2020, sales2019):
    rer = cur/pre*100
    print(f'{cur} /{pre} /{rer:.1f}%')


for i, n in enumerate(sales2019,start=1):
    print(f'{i}# {n}')

print('****************************')
print('****************************')
print(sys.path)

user_s = User('佐藤')
user_t = User('田中')

user_s.display()
user_t.display()

# exit

xr = np.array([0, 204, 2, 3])
xr2 = np.array([0, 204, 2, 3])

print(type(xr+xr2))
print(xr+xr2)

print("helloPython")
print("hog+heg")
hog = 1
heg = 2
print(hog)
print(heg)
print(hog+heg)

print("while")
i = 0
while i < 6:
    print(i)
    i += 1
print("for")
for i in [1, 2, 3, 4, 5, 10]:
    print(i)
print("dic")
# dic2 = {"�ｿｽ�ｿｽ�ｿｽ": 300, "�ｿｽﾈゑｿｽ": 50, "�ｿｽﾆまゑｿｽ": 20, "�ｿｽﾈゑｿｽ": 40}
dic = {"りんご": 300, "なし": 50, "とまと": 20, "なす": 40}
for x in dic:
    print(x, dic[x])
print("func")


def func1(arg1, arg2):
    return arg1 * arg2


print(func1(1, 10))
print(func1(2, 20))
print(func1(3, func1(2, 20)))


print(math.pi)


print(ppi)

print(1 != 1)
print("for")
for i in range(4):
    print(i)

ff = func1

print(ff(3, 5))
print(ff(6, 5))

print("class")
class Student:
    def __init__(self,name) :
        self.name = name
    def avg(self,math,english):
        print((math+english)/2)


a001 = Student("sato")
print(a001.name)
a001.avg(7,9)

a002 = Student("tanaka")
print(a002.name)

print("lamda")

nums = [100, 200, 50, 40]

for num in (nums):
    print(num ,"ok" if num > 50 else "bad")

results = filter(lambda num: num > 90,nums)

ret = list(results)
print(list(ret))
print(type(ret))


for res in (ret):
    print(res)

import openpyxl
import pandas as pd
import glob
        
ans = ["uru", "!uru"]


in_line = int(input())
print(type(in_line))

if in_line%4 == 0:
    if in_line % 100 == 0:
        if in_line % 400 == 0:
            print(ans[0])
        else:
            print(ans[1])
    else:
        print(ans[0])
else:
    print(ans[1])




# for i in range(in_line):
    # print("in=",i)
print("webdriver")
from selenium import webdriver
import time
import os
import datetime
# ##########################


def printrem():
    print("##########################")

def captweb():
    # クロームの立ち上げ
    driver = webdriver.Chrome()

    # ページ接続
    driver.get('https://www.conoha.jp/conoha/')

    # 5秒終了を待つ
    time.sleep(5)

    # 画面キャプチャを取得
    cyap = driver.save_screenshot('./conoha.png')
    print("------------- 画面キャプチャ is ", cyap)

    # クロームの終了処理
    driver.close()
    
# ##########################

captweb()
# ##########################
# csvデータ読込　銘柄コード
def read_csv():
    a = 0
    with open('./stocklst.csv','r') as f:
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
    # updated_data = existing_data.append(new_data, ignore_index=True)
    updated_data = pd.concat([existing_data, new_data],axis=0, ignore_index=True)

    # 追記した結果をCSVファイルに書き込む
#     updated_data.to_csv(file_path, index=False, mode='w',
#                         header=not existing_data.empty)
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

    # print(soup)
    print(type(soup))
    print("---title---:",soup.title)
    # strGet = soup.find('content').text

    # 株価を抽出
    # stock_price = soup.find('span', class_='mkc-stock_prices').text
    # 文字’円’を’’に置換する
    stock_price = soup.find(
        'td', class_='ly_vamd_inner ly_colsize_9_fix fwb tar wsnw').text
    stock_name = soup.find(
        'div', class_='md_card_ti').text
    loc = stock_name.split("の")
# ly_vamd_inner ly_colsize_9_fix fwb tar wsnw
    return loc[0] + "  " + stock_price
# ##########################


meigaralst =  read_csv()

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

    # temp[1] = convert_to_numeric(temp[1])
    logging.debug('price')
    logging.debug(temp[1])

    pricelist.append(temp[1])
    # 改行コード除去
    chars_to_exclude = "\n"
    temp[0] = re.sub(chars_to_exclude, "", temp[0])

    namelist.append(temp[0])
    dtnows.append(datetime.datetime.now())

dtStoks = pd.DataFrame(
    {'datetime':dtnows,'meigaraCD': meigaralist, 'name':  namelist, 'price': pricelist})

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

# 株価を取得する銘柄コードを指定
stock_code = '8001'  # ここに対象の銘柄コードを入力

# 株価を取得
price = get_stock_price(stock_code)

# "[円]"除去
chars_to_exclude = "[円]"
price = re.sub(chars_to_exclude, "", price)

meigaralist=[]
pricelist = []
namelist = []

printrem()
meigaralist.append(stock_code)
temp = price.split("  ")
print("tt:",temp)
pricelist.append(temp[1])
# 改行コード除去
chars_to_exclude = "\n"
temp[0] = re.sub(chars_to_exclude, "", temp[0])


namelist.append(temp[0])

print(meigaralist[0])
print(pricelist[0])
dtStoks = pd.DataFrame({'meigaraCD': meigaralist, 'name':  namelist, 'price': pricelist})
print("print(dtStoks)")
print(dtStoks)

dtStoksnonull = dtStoks.dropna(how="any")
print("print(dtStoksnonull)")
print(dtStoksnonull)

dtStoksnonull.to_csv('./dtStoksnonull.csv')
print(f'銘柄コード {stock_code} の株価: {price} 円')
printrem()

# series
setmp = [1,20,4]

print(setmp)

ttpd = pd.DataFrame({'cd': setmp})

print(ttpd)

# ##########################
# 下記は異常で不動

browser = webdriver.Chrome(executable_path = 'C:\WebDriver\bin')

browser.implicitly_wait(3)

url_login = "https://www.yahoo.co.jp/"
browser.get(url_login)
time.sleep(3)
print("yahoo")


print("-------End------")
