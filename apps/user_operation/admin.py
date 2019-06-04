from django.contrib import admin
from user_operation.models import UserFav, UserAddress,UserLeavingMessage
# Register your models here.
admin.site.register([UserFav, UserAddress,UserLeavingMessage])