import subprocess
import threading

from django.views.generic import View
from django.shortcuts import render


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        print('スクレイピングボタンが押されました')

        def research():
            """インナー関数としてリサーチスクリプト起動のコマンドを定義"""
            # <アプリ名>/management/commands/<スクリプト名>.py　を作成すると、
            # python manage.py <スクリプト名>でそのスクリプトを実行できます！ (https://docs.djangoproject.com/en/4.0/howto/custom-management-commands/)
            subprocess.run(["python", "manage.py", "kakakucom"], check=True)

        # リサーチスクリプトはバックで起動するためスレッドとして実行
        th = threading.Thread(target=research)
        th.start()

        # レスポンスを返す 例：「スタートしました」「失敗しました」等の表示
        response = None
        return response
