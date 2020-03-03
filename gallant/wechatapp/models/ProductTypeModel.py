from django.db import models
from datetime import datetime
from stdimage.models import StdImageField

# 商品分类表用于客户定义产品分类类别的
# 这里使用一张表来完成分类，
class ProductType(models.Model):
    
    # 商品总类 ------- 名称
    typeName = models.CharField('商品总类',max_length=50,blank=False)

    # 商品大类
    typeChildName = models.CharField('商品大类',max_length=50,blank=False,default='大类产品')

    # 商品子类
    typeChildsName = models.CharField('商品子类',max_length=50,blank=False,default='子类产品')

    def __str__(self):
        return "["+self.typeName.__str__()+"]"+"["+self.typeChildName.__str__()+"]"+"["+self.typeChildsName.__str__()+"]"

    class Meta:
        app_label = 'wechatapp'
        verbose_name = '商品类别管理'
        verbose_name_plural = '商品类别管理'
    