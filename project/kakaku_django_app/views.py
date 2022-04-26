import subprocess
import threading

from django.views.generic import View
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages

from sqlalchemy import create_engine
import pandas as pd




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

    engine = create_engine('sqlite:///db.sqlite3', echo=True)
    df = pd.read_sql_table('kakaku_django_app_usedpc', engine)
    
    response = HttpResponse(content_type='text/csv; charset=utf8')
    response['Content-Disposition'] = 'attachment; filename=users.csv'
    df.to_csv(path_or_buf=response, encoding='utf_8_sig', index=False)

    return response