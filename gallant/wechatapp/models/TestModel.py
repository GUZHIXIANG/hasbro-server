from django.db import models

class Test(models.Model):
    name = models.CharField(verbose_name='姓名',max_length=10)
    age = models.IntegerField(verbose_name='年龄')
    CHOICE = ((0,'未知'),(1,'男'),(2,'女'))
    sex = models.IntegerField(verbose_name='性别',choices=CHOICE,default=0)

    # def __str__(self):
    #     return self.name.__str__()
    
    class Meta:
        app_label = 'wechatapp'
        verbose_name = 'Test'
        verbose_name_plural = '测试用例'
