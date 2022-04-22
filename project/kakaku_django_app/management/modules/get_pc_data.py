
import math
from selenium.webdriver.common.by import By
from tenacity import retry, wait_fixed,retry_if_exception_type,TryAgain
from selenium.common.exceptions import InvalidSessionIdException
from selenium.common.exceptions import WebDriverException


# 最大件数を1ページ内のアイテム数30で割ってページ数を計算
# 1,000以上の「,」が邪魔でintに変換できないためreplaceする
def get_page_counts(chrome_driver, genre_url):
    chrome_driver.wait_displayed_page()
    chrome_driver.open_url(genre_url)

    # 商品数を取得
    # target_xpath = '//*[@id="itemList"]/form/div[1]/table/tbody/tr/td[1]/p[1]/span'
    target_xpath = '//*[@id="main"]/div[1]/div/div/div/div/div/div/div/table/tbody/tr/td[1]/p/span[1]'
    max_item_counts = chrome_driver.get_text_xpath(target_xpath)

    # ページ数を取得
    max_item_counts = int(max_item_counts.replace(',',''))
    page_counts = math.ceil(max_item_counts / 30)

    # page_num = math.ceil(max_item_num / 40)
    print(f'{page_counts}ページ・{max_item_counts}の商品があります')
    
    return page_counts


def get_item_urls(chrome_driver,genre_url,i):
    # pageを表示
    print(f'{genre_url}?pdf_pg={i}を開きます')
    chrome_driver.wait_displayed_page()
    chrome_driver.open_url(f'{genre_url}?pdf_pg={i}')

    # page内の商品リンク先を取得
    # リンク先から戻ってくるとページが変わっているため最初にurlをリスト格納する
    #  https://buralog.jp/python-selenium-stale-element-reference-element-is-not-attached-to-the-page-document-error/
    print('ページ内にある商品のリンク先を取得します')
    target_xpath = '.itemName > p > a'
    urls = chrome_driver.get_href_css_selector(target_xpath)
    links = [i.get_attribute('href') for i in urls]

    return links


# ページ内の詳細を取得しdictへ格納。それぞれの項目取得処理は下に記載
def get_data(chrome_driver,link):
    # 格納した商品urlのページを一つずつ表示する
    chrome_driver.wait_displayed_page()
    chrome_driver.open_url(link)

    # 商品番号取得
    item_id = get_data_product(chrome_driver)
    
    # 商品url
    item_url = {'item_url':link}

    # 画像取得
    pc_img = get_data_img(chrome_driver)

    # スペック取得
    spec_dict = get_data_spec(chrome_driver)

    result = {}

    result = item_id | item_url | spec_dict | pc_img

    print(result)
    return result


# ページ内のそれぞれの項目取得処理
    # 商品id取得
def get_data_product(chrome_driver):
    
    product_id = chrome_driver.get_text_css_selector('.ItemCom dl dd')

    item_id = {'item_id':product_id}

    return item_id


# ページ内のそれぞれの項目取得処理
    # 商品画像取得
    # imgがないページは空白で返す
def get_data_img(chrome_driver):
    img_dict = {}

    photo_area = chrome_driver.get_blocks('.usedprdPhoto > ul >li')

    if photo_area == '':
        img_dict['img1'] = ''
    else:
        for i in range(1,len(photo_area)+1):
            img_url = chrome_driver.get_src(f'//*[@id="usedprdData"]/table[1]/tbody/tr[2]/td/div/ul/li[{i}]/img')
            img_dict[f'img{i}'] = img_url

            # img_dict[f'img{i}'] = photo_area[i-1].get_attribute('src')

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

