from django.db import models

class UsedPC(models.Model):

    class Meta:
        verbose_name = '中古PC'
        verbose_name_plural = '中古PC'

    #商品番号
    item_id = models.CharField(max_length=255,blank=True,null=True,default='')
    #商品URL
    item_url = models.URLField()
    #メーカー
    メーカー = models.CharField(max_length=255,blank=True,null=True,default='')
    #画面サイズ
    画面サイズ = models.CharField(max_length=255,blank=True,null=True,default='')
    #記憶容量
    記憶容量 = models.CharField(max_length=255,blank=True,null=True,default='')
    #スペック詳細
    スペック詳細 = models.TextField(blank=True,null=True,default='')
    #商品画像
    img1 = models.URLField(blank=True,null=True,default='')
    img2 = models.URLField(blank=True,null=True,default='')
    img3 = models.URLField(blank=True,null=True,default='')
    img4 = models.URLField(blank=True,null=True,default='')
    img5 = models.URLField(blank=True,null=True,default='')
    img6 = models.URLField(blank=True,null=True,default='')

    モニタタイプ = models.TextField(blank=True,null=True,default='')
    モニタサイズ = models.CharField(max_length=255,blank=True,null=True,default='')
    OS = models.CharField(max_length=255,blank=True,null=True,default='')
    CPU = models.CharField(max_length=255,blank=True,null=True,default='')

    def __str__(self):
        return self.item_id



class NewPC(models.Model):
    
    class Meta:
        verbose_name = '新品PC'
        verbose_name_plural = '新品PC'

    #商品番号
    title = models.CharField(max_length=255,blank=True,null=True,default='')
    発売日  = models.CharField(max_length=255,blank=True,null=True,default='')
    メーカーurl = models.URLField(blank=True,null=True,default='')
    #商品URL 
    商品url = models.URLField(blank=True,null=True,default='')
    #商品画像
    img1 = models.URLField(blank=True,null=True,default='')
    img2 = models.URLField(blank=True,null=True,default='')
    img3 = models.URLField(blank=True,null=True,default='')
    img4 = models.URLField(blank=True,null=True,default='')
    img5 = models.URLField(blank=True,null=True,default='')
    img6 = models.URLField(blank=True,null=True,default='')


    タッチペン付属 = models.CharField(max_length=255,blank=True,null=True,default='')
    防塵機能 = models.CharField(max_length=255,blank=True,null=True,default='')
    防水機能 = models.CharField(max_length=255,blank=True,null=True,default='')
    コア数  = models.CharField(max_length=255,blank=True,null=True,default='')
    メモリ  = models.CharField(max_length=255,blank=True,null=True,default='')
    ネットワーク接続タイプ  = models.CharField(max_length=255,blank=True,null=True,default='')
    OS種類 = models.CharField(max_length=255,blank=True,null=True,default='')
    CPU = models.CharField(max_length=255,blank=True,null=True,default='')
    CPUスコア = models.CharField(max_length=255,blank=True,null=True,default='')
    画面サイズ = models.CharField(max_length=255,blank=True,null=True,default='')
    画面種類 = models.CharField(max_length=255,blank=True,null=True,default='')
    解像度 = models.CharField(max_length=255,blank=True,null=True,default='')
    タッチパネル = models.CharField(max_length=255,blank=True,null=True,default='')
    in1タイプ = models.CharField(max_length=255,blank=True,null=True,default='')
    ワイド画面 = models.CharField(max_length=255,blank=True,null=True,default='')
    表面処理 = models.CharField(max_length=255,blank=True,null=True,default='')
    メモリ容量 = models.CharField(max_length=255,blank=True,null=True,default='')
    メモリ規格 = models.CharField(max_length=255,blank=True,null=True,default='')
    メモリスロット空き = models.CharField(max_length=255,blank=True,null=True,default='')
    ストレージ容量 = models.CharField(max_length=255,blank=True,null=True,default='')
    HDD回転数 = models.CharField(max_length=255,blank=True,null=True,default='')
    OS = models.CharField(max_length=255,blank=True,null=True,default='')
    Office詳細 = models.CharField(max_length=255,blank=True,null=True,default='')
    ドライブ規格 = models.CharField(max_length=255,blank=True,null=True,default='')
    ビデオチップ = models.CharField(max_length=255,blank=True,null=True,default='')
    ビデオメモリ = models.CharField(max_length=255,blank=True,null=True,default='')
    駆動時間 = models.CharField(max_length=255,blank=True,null=True,default='')
    インターフェース = models.CharField(max_length=255,blank=True,null=True,default='')
    インテルEvoプラットフォーム = models.CharField(max_length=255,blank=True,null=True,default='')
    ゲーミングPC = models.CharField(max_length=255,blank=True,null=True,default='')
    USBPD = models.CharField(max_length=255,blank=True,null=True,default='')
    ファンレス = models.CharField(max_length=255,blank=True,null=True,default='')
    生体認証 = models.CharField(max_length=255,blank=True,null=True,default='')
    センサー = models.CharField(max_length=255,blank=True,null=True,default='')
    BTO対応 = models.CharField(max_length=255,blank=True,null=True,default='')
    その他 = models.CharField(max_length=255,blank=True,null=True,default='')
    無線LAN = models.CharField(max_length=255,blank=True,null=True,default='')
    WiFiDirect対応 = models.CharField(max_length=255,blank=True,null=True,default='')
    NFC = models.CharField(max_length=255,blank=True,null=True,default='')
    LAN = models.CharField(max_length=255,blank=True,null=True,default='')
    SIMフリー対応 = models.CharField(max_length=255,blank=True,null=True,default='')
    SIMカード = models.CharField(max_length=255,blank=True,null=True,default='')
    地上デジタルチューナー = models.CharField(max_length=255,blank=True,null=True,default='')
    重量 = models.CharField(max_length=255,blank=True,null=True,default='')
    幅x高さx奥行 = models.CharField(max_length=255,blank=True,null=True,default='')
    エコマーク = models.CharField(max_length=255,blank=True,null=True,default='')
    認定番号 = models.CharField(max_length=255,blank=True,null=True,default='')
    カラー = models.URLField(blank=True,null=True,default='')


    def __str__(self):
        return self.title


