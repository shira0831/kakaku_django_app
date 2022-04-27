from .chrome_driver import ChromeDriver
from selenium.common.exceptions import InvalidSessionIdException
from tenacity import retry, wait_fixed

from .get_data_sub import *
import math
import time


retry_flg = 0


class GetData(ChromeDriver):
    
    # コンストラクタの定義
    def __init__(self):
        print('ChromeDriverを起動します。')
        super(GetData, self).__init__()

    # __call__メソッドの定義
    def __call__(self):
        print('callメソッド!!!')

    def __del__(self):
        print('class GetDataの終了（デストラクタの呼び出し）')

    def get_data_exception(func):
        def wrapper(self,*args, **kwargs):

            global retry_flg

            try:
                return func(self,*args, **kwargs)

            except InvalidSessionIdException as e:
                print('セッション死亡！！:InvalidSessionIdException',e)
                time.sleep(5)
                retry_flg += 1
                print('retry_flg',retry_flg)
            
            except Exception as e:
                print('エラー:Exception',e)
                time.sleep(5)
                retry_flg += 1
                print('retry_flg',retry_flg)

        return wrapper


    @retry
    @get_data_exception
    def get_sp(self, link):

        global retry_flg
        if retry_flg > 0:
            print('リトライ')
            time.sleep(5)
            self = GetData()
            time.sleep(10)
            retry_flg = 0

        link = f'{link}spec/'

        print(f'{link}の情報を取得します')
        # 格納した商品urlのページを一つずつ表示する
        self.wait_displayed_page()
        self.open_url(link)

        # spのデータ取得
        dict = {
            'maker' : self.get_text_xpath('//*[@id="keitai"]/div[2]/div[1]/div/div[1]/div[2]/p/a[1]'),
            'product': self.get_text_xpath('//*[@id="keitai"]/div[2]/div[1]/div/div[1]/div[2]/p/a[2]'),
            'release_date': self.get_text_xpath('//*[@id="keitai"]/div[2]/div[1]/div/div[2]/div[2]/ul/li[1]'),
        }
        result = get_spec_sp(self, dict) # スペック取得

        print(result)
        return result


    @retry
    @get_data_exception
    def get_newpc(self, link):

        global retry_flg
        if retry_flg > 0:
            print('リトライ')
            time.sleep(5)
            self = GetData()
            time.sleep(10)
            retry_flg = 0
        
        link = f'{link}spec/#tab'
        print(f'{link}の情報を取得します')

        # 格納した商品urlのページを一つずつ表示する
        self.wait_displayed_page()
        self.open_url(link)

        # 新品PCのデータ取得
        item_id = get_item_name(self) # 商品の名前を取得
        release_date = get_release_date(self) # 商品の名前を取得
        item_url = { '商品url': link } # 商品url　
        maker_url = get_maker_url(self) # メーカー製品情報url取得
        pc_img = get_img(self,'newpc') # 画像取得
        spec_dict = get_spec_newpc(self) # スペック取得

        result = {}
        result =  item_id | release_date | item_url | maker_url | pc_img | spec_dict

        print(result)
        return result

    @retry 
    @get_data_exception
    def get_usedpc(self, link):

        global retry_flg
        if retry_flg > 0:
            print('リトライ')
            time.sleep(5)
            self = GetData()
            time.sleep(10)
            retry_flg = 0
            

        print(f'{link}の情報を取得します')
        # 格納した商品urlのページを一つずつ表示する
        self.wait_displayed_page()
        self.open_url(link)

        # 中古PCのデータ取得
        item_id = get_data_product(self) # 商品番号取得
        item_url = {'item_url':link} # 商品url
        pc_img = get_img(self, 'usedpc') # 画像取得
        spec_dict = get_spec_usedpc(self) # スペック取得

        result = {}
        result = item_id | item_url | spec_dict | pc_img

        print(result)

        return result


    # 最大件数を1ページ内のアイテム数30で割ってページ数を計算
    # 1,000以上の「,」が邪魔でintに変換できないためreplaceする
    def page_counts(self, url, genre):

        self.wait_displayed_page()
        self.open_url(url)

        # 変数セット
        if genre == 'usedpc':
            target_xpath = '//*[@id="main"]/div[1]/div/div/div/div/div/div/div/table/tbody/tr/td[1]/p/span[1]'
            num = 30
        elif genre == 'newpc':
            target_xpath = '//*[@id="itemList"]/form/div[1]/table/tbody/tr/td[1]/p[1]/span'
            num = 40
        elif genre == 'sp':
            page_counts = int(self.get_text_css_selector('.p-pager_item.p-pager_item-num.p-pager_item-disabled'))
            max_item_counts = self.get_text_css_selector('.p-searchSum_hitnum_txt')
            print(f'{page_counts}ページ・{max_item_counts}の商品があります')
            return page_counts


        # 商品数を取得
        max_item_counts = self.get_text_xpath(target_xpath)

        # ページ数を取得
        max_item_counts = int(max_item_counts.replace(',',''))
        page_counts = math.ceil(max_item_counts / num)
        print(f'{page_counts}ページ・{max_item_counts}の商品があります')
        
        return page_counts


    def item_urls(self, url, genre, i):

        # page内の商品リンク先を取得
        # リンク先から戻ってくるとページが変わっているため最初にurlをリスト格納する
        #  https://buralog.jp/python-selenium-stale-element-reference-element-is-not-attached-to-the-page-document-error/
        print('ページ内にある商品のリンク先を取得します')

        # 変数セット
        if genre == 'usedpc':
            target_xpath = '.itemName > p > a'
            print(f'{url}/Page={i}を開きます')
            self.wait_displayed_page()
            self.open_url(f'{url}Page={i}')

        elif genre == 'newpc':
            target_xpath = '.ckitemLink > a'
            self.wait_displayed_page()
            print(f'{url}?pdf_pg={i}を開きます')
            self.open_url(f'{url}?pdf_pg={i}')

        elif genre == 'sp':
            target_xpath = '.p-list_name > a'

        urls = self.get_href_css_selector(target_xpath)
        links = [i.get_attribute('href') for i in urls]

        return links