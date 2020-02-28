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
    
# 商品基础信息表
class ProductBaseInfo(models.Model):

    CHOOSE = (
        ('on','上架'),
        ('off','下架'),
    )

    # 货号 ------- 主键
    productId   = models.CharField('货号',max_length=100,primary_key=True)
    # 品名
    productName = models.CharField('商品名称',max_length=255)
    # 分类 ------- 关联类目信息
    productType = models.ForeignKey(ProductType,on_delete=models.CASCADE)
    # 系统编码
    systemCode  = models.BigIntegerField(blank=True)
    # 条形编码
    barCode  = models.BigIntegerField(blank=True)
    # 颜色
    color = models.CharField(max_length=255,blank=True)
    # 规格
    norms = models.CharField(max_length=255,blank=True)
    # 重量
    weight = models.IntegerField(blank=True)
    # 价格  
    price = models.IntegerField(blank=False)
    
    # 商品详情
    description = models.TextField(blank=True)
    # 商品简介
    brief = models.TextField(blank=True,default="这里是商品简介")
    # 品牌
    brand = models.TextField(blank=True,default="这里是商品牌")

    # 缩略图
    smallurl = StdImageField(verbose_name="商品展示缩略图",upload_to='ProductPreViewPic',variations={'nail': {'width': 100, 'height': 75}},default='')
    
    shell = models.CharField(max_length=3, choices=CHOOSE,default='on')
    
    quantity = models.IntegerField(blank=False,default=500)
    
    def __str__(self):
        return self.productId.__str__()+"["+self.productName.__str__()+"]"+"("+self.norms.__str__()+")"

    class Meta:
        app_label = 'wechatapp'
        verbose_name = '商品详情管理'
        verbose_name_plural = '商品详情管理'

    def image_img(self):
        if self.smallurl:
            return str('<img src="%s" />' % self.smallurl.nail.url)
        else:
            return u'上传图片'

    image_img.short_description = '商品展示缩略图'
    image_img.allow_tags = True

    
# 商品图片链接表  多个图片链接关联到一个商品上
class ProductUrl(models.Model):

    # 外键关联了
    productbaseinfo = models.ForeignKey(ProductBaseInfo,on_delete=models.CASCADE,related_name="url")

    # 图片链接
    url = StdImageField(verbose_name='商品详情轮播图',upload_to='img',variations={'product': {'width': 375, 'height': 400}},default='')

    def __str__(self):
        return self.url.__str__()

    class Meta:
        app_label = 'wechatapp'
        verbose_name = '商品图片管理'
        verbose_name_plural = '商品图片管理'
    
    def image_img(self):
        if self.url:
            return str('<img src="%s" />' % self.url.product.url)
        else:
            return u'上传图片'

    image_img.short_description = '商品展示缩略图'
    image_img.allow_tags = True

class ProductTag(models.Model):

    tag_type = (
        ('h', '热门商品'),
        ('d', '降价促销'),
        ('n', '新品上架'),
    )

    # 外键关联了
    productbaseinfo = models.OneToOneField(ProductBaseInfo,on_delete=models.CASCADE,primary_key=True)
    
    # 标签
    tag = models.CharField(max_length=1, choices=tag_type)

    def __str__(self):
        return self.tag.__str__()

    class Meta:
        app_label = 'wechatapp'
        verbose_name = '商品标签管理'
        verbose_name_plural = '商品标签管理'
