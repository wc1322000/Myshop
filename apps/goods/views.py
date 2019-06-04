from .models import Goods,GoodsCategory
from .serializers import GoodsSerializer, CategorySerializer
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .filters import GoodsFilter
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
# Create your views here.

class GoodsPagination(PageNumberPagination):
    '''
    商品列表自定义分页
    '''
    #默认每页显示的个数
    page_size = 12
    #可以动态改变每页显示的个数
    page_size_query_param = 'page_size'
    #页码参数
    page_query_param = 'page'
    #最多能显示多少页
    max_page_size = 100


class GoodsListViewSet(viewsets.ReadOnlyModelViewSet):
    """
    商品列表页.
    """
    queryset = Goods.objects.all().order_by('id')
    # 分页
    pagination_class = GoodsPagination
    #身份认证
    #authentication_classes = (TokenAuthentication,)
    # 序列化
    serializer_class = GoodsSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    # 设置filter的类为我们自定义的类
    # 过滤
    filter_class = GoodsFilter
    # 搜索
    search_fields = ('name', 'goods_brief', 'goods_desc')
    # 排序
    ordering_fields = ('sold_num', 'shop_price')


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    商品分类列表
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer
