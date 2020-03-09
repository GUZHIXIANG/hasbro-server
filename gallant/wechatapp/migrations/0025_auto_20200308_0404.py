# Generated by Django 2.2.7 on 2020-03-08 04:04

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('wechatapp', '0024_auto_20200308_0324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ptype',
            name='name',
            field=models.CharField(max_length=20, unique=True, verbose_name='类型'),
        ),
        migrations.AlterField(
            model_name='ptypeimage',
            name='image',
            field=stdimage.models.StdImageField(default='', upload_to='PTypeImage', verbose_name='图片路径'),
        ),
    ]