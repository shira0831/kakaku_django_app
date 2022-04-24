
import math
from selenium.webdriver.common.by import By
from tenacity import retry, wait_fixed
from .chrome_driver import ChromeDriver
from selenium.common.exceptions import InvalidSessionIdException
import time





# 最大件数を1ページ内のアイテム数30で割ってページ数を計算
# 1,000以上の「,」が邪魔でintに変換できないためreplaceする
def get_page_counts(chrome_driver, url, genre):
    chrome_driver.wait_displayed_page()
    chrome_driver.open_url(url)

    # 変数セット
    if genre == 'used_pc':
        target_xpath = '//*[@id="main"]/div[1]/div/div/div/div/div/div/div/table/tbody/tr/td[1]/p/span[1]'
        num = 30
    elif genre == 'new_pc':
        target_xpath = '//*[@id="itemList"]/form/div[1]/table/tbody/tr/td[1]/p[1]/span'
        num = 40
    elif genre == 'sp':
        page_counts = int(chrome_driver.get_text_css_selector('.p-pager_item.p-pager_item-num.p-pager_item-disabled'))
        max_item_counts = chrome_driver.get_text_css_selector('.p-searchSum_hitnum_txt')
        print(f'{page_counts}ページ・{max_item_counts}の商品があります')
        return page_counts


    # 商品数を取得
    max_item_counts = chrome_driver.get_text_xpath(target_xpath)

    # ページ数を取得
    max_item_counts = int(max_item_counts.replace(',',''))
    page_counts = math.ceil(max_item_counts / num)
    print(f'{page_counts}ページ・{max_item_counts}の商品があります')
    
    return page_counts


def get_item_urls(chrome_driver, url, genre, i):
    # pageを表示
    print(f'{url}?pdf_pg={i}を開きます')
    chrome_driver.wait_displayed_page()
    chrome_driver.open_url(f'{url}?pdf_pg={i}')

    # page内の商品リンク先を取得
    # リンク先から戻ってくるとページが変わっているため最初にurlをリスト格納する
    #  https://buralog.jp/python-selenium-stale-element-reference-element-is-not-attached-to-the-page-document-error/
    print('ページ内にある商品のリンク先を取得します')

    # 変数セット
    if genre == 'used_pc':
        target_xpath = '.itemName > p > a'
    elif genre == 'new_pc':
        target_xpath = '.ckitemLink > a'
    elif genre == 'sp':
        target_xpath = '.p-list_name > a'

    urls = chrome_driver.get_href_css_selector(target_xpath)
    # links = [i.get_attribute('href') for i in urls]
    links = [i.get_attribute('href') for i in urls]

    return links

# ページ内の詳細を取得しdictへ格納。それぞれの項目取得処理は下に記載

try_flg = 0

