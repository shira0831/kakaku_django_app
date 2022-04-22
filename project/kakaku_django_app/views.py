import subprocess
import threading

from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        check1 = request.POST.getlist("used_pc")
        check2 = request.POST.getlist("newPC")
        print('こここここ',check1,type(check1))
        print('こここここ',check2)


        print('スクレイピングボタンが押されました')

        def research():
            """インナー関数としてリサーチスクリプト起動のコマンドを定義"""
            # <アプリ名>/management/commands/<スクリプト名>.py　を作成すると、
            # python manage.py <スクリプト名>でそのスクリプトを実行できます！ (https://docs.djangoproject.com/en/4.0/howto/custom-management-commands/)
            subprocess.run(["python", "manage.py", "kakakucom",','.join(check1)], check=True)
        
        # リサーチスクリプトはバックで起動するためスレッドとして実行
        th = threading.Thread(target=research)
        th.start()

        # レスポンスを返す 例：「スタートしました」「失敗しました」等の表示
        response = HttpResponse('<h1>成功</h1>')
        return response
