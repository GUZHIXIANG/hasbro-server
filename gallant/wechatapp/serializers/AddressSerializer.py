from rest_framework import serializers
from wechatapp.models.AddressModel import *

class AddressDetailSerializer(serializers.ModelSerializer):
    province_name = serializers.CharField(source='province.name')
    city_name = serializers.CharField(source='city.name')
    district_name = serializers.CharField(source='district.name')

    class Meta:
        model = Address
        fields = ("name","mobile","province","province_name","city","city_name","district","district_name","address","is_default")


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ("user","name","mobile","province","city","district","address","is_default")
    
    def create(self,validate_data):
        Address.objects.create(**validate_data)
    
    def update(self, instance, validated_data):
        for item in validated_data:
            if Address._meta.get_field(item):
                setattr(instance, item, validated_data[item])
        instance.save()
        return instance
