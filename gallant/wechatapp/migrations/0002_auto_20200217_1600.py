# Generated by Django 2.2.7 on 2020-02-17 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wechatapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mytrolly',
            options={'verbose_name': '购物车管理', 'verbose_name_plural': '购物车管理'},
        ),
        migrations.AlterModelOptions(
            name='productbaseinfo',
            options={'verbose_name': '商品详情管理', 'verbose_name_plural': '商品详情管理'},
        ),
        migrations.AlterModelOptions(
            name='producttag',
            options={'verbose_name': '商品标签管理', 'verbose_name_plural': '商品标签管理'},
        ),
        migrations.AlterModelOptions(
            name='producttype',
            options={'verbose_name': '商品类别管理', 'verbose_name_plural': '商品类别管理'},
        ),
        migrations.AlterModelOptions(
            name='producturl',
            options={'verbose_name': '商品图片管理', 'verbose_name_plural': '商品图片管理'},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': '用户微信注册信息详情', 'verbose_name_plural': '用户微信注册信息详情'},
        ),
        migrations.AddField(
            model_name='producttype',
            name='typeChildsName',
            field=models.CharField(default='子类产品', max_length=50, verbose_name='商品子类'),
        ),
        migrations.AlterField(
            model_name='productbaseinfo',
            name='productId',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='货号'),
        ),
        migrations.AlterField(
            model_name='productbaseinfo',
            name='productName',
            field=models.CharField(max_length=255, verbose_name='商品名称'),
        ),
        migrations.AlterField(
            model_name='producttype',
            name='typeChildName',
            field=models.CharField(default='大类产品', max_length=50, verbose_name='商品大类'),
        ),
        migrations.AlterField(
            model_name='producttype',
            name='typeName',
            field=models.CharField(max_length=50, unique=True, verbose_name='商品总类'),
        ),
    ]