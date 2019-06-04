from django.contrib import admin
from trade.models import ShoppingCart, OrderInfo, OrderGoods
# Register your models here.
admin.site.register([ShoppingCart, OrderInfo, OrderGoods])