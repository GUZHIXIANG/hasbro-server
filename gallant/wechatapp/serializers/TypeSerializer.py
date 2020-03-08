from rest_framework import serializers
from wechatapp.models.ProductTypeModel import ProductSecondCategory,ProductType,ProductMainCategory,PType,PTypeImage


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
    # image = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()

    class Meta:
        model = PType
        fields = ('id','parent','name','desc','images')
    
    def get_parent(self, obj):
        return obj.parent.id
    
    def get_desc(self, obj):
        return obj.get_desc_display()

    # def get_image(self, obj):
    #     return obj.type_image.get().image

    def get_images(self, obj):
        query_set = obj.type_image.all()
        return [{'image': obj.image.thumbnail.__str__()} for obj in query_set]
