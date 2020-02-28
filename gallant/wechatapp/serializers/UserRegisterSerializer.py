from rest_framework import serializers
from wechatapp.models.UserModel import UserProfile,User

class UserBaseInfoSerializer(serializers.ModelSerializer):
   class Meta:
        model = User
        fields = ("username","password")
   def create(self, validated_data):
        return User.objects.create(**validated_data)

class UserWxInfoSerializer(serializers.ModelSerializer):
   
   user = UserBaseInfoSerializer()
   
   class Meta:
        model = UserProfile
        fields = ('avatarUrl','nickName','gender','country','province','city','language','user')
        
   def create(self, validated_data):
        profile = validated_data.pop('user')
        user  = User.objects.create(**profile)
        user.save()
        userinfo = UserProfile.objects.create(user=user,**validated_data)
        userinfo.save()
        return userinfo




