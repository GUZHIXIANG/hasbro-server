from django.db import models


class Author(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=10)
    age = models.IntegerField(verbose_name='年龄')
    CHOICE = ((0, '未知'), (1, '男'), (2, '女'))
    sex = models.IntegerField(verbose_name='性别', choices=CHOICE, default=0)

    def __str__(self):
        return self.name.__str__()

    class Meta:
        app_label = 'newapp1'
        verbose_name = '作者信息'
        verbose_name_plural = '作者信息管理'


class Book(models.Model):
    name = models.CharField(verbose_name='书名', max_length=10)
    page = models.IntegerField(verbose_name='页数')

    def __str__(self):
        return self.name.__str__()

    class Meta:
        app_label = 'newapp1'
        verbose_name = '书本信息'
        verbose_name_plural = '书本信息管理'
