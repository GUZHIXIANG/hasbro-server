from rest_framework import serializers
from wechatapp.models.ProductModel import (ProductBaseInfo,ProductUrl,ProductTag)




class ProductSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = ProductBaseInfo
        fields = "__all__"
    #     fields = ('productId','productName','productType','systemCode','barCode','color','norms','weight','price','descripation')
    
    # def create(self, validated_data):
    #     productType = validated_data.pop('productTyper')
    #     ptype = ProductType.objects.get(typeName=productType)
    #     product = ProductBaseInfo.objects.create(productType=ptype,**validated_data)
    #     product.save()
    #     return product

class ProductUrlSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductUrl
        fields = ("url",)

class ProductTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductTag
        fields = ("tag",)


class ProductAllSerializer(serializers.ModelSerializer):
    #url = serializers.StringRelatedField(many=True)
    class Meta:
        model = ProductBaseInfo
        fields = ("productId","productName","smallurl","price")

    
 
class ItemsAllSerializer(serializers.ModelSerializer):
    url = serializers.StringRelatedField(many=True)
    class Meta:
        model = ProductBaseInfo
        fields = ("productId","productName","url","price",'color','norms','weight','descripation','shell',"quantity")
