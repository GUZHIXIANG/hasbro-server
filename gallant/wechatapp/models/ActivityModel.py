from django.db import models
from django.utils import timezone
from wechatapp.models.StoreModel import Store

# 活动信息表
class Activity(models.Model):
    # 父活动 ----- 自关联
    super_activity = models.ForeignKey(
        'self', on_delete=models.CASCADE, blank=True,null=True)
    # 活动类型 ----- 关联活动类型表
    activity_type = models.ForeignKey(
        'ActivityType', on_delete=models.CASCADE, default=1)
    # 关联门店 ----- 关联门店信息表
    activity_store = models.ManyToManyField(
        Store, through='ActivityStore', related_name='activity_store')
    # 活动名
    activity_name = models.CharField(
        verbose_name='活动名', max_length=100,unique=True)
    # 活动描述
    activity_descripation = models.TextField(verbose_name='活动描述', blank=True)
    # 活动开始时间
    activity_start_datetime = models.DateTimeField(
        verbose_name='活动开始时间', default=timezone.now())
    # 活动结束时间
    activity_end_datetime = models.DateTimeField(
        verbose_name='活动结束时间', default=timezone.now())
    # 创建时间
    activity_create_time = models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    # 操作时间
    activity_operate_time = models.DateTimeField(verbose_name='操作时间',auto_now=True)

    def __str__(self):
        return self.activity_name.__str__()

    class Meta:
        app_label = 'wechatapp'
        verbose_name = 'Activity'
        verbose_name_plural = '活动信息表'

class ActivityStore(models.Model):
    # 活动 ----- 关联活动信息表
    activity = models.ForeignKey(
        Activity, on_delete=models.CASCADE)
    # 门店 ----- 关联门店信息表
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    class Meta:
        app_label = 'wechatapp'
        verbose_name = 'ActivityStore'
        verbose_name_plural = '活动门店关联表'


# 活动类型表
class ActivityType(models.Model):
    # 活动类型
    activity_type = models.CharField(verbose_name='活动类型',max_length=16,unique=True)

    def __str__(self):
        return self.activity_type.__str__()

    class Meta:
        app_label = 'wechatapp'
        verbose_name = 'ActivityType'
        verbose_name_plural = '活动类型表'

# 活动图片表
class ActivityImage(models.Model):
    # 关联活动 ----- 关联活动基础表
    activity = models.ForeignKey('Activity',on_delete=models.CASCADE,related_name='activity_image')
    # 活动图片
    image = models.URLField(verbose_name='活动图片',max_length=250)
    # 图片类型
    IMAGE_TYPE = (
        (1, 'type1'),
        (2, 'type2'),
        (3, 'type3'),
    )
    image_type = models.IntegerField(verbose_name='图片类型',choices=IMAGE_TYPE,default=1)

    def __str__(self):
        return self.image.__str__()

    class Meta:
        app_label = 'wechatapp'
        verbose_name = 'ActivityImage'
        verbose_name_plural = '活动图片表'


# 活动文本表
class ActivityText(models.Model):
    # 关联活动 ----- 关联活动基础表
    activity = models.ForeignKey('Activity',on_delete=models.CASCADE,related_name='activity_text')
    # 文本标题
    title = models.CharField(
        verbose_name='文本标题', max_length=100)
    # 文本正文
    text = models.TextField(verbose_name='文本正文', blank=True)

    def __str__(self):
        return self.title.__str__()

    class Meta:
        app_label = 'wechatapp'
        verbose_name = 'ActivityText'
        verbose_name_plural = '活动文本表'