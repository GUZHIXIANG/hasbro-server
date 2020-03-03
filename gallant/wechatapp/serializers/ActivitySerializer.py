from rest_framework import serializers
from wechatapp.models.ActivityModel import *


class ActivityStoreSerializer(serializers.ModelSerializer):
    # store_name = serializers.CharField(source='store_name',required=False)
    class Meta:
        model = ActivityStore
        fields = ('store',)
    

class ActivityImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityImage
        fields = ('image', 'image_type')

class ActivityTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityText
        fields = ('title', 'text')


class ActivitySerializer(serializers.ModelSerializer):
    activity_start_datetime = serializers.DateTimeField(
        format='%Y-%m-%d %H:%M')
    activity_end_datetime = serializers.DateTimeField(
        format='%Y-%m-%d %H:%M')
    activity_type = serializers.CharField(
        source='activity_type.activity_type')
    # super_activity = serializers.CharField(
    #     source='super_activity.activity_name')

    activity_store = serializers.SerializerMethodField()

    class Meta:
        model = Activity
        fields = ("id", "activity_start_datetime", "activity_end_datetime",
                  "activity_type", "activity_store", "activity_name", "super_activity")
    
    def get_activity_store(self, obj):
        query_set = obj.activity_store.all()
        return [{'store_name': obj.store_name} for obj in query_set]


class ActivityDetailSerializer(serializers.ModelSerializer):
    activity_start_datetime = serializers.DateTimeField(
        format='%Y-%m-%d %H:%M')
    activity_end_datetime = serializers.DateTimeField(
        format='%Y-%m-%d %H:%M')
    activity_type = serializers.CharField(
        source='activity_type.activity_type')
    # super_activity = serializers.CharField(
    #     source='super_activity.activity_name')

    activity_image = serializers.SerializerMethodField()
    activity_text = serializers.SerializerMethodField()
    activity_store = serializers.SerializerMethodField()

    class Meta:
        model = Activity
        fields = "__all__"

    def get_activity_image(self, obj):
        query_set = obj.activity_image.all()
        return [{'image': obj.image, 'image_type': obj.get_image_type_display()} for obj in query_set]
    
    def get_activity_text(self, obj):
        query_set = obj.activity_text.all()
        return [{'title': obj.title, 'text': obj.text} for obj in query_set]

    def get_activity_store(self, obj):
        query_set = obj.activity_store.all()
        return [{'store_id': obj.id, 'store_name': obj.store_name, 
        'store_area': obj.store_area,'store_address': obj.store_address, 'store_telephone': obj.store_telephone,} for obj in query_set]
 

class ActivityCreateSerializer(serializers.ModelSerializer):
    activity_store = ActivityStoreSerializer(many=True, partial=True)
    activity_image = ActivityImageSerializer(many=True, partial=True)
    activity_text = ActivityTextSerializer(many=True, partial=True)
    super_activity = serializers.IntegerField(required=False)
    class Meta:
        model = Activity
        # fields = "__all__"
        fields = ("activity_name",
                  "activity_descripation",
                  "activity_type",
                  "activity_start_datetime",
                  "activity_end_datetime",
                  "super_activity",
                  "activity_store",
                  "activity_image",
                  "activity_text")

    def create(self, validated_data):
        store_data = validated_data.pop(
            'activity_store') if 'activity_store' in validated_data else None
        image_data = validated_data.pop(
            'activity_image') if 'activity_image' in validated_data else None
        text_data = validated_data.pop(
            'activity_text') if 'activity_text' in validated_data else None
        # 活动信息
        activity = Activity.objects.create(**validated_data)
        # 关联门店
        if store_data:
            for store in store_data:
                d = dict(store)
                ActivityStore.objects.create(
                    activity=activity, 
                    store=d['store']
                    )
        # 关联图片
        if image_data:
            for image in image_data:
                d = dict(image)
                ActivityImage.objects.create(
                    activity=activity, 
                    image=d['image'],
                    image_type=d['image_type']
                    )

        # 关联文本
        if text_data:
            for text in text_data:
                d = dict(text)
                ActivityText.objects.create(
                    activity=activity, 
                    title=d['title'],
                    text=d['text']
                    )

        return activity




class ActivityUpdateSerializer(serializers.ModelSerializer):
    activity_store = ActivityStoreSerializer(many=True, partial=True)
    activity_image = ActivityImageSerializer(many=True, partial=True)
    activity_text = ActivityTextSerializer(many=True, partial=True)
    class Meta:
        model = Activity
        fields = ("activity_name",
                  "activity_descripation",
                  "activity_type",
                  "activity_start_datetime",
                  "activity_end_datetime", 
                  "super_activity",
                  "activity_store",
                  "activity_image",
                  "activity_text")

    def update(self, instance, validated_data):
        store_data = validated_data.pop(
            'activity_store') if 'activity_store' in validated_data else None
        image_data = validated_data.pop(
            'activity_image') if 'activity_image' in validated_data else None
        image_text = validated_data.pop(
            'activity_text') if 'activity_text' in validated_data else None
        # 活动信息
        for item in validated_data:
            if Activity._meta.get_field(item):
                setattr(instance, item, validated_data[item])
        # 关联门店
        if store_data:
            ActivityStore.objects.filter(activity=instance).delete()
            for store in store_data:
                d = dict(store)
                ActivityStore.objects.create(
                    activity=instance,
                    store=d['store']
                )

        # 关联图片
        if image_data:
            ActivityImage.objects.filter(activity=instance).delete()
            for image in image_data:
                d = dict(image)
                ActivityImage.objects.create(
                    activity=instance,
                    image=d['image'],
                    image_type=d['image_type']
                )

        # 关联文本
        if text_data:
            for text in text_data:
                d = dict(text)
                ActivityText.objects.create(
                    activity=activity, 
                    title=d['title'],
                    text=d['text']
                    )
        
        instance.save()
        return instance


'''################### 活动类型 ###################'''


class ActivityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityType
        fields = "__all__"

    
class ActivityTypeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityType
        fields = ("activity_type",)

    def create(self, validated_data):
        return ActivityType.objects.create(**validated_data)


class ActivityTypeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityType
        fields = ("activity_type",)

    def update(self, instance, validated_data):
        instance.activity_type = validated_data.get('activity_type', instance.activity_type)
        instance.save()
        return instance
