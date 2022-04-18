from django.db import models

# Create your models here.
class UsedPC(models.Model):

    class Meta:
        verbose_name = '中古PC'
        verbose_name_plural = '中古PC'

    #商品番号
    item_id = models.CharField(max_length=255)

    #商品URL
    item_url = models.URLField()

    #スクレイピング実行日
    created_at = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.item_id