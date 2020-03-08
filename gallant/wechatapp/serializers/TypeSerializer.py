from rest_framework import serializers
from wechatapp.models.ProductTypeModel import ProductSecondCategory,ProductType,ProductMainCategory


class ProductSecondCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSecondCategory
        fields = "__all__"

class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = "__all__"

class ProductMainCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMainCategory
        fields = "__all__"