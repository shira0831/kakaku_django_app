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

    モニタタイプ = models.TextField(blank=True,null=True,default='')
    モニタサイズ = models.CharField(max_length=255,blank=True,null=True,default='')
    OS = models.CharField(max_length=255,blank=True,null=True,default='')
    CPU = models.CharField(max_length=255,blank=True,null=True,default='')

    def __str__(self):
        return self.item_id