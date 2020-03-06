from django.db import models

class Test(models.Model):
    name = models.CharField(verbose_name='姓名',max_length=10)
    age = models.IntegerField(verbose_name='年龄')
    CHOICE = ((0,'未知'),(1,'男'),(2,'女'))
    sex = models.IntegerField(verbose_name='性别',choices=CHOICE,default=0)
    type = models.ForeignKey('Type',on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.name.__str__()
    
    class Meta:
        app_label = 'wechatapp'
        verbose_name = 'Test'
        verbose_name_plural = '测试用例'


class Test2(models.Model):
    user = models.ForeignKey(Test,on_delete=models.CASCADE,related_name='test2')
    phone = models.CharField(verbose_name='手机号',max_length=13)
    class Meta:
        app_label = 'wechatapp'
        verbose_name = 'Test2'
        verbose_name_plural = '测试用例2'
    def __str__(self):
        return self.phone.__str__()


class Type(models.Model):
    name = models.CharField(verbose_name='类别名', max_length=10)
    desc = models.CharField(verbose_name='类别描述', max_length=100)

    class Meta:
        app_label = 'wechatapp'
        verbose_name = 'Type'
        verbose_name_plural = '测试用例3'

    def __str__(self):
        return self.name.__str__()
