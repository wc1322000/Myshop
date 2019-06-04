from django.contrib import admin
from users.models import UserProfile, VerifyCode
# Register your models here.
admin.site.register([UserProfile, VerifyCode])