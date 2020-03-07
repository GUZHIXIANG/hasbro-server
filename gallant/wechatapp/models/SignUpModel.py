from django.db import models
from django.contrib.auth.models import User
from wechatapp.models.ActivityModel import Activity
from wechatapp.models.StoreModel import Store


# 报名信息表
class SignUp(models.Model):
    # 活动关联 ----- 关联活动信息表
    activity = models.ForeignKey('Activity', on_delete=models.CASCADE, blank=True,verbose_name='报名活动')
    # 活动门店 ----- 关联门店信息表
    store = models.ForeignKey(
        'Store', on_delete=models.CASCADE, blank=True, verbose_name='活动门店')
    # 活动用户 ----- 关联用户信息表
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, verbose_name='报名用户')
    # 报名人姓名
    signup_name = models.CharField(
        verbose_name='参加者姓名', max_length=128, blank=True)
    # 报名人电话
    signup_phone = models.CharField(
        verbose_name='参加者电话', max_length=128, blank=True)
    # 创建时间
    signup_create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    # 操作时间
    signup_operate_time = models.DateTimeField(verbose_name='操作时间', auto_now=True)

    
    def __str__(self):
        return self.user.__str__()

    class Meta:
        app_label = 'wechatapp'
        verbose_name = 'SignUp'
        verbose_name_plural = '报名信息查看'