@retry
def get_data(chrome_driver, genre, link):
    try:
        global try_flg
        if try_flg > 0:
            print('retry!!')
            chrome_driver = ChromeDriver()
            time.sleep(20)
            try_flg = 0

        if genre == 'new_pc':
            link = f'{link}spec/#tab'
        elif genre == 'sp':
            link = f'{link}spec/'

        print(f'{link}の情報を取得します')
        # 格納した商品urlのページを一つずつ表示する
        chrome_driver.wait_displayed_page()
        chrome_driver.open_url(link)

        # 中古PCのデータ取得
        if genre == 'used_pc':

            item_id = get_data_product(chrome_driver) # 商品番号取得
            item_url = {'item_url':link} # 商品url
            pc_img = get_data_img(chrome_driver, genre) # 画像取得
            spec_dict = get_data_spec(chrome_driver) # スペック取得

            result = {}
            result = item_id | item_url | spec_dict | pc_img
            print(result)
            return result

        # 新品PCのデータ取得
        elif genre == 'new_pc':

            item_id = get_data_item_name(chrome_driver) # 商品の名前を取得
            release_date = get_release_date(chrome_driver) # 商品の名前を取得
            item_url = { '商品url': link } # 商品url　
            maker_url = get_maker_url(chrome_driver) # メーカー製品情報url取得
            pc_img = get_data_img(chrome_driver, genre) # 画像取得
            spec_dict = get_data_spec2(chrome_driver) # スペック取得

            result = {}
            result =  item_id | release_date | item_url | maker_url | pc_img | spec_dict
            print(result)
            return result

        elif genre == 'sp':
            result = {
            'maker' : chrome_driver.get_text_xpath('//*[@id="keitai"]/div[2]/div[1]/div/div[1]/div[2]/p/a[1]'),
            'product': chrome_driver.get_text_xpath('//*[@id="keitai"]/div[2]/div[1]/div/div[1]/div[2]/p/a[2]'),
            'release_date': chrome_driver.get_text_xpath('//*[@id="keitai"]/div[2]/div[1]/div/div[2]/div[2]/ul/li[1]'),
            }

            print(result)
            return result

    except InvalidSessionIdException as e:
        print('セッション死亡！！:InvalidSessionIdException',e)
        time.sleep(10)
        try_flg += 1
        print('try_flg',try_flg)
        
    except Exception as e:
        print('エラー:Exception',e)
        chrome_driver.close_driver()
        try_flg += 1
        print('try_flg',try_flg)


# ページ内のそれぞれの項目取得処理
    # 商品id取得
def get_data_product(chrome_driver):
    product_id = chrome_driver.get_text_css_selector('.ItemCom dl dd')
    item_id = {'item_id':product_id}
    return item_id


def get_data_item_name(chrome_driver):
    item_name = chrome_driver.get_text_css_selector('#titleBox')
    item_name = { 'title': item_name }
    return item_name


def get_release_date(chrome_driver):
    release_date = chrome_driver.get_text_css_selector('.releaseDate')
    release_date = { '発売日': release_date }
    return release_date


def get_maker_url(chrome_driver):
    maker_url = chrome_driver.get_href('#specInfo > li > a')
    maker_url = { 'メーカーurl': maker_url }
    return maker_url


def get_data_img(chrome_driver, genre):
    img_dict = {}

    # 変数セット
    if genre == 'used_pc':
        target_xpath = '.usedprdPhoto img'
    elif genre == 'new_pc':
        target_xpath = '#imgBox img'

    photo_area = chrome_driver.get_blocks(target_xpath)

    if photo_area == '':
        img_dict['img1'] = ''
    else:
        for i in range(1,len(photo_area)+1):
            img_dict[f'img{i}'] = photo_area[i-1].get_attribute('src')

    return img_dict

# ページ内のそれぞれの項目取得処理
    # スペック欄取得
def get_data_spec(chrome_driver):
    spec_dict = {}

    blocks = chrome_driver.get_blocks('.usedspecinfo > tbody > tr')

    
    for block in blocks:
        elements_th = block.find_elements(By.XPATH, './th')
        elements_td = block.find_elements(By.XPATH, './td')

        if len(elements_th) != 0 and len(elements_td) >= 2:
            temporary_box = ''
            for i, ele in enumerate(elements_td):
                # リスト内の奇数はkey
                if (i + 1) % 2 != 0: 
                    spec_dict[ele.text] = ''
                    temporary_box = ele.text
                # リスト内の偶数はvalue
                else:
                    spec_dict[temporary_box] = ele.text

        elif len(elements_th) != 0 and len(elements_td) == 1:
            spec_dict[elements_th[0].text] = elements_td[0].text
            
    return spec_dict

def get_data_spec2(chrome_driver):
    spec_dict = {}

    blocks = chrome_driver.get_blocks('#specContents #mainLeft tbody tr')

    for block in blocks:
        elements_ths = block.find_elements(By.XPATH, './th')
        elements_tds = block.find_elements(By.XPATH, './td')

        if len(elements_tds) != 0:
            for th, td in zip(elements_ths, elements_tds):
                spec_dict[th.text] = td.text

    return spec_dict


      

