# Generated by Django 2.2.7 on 2020-02-17 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wechatapp', '0003_auto_20200217_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mytrolly',
            name='checkbox',
            field=models.IntegerField(choices=[(0, '未选中'), (1, '选中')], default=0),
        ),
    ]
