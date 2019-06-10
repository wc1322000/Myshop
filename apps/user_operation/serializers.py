# -*- coding: utf-8 -*-
# @Time    : 2019/6/5 15:21
# @Author  : wei
# @FileName: serializers.py
from rest_framework import serializers
from .models import UserFav, UserLeavingMessage, UserAddress
from rest_framework.validators import UniqueTogetherValidator
from goods.serializers import GoodsSerializer


class UserFavDetailSerializer(serializers.ModelSerializer):
    '''
    用户收藏详情
    '''

    # 通过商品id获取收藏的商品，需要嵌套商品的序列化
    goods = GoodsSerializer()

    class Meta:
        model = UserFav
        fields = ("goods", "id")


class UserFavSerializer(serializers.ModelSerializer):
    # 获取当前登录的用户
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        # validate实现唯一联合，一个商品只能收藏一次
        validators = [
            UniqueTogetherValidator(
                queryset=UserFav.objects.all(),
                fields=('user', 'goods'),
                # message的信息可以自定义
                message="已经收藏"
            )
        ]
        model = UserFav
        # 收藏的时候需要返回商品的id，因为取消收藏的时候必须知道商品的id是多少
        fields = ("user", "goods", 'id')


class LeavingMessageSerializer(serializers.ModelSerializer):
    # 获取当前登录的用户
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = UserLeavingMessage
        fields = ("user", "message_type", "subject", "message", "file", "id", "add_time")


class AddressSerializer(serializers.ModelSerializer):
    # 获取当前登录的用户
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = UserAddress
        fields = ("id", "user", "province", "city", "district", "address", "signer_name", "signer_mobile", "add_time")