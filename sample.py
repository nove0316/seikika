#必要なライブラリをインポート
import sys
import csv
import itertools

#読み込むファイルのパスを受け取る
if len(sys.argv) == 3 and (sys.argv[2] == '1' or sys.argv[2] == '2'):
    file_path = sys.argv[1]
    kadai = sys.argv[2]
else:
    sys.exit("ファイル名と番号を入力してください\n例 1. 第一正規化の場合\n  sample.py sample.tsv 1")

#tsvファイルを読み込む
with open(file_path, mode='r', encoding='ascii') as f:
    #tsvファイルß
    tsv_reader = csv.reader(f, delimiter='\t')
    #2次元配列として1行ずつ格納する
    rows_arr = [row for row in tsv_reader]



#1. 第一正規化
#コマンドライン引数に'1'が入力された時、第一正規化したtsvファイルを出力
if kadai == '1':

    #出力するファイル名はnormalized'+元のファイル名
    with open('normalized_' + file_path, mode='w', encoding='ascii') as fo:
        tsv_writer = csv.writer(fo, delimiter='\t')

        #列の数だけ以下を繰り返す
        for i in range(len(rows_arr)):
            #1行ずつ処理するための配列rowを初期化
            row = []
            #半角コロンで要素を分ける
            for j in range(len(rows_arr[0])):
                row.append(rows_arr[i][j].split(':'))

            #配列rowの直積を出力することで正規化
            l_p = list(itertools.product(*row))
            #配列をtsv形式で書き込み
            tsv_writer.writerows(l_p)



#2. 第一正規化の逆変換
#コマンドライン引数に'2'が入力された時、第一正規化の逆変換をしたtsvファイルを出力
if kadai == '2':

    #出力するファイル名はreversed'+元のファイル名
    with open('reversed_' + file_path, mode='w', encoding='ascii') as fo:
        tsv_writer = csv.writer(fo, delimiter='\t')

        #辞書dict1を作成
        dict1 = {}
        #列の数だけ以下を繰り返す
        for k in range(len(rows_arr)):
            #すでにキーが存在している時、半角コロンとvalueを追加する
            if rows_arr[k][0] in dict1.keys():
                dict1[rows_arr[k][0]] += ':' + rows_arr[k][1]
            #キーが存在しない時、キーとvalueを追加
            else:
                dict1[rows_arr[k][0]] = rows_arr[k][1]
        #辞書dict1を配列に変換し、tsv形式で書き込み
        tsv_writer.writerows(list(dict1.items()))
