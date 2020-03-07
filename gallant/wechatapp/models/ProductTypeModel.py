from django.db import models
from datetime import datetime
from stdimage.models import StdImageField

# 商品分类表用于客户定义产品分类类别的
# 这里使用一张表来完成分类，


class ProductMainCategory(models.Model):
    # 商品总类 ------- 名称
    typeName = models.CharField('商品总类',max_length=50,blank=False)

    def __str__(self):
        return self.typeName.__str__()

    class Meta:
        app_label = 'wechatapp'
        verbose_name = '商品总类注册'
        verbose_name_plural = '商品总类注册'


class ProductSecondCategory(models.Model):
    # 商品大类 ------- 名称
    typeName = models.ForeignKey(ProductMainCategory,on_delete=models.CASCADE)

    typeChildName =  models.CharField('商品大类',max_length=50,blank=False)

    url = StdImageField(verbose_name="大类缩略图",upload_to='typea',variations={'nail': {'width': 10, 'height': 10}},default='')

    banner_url = StdImageField(verbose_name="大类广告",upload_to='typeadv',default='')
    
    banner_name = models.CharField('大类广告名称',max_length=50,blank=False,default='')

    def __str__(self):
        return self.typeChildName.__str__()

    class Meta:
        app_label = 'wechatapp'
        verbose_name = '商品大类注册'
        verbose_name_plural = '商品大类注册'

    def image_img(self):
        if self.url:
            return str('<img src="%s" />' % self.url.nail.url)
        else:
            return u'上传图片'
    
    def image_img1(self):
        if self.banner_url:
            return str('<img src="%s" />' % self.banner_url.url)
        else:
            return u'上传图片'

    image_img.short_description = '图标'
    image_img.allow_tags = True

    image_img1.short_description = '广告'
    image_img1.allow_tags = True

class ProductType(models.Model):
    
    # 商品大类
    typeChildName = models.ForeignKey(ProductSecondCategory,on_delete=models.CASCADE)

    # 商品子类
    typeChildsName = models.CharField('商品子类',max_length=50,blank=False,default='子类产品')

    url = StdImageField(verbose_name="子类缩略图",upload_to='typeb',variations={'nail': {'width': 25, 'height': 25}},default='')

    def __str__(self):
        return self.typeChildsName.__str__()

    class Meta:
        app_label = 'wechatapp'
        verbose_name = '商品类别管理'
        verbose_name_plural = '商品类别管理'

    def image_img(self):
        if self.url:
            return str('<img src="%s" />' % self.url.nail.url)
        else:
            return u'上传图片'

    image_img.short_description = '类别缩略图'
    image_img.allow_tags = True