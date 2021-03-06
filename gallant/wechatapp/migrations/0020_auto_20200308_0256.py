# Generated by Django 2.2.7 on 2020-03-08 02:56

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('wechatapp', '0019_auto_20200308_0225'),
    ]

    operations = [
        migrations.CreateModel(
            name='PTypeImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', stdimage.models.StdImageField(default='', upload_to='PTypeImage', verbose_name='活动图片')),
            ],
            options={
                'verbose_name': '商品类型图片',
                'verbose_name_plural': '商品类型图片管理',
            },
        ),
        migrations.AlterModelOptions(
            name='activity',
            options={'verbose_name': '活动信息', 'verbose_name_plural': '活动信息管理'},
        ),
        migrations.AlterModelOptions(
            name='activityimage',
            options={'verbose_name': '活动图片', 'verbose_name_plural': '活动图片管理'},
        ),
        migrations.AlterModelOptions(
            name='activitytext',
            options={'verbose_name': '活动文本', 'verbose_name_plural': '活动文本管理'},
        ),
        migrations.AlterModelOptions(
            name='activitytype',
            options={'verbose_name': '活动类型', 'verbose_name_plural': '活动类型管理'},
        ),
        migrations.AlterModelOptions(
            name='signup',
            options={'verbose_name': '报名信息', 'verbose_name_plural': '报名信息查看'},
        ),
        migrations.AlterModelOptions(
            name='store',
            options={'verbose_name': '门店信息', 'verbose_name_plural': '门店信息管理'},
        ),
        migrations.AlterField(
            model_name='activity',
            name='activity_end_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='结束时间'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='activity_start_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='开始时间'),
        ),
        migrations.CreateModel(
            name='PType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='类型名称')),
                ('desc', models.CharField(max_length=20, unique=True, verbose_name='类型')),
                ('activity_create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('activity_operate_time', models.DateTimeField(auto_now=True, verbose_name='操作时间')),
                ('image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wechatapp.PTypeImage', verbose_name='图片')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wechatapp.PType', verbose_name='父类型')),
            ],
            options={
                'verbose_name': '商品类型',
                'verbose_name_plural': '商品类型管理',
            },
        ),
    ]
