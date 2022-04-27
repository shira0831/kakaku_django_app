import subprocess
import threading

from django.views.generic import View
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages

from sqlalchemy import create_engine
import pandas as pd

from datetime import datetime as dt


import csv
from django.http import HttpResponse




class IndexView(View):

    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):

        target_name = ["usedpc","newpc","sp"]

        targets = []

        for i in target_name:
            data = request.POST.getlist(i)
            url = [{"url":j,'genre':i} for j in data]
            targets.extend(url)
        

        print(targets)
        print('スクレイピングボタンが押されました')

        if len(targets) == 0:
            # message framework
            # https://dot-blog.jp/news/django-messages-frame-work/
            print('ラジオボタンデータなし')
            messages.error(request, 'CheckBoxのどれかを選択してください!')
            return redirect('index')

        def research():
            """インナー関数としてリサーチスクリプト起動のコマンドを定義"""
            # <アプリ名>/management/commands/<スクリプト名>.py　を作成すると、
            # python manage.py <スクリプト名>でそのスクリプトを実行できます！ (https://docs.djangoproject.com/en/4.0/howto/custom-management-commands/)
            subprocess.run(["python", "manage.py", "kakakucom",str(targets)], check=True)

        # リサーチスクリプトはバックで起動するためスレッドとして実行
        th = threading.Thread(target=research)
        th.start()


        # レスポンスを返す 例：「スタートしました」「失敗しました」等の表示
        messages.info(request, 'スクレイピングを開始します')
        return redirect('index')



def csvexport(request):
    print('csvexportcsvexportcsvexportcsvexportcsvexport')

    data  = request.GET.get('from')
    data2 = request.GET.get('to')
    data3 = request.GET.get('csv_usedpc')
    data4 = request.GET.get('csv_newpc')
    data5 = request.GET.get('csv_sp')

    print('data',data,data2,data3,data4,data5)

    # engine = create_engine('sqlite:///db.sqlite3', echo=True)
    # df = pd.read_sql_table('kakaku_django_app_usedpc', engine)

    # df['X'] = pd.to_datetime(df['create_date'])
    # print('df2',df['X'])
    # df['Z'] = df['X'].dt.strftime('%Y-%m-%d')
    # print('df3',df['Z'])
 
    # df4 = df[df['Z'] == data]
    # print('df4',df4)

    # # # df = df[df['create_date'] == "2021-04-27"]
    # # # print(df)
    # df4.to_csv("pandas_test.csv", index=False, encoding="utf-8-sig")

    
    # response = HttpResponse(content_type='text/csv; charset=utf8')
    # response['Content-Disposition'] = 'attachment; filename=users.csv'
    # df.to_csv(path_or_buf=response, encoding='utf_8_sig', index=False)

    # return response
    # return render(request, 'index', params)
    messages.info(request, 'CSV抽出を開始します')
    return redirect('index')