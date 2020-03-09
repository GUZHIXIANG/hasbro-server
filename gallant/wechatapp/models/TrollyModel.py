from django.db import models
from wechatapp.models.ProductModel import ProductBaseInfo
from wechatapp.models.UserModel import UserProfile
"""
用户发生购买之前可以添加购物车,

1. 用户必须登陆之后才能使用该模型
2. 
"""
class MyTrolly(models.Model):

    CHOOSE = (
        (0,'未选中'),
        (1,'选中'),
    )

    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name="userid")
    
    productbaseinfo = models.ForeignKey(ProductBaseInfo,on_delete=models.CASCADE,related_name="product")
    
    nums = models.IntegerField(blank=False,default=1)
 
    checkbox = models.BooleanField(choices=CHOOSE,default=False)
    
    def __str__(self):
        return self.user.__str__()
    
    class Meta:
        app_label = 'wechatapp'
        verbose_name = '购物车管理'
        verbose_name_plural =  '购物车管理'