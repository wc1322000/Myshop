from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import UserFav
from .serializers import UserFavSerializer
from utils.permissions import IsOwnerOrReadOnly
# Create your views here.


class UserFavViewset(viewsets.ModelViewSet):
    """
    用户收藏功能
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    serializer_class = UserFavSerializer
    authentication_classes = (SessionAuthentication, JWTAuthentication)
    lookup_field = "goods_id"

    def get_queryset(self):
        return UserFav.objects.filter(user=self.request.user)