class Sp(models.Model):
    
    class Meta:
        verbose_name = 'sp'
        verbose_name_plural = 'sp'

    #商品番号
    maker = models.CharField(max_length=255,blank=True,null=True,default='')
    #商品URL
    product = models.URLField()
    #メーカー
    release_date = models.CharField(max_length=255,blank=True,null=True,default='')
    #画面サイズ
    製品名 = models.CharField(max_length=255,blank=True,null=True,default='')
    #記憶容量
    発売日 = models.CharField(max_length=255,blank=True,null=True,default='')
    #記憶容量
    OS種類 = models.CharField(max_length=255,blank=True,null=True,default='')
    #商品画像
    img1 = models.URLField(blank=True,null=True,default='')
    img2 = models.URLField(blank=True,null=True,default='')
    img3 = models.URLField(blank=True,null=True,default='')
    img4 = models.URLField(blank=True,null=True,default='')
    img5 = models.URLField(blank=True,null=True,default='')
    img6 = models.URLField(blank=True,null=True,default='')

    CPU = models.CharField(max_length=255,blank=True,null=True,default='')
    CPUコア数 = models.CharField(max_length=255,blank=True,null=True,default='')
    内蔵メモリROM = models.CharField(max_length=255,blank=True,null=True,default='')
    内蔵メモリRAM = models.CharField(max_length=255,blank=True,null=True,default='')
    充電器充電ケーブル = models.CharField(max_length=255,blank=True,null=True,default='')
    外部メモリタイプ = models.CharField(max_length=255,blank=True,null=True,default='')
    外部メモリ最大容量 = models.CharField(max_length=255,blank=True,null=True,default='')
    バッテリー容量 = models.CharField(max_length=255,blank=True,null=True,default='')
    画面サイズ = models.CharField(max_length=255,blank=True,null=True,default='')
    画面解像度 = models.CharField(max_length=255,blank=True,null=True,default='')
    パネル種類 = models.CharField(max_length=255,blank=True,null=True,default='')
    背面カメラ画素数 = models.CharField(max_length=255,blank=True,null=True,default='')
    前面カメラ画素数 = models.CharField(max_length=255,blank=True,null=True,default='')
    手ブレ補正 = models.CharField(max_length=255,blank=True,null=True,default='')
    K撮影対応 = models.CharField(max_length=255,blank=True,null=True,default='')
    スローモーション撮影 = models.CharField(max_length=255,blank=True,null=True,default='')
    撮影用フラッシュ = models.CharField(max_length=255,blank=True,null=True,default='')
    複数レンズ = models.CharField(max_length=255,blank=True,null=True,default='')
    幅 = models.CharField(max_length=255,blank=True,null=True,default='')
    高さ = models.CharField(max_length=255,blank=True,null=True,default='')
    厚み = models.CharField(max_length=255,blank=True,null=True,default='')
    重量 = models.CharField(max_length=255,blank=True,null=True,default='')
    カラー = models.CharField(max_length=255,blank=True,null=True,default='')
    おサイフケータイFeliCa = models.CharField(max_length=255,blank=True,null=True,default='')
    ワイヤレス充電Qi = models.CharField(max_length=255,blank=True,null=True,default='')
    急速充電 = models.CharField(max_length=255,blank=True,null=True,default='')
    認証機能 = models.CharField(max_length=255,blank=True,null=True,default='')
    耐水防水 = models.CharField(max_length=255,blank=True,null=True,default='')
    防塵 = models.CharField(max_length=255,blank=True,null=True,default='')
    MIL規格 = models.CharField(max_length=255,blank=True,null=True,default='')
    イヤホンジャック = models.CharField(max_length=255,blank=True,null=True,default='')
    HDMI端子 = models.CharField(max_length=255,blank=True,null=True,default='')
    MHL = models.CharField(max_length=255,blank=True,null=True,default='')
    フルセグ = models.CharField(max_length=255,blank=True,null=True,default='')
    ワンセグ = models.CharField(max_length=255,blank=True,null=True,default='')
    ハイレゾ = models.CharField(max_length=255,blank=True,null=True,default='')
    GPS = models.CharField(max_length=255,blank=True,null=True,default='')
    センサー = models.CharField(max_length=255,blank=True,null=True,default='')
    G = models.CharField(max_length=255,blank=True,null=True,default='')
    GLTE = models.CharField(max_length=255,blank=True,null=True,default='')
    無線LAN規格 = models.CharField(max_length=255,blank=True,null=True,default='')
    テザリング対応 = models.CharField(max_length=255,blank=True,null=True,default='')
    Bluetooth = models.CharField(max_length=255,blank=True,null=True,default='')
    NFC = models.CharField(max_length=255,blank=True,null=True,default='')
    赤外線通信機能 = models.CharField(max_length=255,blank=True,null=True,default='')
    デュアルSIM = models.CharField(max_length=255,blank=True,null=True,default='')
    デュアルSIMデュアルスタンバイDSDS = models.CharField(max_length=255,blank=True,null=True,default='')
    デュアルSIMデュアルVoLTEDSDV = models.CharField(max_length=255,blank=True,null=True,default='')
    SIM情報 = models.CharField(max_length=255,blank=True,null=True,default='')


    def __str__(self):
        return self.製品名