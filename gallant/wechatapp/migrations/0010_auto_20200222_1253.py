# Generated by Django 2.2.7 on 2020-02-22 12:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wechatapp', '0009_auto_20200218_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttype',
            name='typeName',
            field=models.CharField(max_length=50, verbose_name='商品总类'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='nickName',
            field=models.CharField(max_length=100, verbose_name='用户昵称'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='用户微信id'),
        ),
    ]
