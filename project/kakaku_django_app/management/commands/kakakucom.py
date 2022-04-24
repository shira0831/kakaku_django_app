from django.core.management.base import BaseCommand

from ..modules.chrome_driver import ChromeDriver
from ..modules import get_pc_data

from sqlalchemy import create_engine
import pandas as pd


class Command(BaseCommand):
    def add_arguments(self, parser): #コマンド引数の定義
        # int型の必須引数の定義
        # tp = lambda x:list(map(str, x.split(',')))
        parser.add_argument('id', type=str, nargs='*')
        args = parser.parse_args()
        print('っっっっっっっd',args)
        print('test',args.id[1])
        output= eval(args.id[1])
        print('output',output)  


    def handle(self, *args,**kwargs):
        self.stdout.write(self.style.SUCCESS('id = "%s"' % kwargs['id']))
        print('argsargsargsargsargsargs',args)
        print('kwargskwargskwargskwargs',kwargs)
        print('kwargskwargskwargskwargskwargskwargskwargskwargs',kwargs['id'])
        print('eval',eval(kwargs['id'][0]))

        # driverを生成
        chrome_driver = ChromeDriver()
        # genre_urls = [
        #     'https://kakaku.com/used/pc/ca=0030/',# 中古タブレットPC
        #     'https://kakaku.com/used/pc/ca=0080/',# 中古モニタ・ディスプレイ 
        #     'https://kakaku.com/used/pc/ca=0019/',# 中古Mac デスクトップパソコン
        #     'https://kakaku.com/used/pc/ca=0010/',# 中古デスクトップパソコン
        #     'https://kakaku.com/used/pc/ca=0020/',# 中古ノートパソコン
        # ]

        # genre_urls = [
        # 'https://kakaku.com/pc/note-pc/itemlist.aspx', # すべて ノートパソコン
        # 'https://kakaku.com/pc/desktop-pc/itemlist.aspx',# すべて デスクトップパソコン
        # 'https://kakaku.com/pc/mac-note-pc/itemlist.aspx',# すべて Mac ノート(MacBook)
        # 'https://kakaku.com/pc/mac-desktop-pc/itemlist.aspx',# すべて Mac デスクトップ
        # 'https://kakaku.com/pc/pda/itemlist.aspx'# すべて タブレットPC
        # ]

        # test_urls = [
        # 'https://kakaku.com/used/pc/ca=0030/',
        # 'https://kakaku.com/used/pc/ca=0080/',
        # 'https://kakaku.com/used/pc/ca=0019/',
        # 'https://kakaku.com/used/pc/ca=0010/',
        # 'https://kakaku.com/used/pc/ca=0020/',
        # 'https://kakaku.com/pc/note-pc/itemlist.aspx', # すべて ノートパソコン
        # 'https://kakaku.com/pc/desktop-pc/itemlist.aspx',# すべて デスクトップパソコン
        # 'https://kakaku.com/pc/mac-note-pc/itemlist.aspx',# すべて Mac ノート(MacBook)
        # 'https://kakaku.com/pc/mac-desktop-pc/itemlist.aspx',# すべて Mac デスクトップ
        # 'https://kakaku.com/pc/pda/itemlist.aspx'# すべて タブレットPC
        # ]

        data= []
        genre_urls = eval(kwargs['id'][0])

        for genre_url in genre_urls:
            print('target_url',genre_url)
    
            # 変数セット
            url = genre_url['url']
            genre = genre_url['genre']

            # ページ数を取得する
            page_counts = get_pc_data.get_page_counts(chrome_driver, url, genre)

            for i in range(1, page_counts + 1):
            # for i in range(1, 2):
                # ページを表示して各ページ内の商品urlを格納
                links = get_pc_data.get_item_urls(chrome_driver, url, genre, i)
                # 各商品url内の情報を取得
                for link in links:
                    result = get_pc_data.get_data(chrome_driver, genre, link)
                    data.append(result)

        # driverを削除する
        chrome_driver.close_driver()

        # DBへデータ登録
        engine = create_engine('sqlite:///db.sqlite3', echo=True)
        df = pd.DataFrame(data)
        df.to_sql('kakaku_django_app_usedpc',con=engine, if_exists='append', index=False)