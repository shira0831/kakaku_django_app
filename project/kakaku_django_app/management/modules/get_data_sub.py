from selenium.webdriver.common.by import By
import copy


# ページ内のそれぞれの項目取得処理
    # 商品id取得
def get_data_product(chrome_driver):
    product_id = chrome_driver.get_text_css_selector('.ItemCom dl dd')
    item_id = {'item_id':product_id}
    return item_id


def get_item_name(self):
    item_name = self.get_text_css_selector('#titleBox')
    item_name = { 'title': item_name }
    return item_name


def get_release_date(self):
    release_date = self.get_text_css_selector('.releaseDate')
    release_date = { '発売日': release_date }
    return release_date


def get_maker_url(self):
    maker_url = self.get_href('#specInfo > li > a')
    maker_url = { 'メーカーurl': maker_url }
    return maker_url


def get_img(self, genre):
    img_dict = {}

    # 変数セット
    if genre == 'usedpc':
        target_xpath = '.usedprdPhoto img'
    elif genre == 'newpc':
        target_xpath = '#imgBox img'

    photo_area = self.get_blocks(target_xpath)

    if photo_area == '':
        img_dict['img1'] = ''
    else:
        for i in range(1,len(photo_area)+1):
            img_dict[f'img{i}'] = photo_area[i-1].get_attribute('src')     
        
    return img_dict

# スペック欄取得
def get_spec_usedpc(chrome_driver):
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

def get_spec_newpc(chrome_driver):
    spec_dict = {}

    blocks = chrome_driver.get_blocks('#specContents #mainLeft tbody tr')

    for block in blocks:
        elements_ths = block.find_elements(By.XPATH, './th')
        elements_tds = block.find_elements(By.XPATH, './td')

        if len(elements_tds) != 0:
            for th, td in zip(elements_ths, elements_tds):
                text = th.text.replace(' ','').replace('（空き）','空き').replace('2in1タイプ','in1タイプ').replace('-','')
                if text != '':
                    spec_dict[text] = td.text
    return spec_dict


def get_spec_sp(chrome_driver, dict):

    tableElems = chrome_driver.get_blocks('.p-hikakuTbl')
        
    target_dom_num = search_dom(tableElems)
    thead_trs = tableElems[target_dom_num].find_elements(by=By.CSS_SELECTOR,value=("thead > tr"))


    tds = thead_trs[0].find_elements(by=By.XPATH,value=('./td'))
    
    result =[]
    for i, td in enumerate(tds):
        item_name = td.get_attribute('textContent').strip()
        tag_name = thead_trs[0].find_elements(by=By.XPATH,value=('./th'))
        dict[tag_name[0].text] = item_name            


        tbody_trs = tableElems[target_dom_num].find_elements(by=By.CSS_SELECTOR,value=("tbody > tr"))

        for tbody_tr in tbody_trs:
            j = i + 1
            tds = tbody_tr.find_element(by=By.XPATH,value=(f'./td[{j}]'))
            tbody_tr_td_name = tds.get_attribute('textContent').strip()

            tag2 = tbody_tr.find_element(by=By.XPATH, value=("./th[@class='p-hikakuTbl-name']"))
            tag_name2 = tag2.text.replace('?', '').strip()
            tag_name2 = tag_name2.replace('/', '').replace('・', '').replace('(', '').replace(')', '').replace('4', '').replace('5', '')

            if tag_name2 != '':
                dict[tag_name2] = tbody_tr_td_name

        # 通常のappendだと値の上書きが発生したためdeepコピー
        # https://qiita.com/kokorinosoba/items/e9ab9398af5b44d2ac9a
        result.append(copy.deepcopy(dict))

    return result


def search_dom(tableElems):
    target = 0

    for i, tableElem in enumerate(tableElems):
        if len(tableElem.find_elements(by=By.TAG_NAME,value=("tbody"))) > 0:
            target = i
            print('該当あり')
            # break
            return target
        # 存在する時の処理
        else:
            print('該当なし')
        # 存在しない時の処理