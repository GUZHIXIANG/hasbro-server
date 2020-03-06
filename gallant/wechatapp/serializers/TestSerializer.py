from rest_framework import serializers
from wechatapp.models.TestModel import *

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'