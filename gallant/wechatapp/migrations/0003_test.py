# Generated by Django 2.2.7 on 2020-03-07 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wechatapp', '0002_auto_20200306_2224'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='姓名')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('sex', models.IntegerField(choices=[(0, '未知'), (1, '男'), (2, '女')], default=0, verbose_name='性别')),
            ],
            options={
                'verbose_name': 'Test',
                'verbose_name_plural': '测试用例',
            },
        ),
    ]