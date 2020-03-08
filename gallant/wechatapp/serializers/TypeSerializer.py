from rest_framework import serializers
from wechatapp.models.ProductTypeModel import *


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


class PTypeImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PTypeImage
        fields = '__all__'


class PTypeSerializer(serializers.ModelSerializer):

    parent = serializers.SerializerMethodField()
    desc = serializers.SerializerMethodField()
    image = serializers.CharField(source='type_image.image')

    class Meta:
        model = PType
        fields = ('id','parent','name','desc','image')

    def get_parent(self, obj):
        return obj.parent.id
    
    def get_desc(self, obj):
        return obj.get_desc_display()

    