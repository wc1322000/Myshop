"""Myshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from Myshop.settings import MEDIA_ROOT
from goods.views import GoodsListViewSet, CategoryViewSet
from users.views import SmsCodeViewset, UserViewset
from user_operation.views import UserFavViewset, LeavingMessageViewset, AddressViewset
from trade.views import ShoppingCartViewset, OrderViewset, AlipayView
from django.views.generic import TemplateView

router = DefaultRouter()
router.register(r'goods', GoodsListViewSet, base_name='goods')
router.register(r'categories', CategoryViewSet, base_name='categories')
router.register(r'codes', SmsCodeViewset, base_name="codes")
router.register(r'users', UserViewset, base_name="users")
router.register(r'userfavs', UserFavViewset, base_name='userfavs')
router.register(r'messages', LeavingMessageViewset, base_name='messages')
router.register(r'address', AddressViewset, base_name='address')
router.register(r'shopcarts', ShoppingCartViewset, base_name='shopcarts')
router.register(r'orders', OrderViewset, base_name='orders')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('ueditor/', include('DjangoUeditor.urls')),
    path('docs/', include_docs_urls(title='电商网站')),
    #文件
    path('media/<path:path>', serve, {'document_root': MEDIA_ROOT}),
    path('', include(router.urls)),
    #drf自带的token认证模式
    #path('api-token-auth/', views.obtain_auth_token),
    #jwt的认证接口
    path('login/', obtain_jwt_token),
    # 首页
    path('index/', TemplateView.as_view(template_name='index.html'), name='index'),
    #simple jwt的认证接口
    # path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('alipay/return/', AlipayView.as_view(), name='alipay'),
]
