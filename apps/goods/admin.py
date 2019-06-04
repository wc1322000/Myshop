from django.contrib import admin
from goods.models import GoodsCategory, GoodsCategoryBrand, Goods, GoodsImage, Banner
# Register your models here.
admin.site.register([GoodsCategory, GoodsCategoryBrand, Goods, GoodsImage, Banner]),
