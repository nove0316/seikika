#必要なライブラリをインポート
import sys
import os
import csv
import itertools
import pprint

#読み込むファイルのパスを受け取る
file_path = sys.argv[1]

#ファイルパスを絶対パスに変換
#file_path = os.file_path.abspath(file_path)

print(file_path)