
import math
from selenium.webdriver.common.by import By
from tenacity import retry, wait_fixed,retry_if_exception_type,TryAgain
from selenium.common.exceptions import InvalidSessionIdException
from selenium.common.exceptions import WebDriverException


# 最大件数を１ページ内のアイテム数30で割ってページ数を計算
# 1,000以上の「,」が邪魔でintに変換できないためreplaceする
def get_page_number(chrome_driver, genre_url, target_xpath):
    chrome_driver.wait_displayed_page()
    chrome_driver.open_url(genre_url)

    max_item_num = chrome_driver.get_text_xpath(target_xpath)
    print(f'{max_item_num}')


    max_item_num = int(max_item_num.replace(',',''))
    # page_num = math.ceil(max_item_num / 30)

    page_num = math.ceil(max_item_num / 40)
    print(f'{page_num}ページあります')
    
    return page_num

@retry(wait=wait_fixed(4))
def get_item_url(chrome_driver,target_xpath):
    try:
        # page内の商品リンク先を取得
        # リンク先から戻ってくるとページが変わっているため最初にurlをリスト格納する
        #  https://buralog.jp/python-selenium-stale-element-reference-element-is-not-attached-to-the-page-document-error/
        print('ページ内にある商品のリンク先を取得します')
        chrome_driver.wait_displayed_page()
        # urls = chrome_driver.get_href_css_selector('.itemName > p > a')
        urls = chrome_driver.get_href_css_selector(target_xpath)

        links = [i.get_attribute('href') for i in urls]

        return links

    except WebDriverException as e:
        print('エラー:WebDriverException',e)
        print('リフレッシュ')
        chrome_driver.refresh()

    except Exception as e:
        print('エラー:Exception',e)


def get_pc_product(chrome_driver):
    
    product_id = chrome_driver.get_text_css_selector('.ItemCom dl dd')

    return product_id


# imgがないページは空白で返す
# def get_pc_img(chrome_driver, img_target_xpath):
#     img_dict = {}

#     # photo_area = chrome_driver.get_blocks('.usedprdPhoto > ul >li')
#     photo_area = chrome_driver.get_blocks(img_target_xpath)


#     if photo_area == '':
#         img_dict['img1'] = ''
#     else:
#         for i in range(1,len(photo_area)+1):
#             # img_url = chrome_driver.get_src(f'//*[@id="usedprdData"]/table[1]/tbody/tr[2]/td/div/ul/li[{i}]/img')
#             # img_dict[f'img{i}'] = img_url

#             img_dict[f'img{i}'] = photo_area[i-1].get_attribute('src')


#     return img_dict


# def get_pc_spec(chrome_driver):
#     spec_dict = {}

#     blocks = chrome_driver.get_blocks('.usedspecinfo > tbody > tr')

    
#     for block in blocks:
#         elements_th = block.find_elements(By.XPATH, './th')
#         elements_td = block.find_elements(By.XPATH, './td')

#         if len(elements_th) != 0 and len(elements_td) >= 2:
#             temporary_box = ''
#             for i, ele in enumerate(elements_td):
#                 # リスト内の奇数はkey
#                 if (i + 1) % 2 != 0: 
#                     spec_dict[ele.text] = ''
#                     temporary_box = ele.text
#                 # リスト内の偶数はvalue
#                 else:
#                     spec_dict[temporary_box] = ele.text

#         elif len(elements_th) != 0 and len(elements_td) == 1:
#             spec_dict[elements_th[0].text] = elements_td[0].text

#     return spec_dict

