from django.core.management.base import BaseCommand
from sqlalchemy import create_engine

from ..modules.get_data import GetData

import pandas as pd


class Command(BaseCommand):
    def add_arguments(self, parser): #コマンド引数の定義
        parser.add_argument('id', type=str, nargs='*')
        args = parser.parse_args()
        output= eval(args.id[1])
        print('output',output)  


    def handle(self, *args,**kwargs):
        self.stdout.write(self.style.SUCCESS('id = "%s"' % kwargs['id']))

        # GetDataクラスからdriverを生成
        get_data = GetData()
        
        data= []
        genre_urls = eval(kwargs['id'][0])

        for genre_url in genre_urls:
            print('target_url',genre_url)
    
            # 変数セット
            url = genre_url['url']
            genre = genre_url['genre']

            # ページ数を取得する
            page_counts = get_data.page_counts(url, genre)

            # for i in range(1, page_counts + 1):
            for i in range(1, 2):
                # ページを表示して各ページ内の商品urlを格納
                links = get_data.item_urls(url, genre, i)

                # 各商品url内の情報を取得
                # for link in links:
                for j in range(1,3):
                    result = getattr(get_data,f'get_{genre}')(links[j])

                    if genre == 'sp':
                        data.extend(result)
                    else:
                        data.append(result)

            # DBへデータ登録
            df = pd.DataFrame(data)
            engine = create_engine('sqlite:///db.sqlite3', echo=True)
            df.to_sql(f'kakaku_django_app_{genre}',con=engine, if_exists='append', index=False)

                    
        # driverを削除する
        get_data.close_driver()
        print('スクレイピング処理完了')

        