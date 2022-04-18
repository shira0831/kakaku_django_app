from django.core.management.base import BaseCommand

from kakaku_django_app.management.commands.modules.chrome_driver import ChromeDriver
from kakaku_django_app.management.commands.modules import get_pc_data
from kakaku_django_app.models import UsedPC


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # driverを生成
        chrome_driver = ChromeDriver()

        genre_urls = [
            'https://kakaku.com/used/pc/ca=0030/',
            # 'https://kakaku.com/used/pc/ca=0080/',
            # 'https://kakaku.com/used/pc/ca=0019/',
            # 'https://kakaku.com/used/pc/ca=0010/',
            # 'https://kakaku.com/used/pc/ca=0020/',
            # 'https://kakaku.com/used/pc/ca=0030/',
        ]

        for genre_url in genre_urls:

            # ページ数を取得する
            target_xpath = '//*[@id="main"]/div[1]/div/div/div/div/div/div/div/table/tbody/tr/td[1]/p/span[1]'
            page_num = get_pc_data.get_page_number(
                chrome_driver, genre_url, target_xpath)
            print(f'{page_num}ページあります')

            for i in range(1, page_num + 1):
                # ページを表示する
                chrome_driver.wait_displayed_page()
                chrome_driver.open_url(f'{genre_url}Page={i}/')

                # ページ内の商品urlを格納
                target_xpath = '.itemName > p > a'
                links = get_pc_data.get_item_url(chrome_driver, target_xpath)

                for link in links:
                    # 格納した商品urlのページを一つずつ表示する
                    chrome_driver.wait_displayed_page()
                    chrome_driver.open_url(link)

                    # 商品番号取得
                    item_id = get_pc_data.get_pc_product(chrome_driver)

                    # 商品url
                    item_url = link

                    # # 画像取得
                    # target_xpath = '.usedprdPhoto > ul >li'
                    # pc_img = get_pc_data.get_pc_img(chrome_driver, target_xpath)

                    # # スペック取得
                    # spec_dict = get_pc_data.get_pc_spec(chrome_driver)

                    print(item_id, item_url)

                    data = UsedPC(
                        item_id=item_id,
                        item_url=item_url
                    )

                    data.save()

        # driverを削除する
        chrome_driver.close_driver()
