# Generated by Django 2.2.7 on 2020-03-08 03:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wechatapp', '0020_auto_20200308_0256'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ptag',
            options={'verbose_name': '商品标签*', 'verbose_name_plural': '商品标签管理*'},
        ),
        migrations.AlterModelOptions(
            name='ptype',
            options={'verbose_name': '商品类型*', 'verbose_name_plural': '商品类型管理*'},
        ),
        migrations.AlterModelOptions(
            name='ptypeimage',
            options={'verbose_name': '商品类型图片*', 'verbose_name_plural': '商品类型图片管理*'},
        ),
    ]