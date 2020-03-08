# Generated by Django 2.2.7 on 2020-03-07 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wechatapp', '0009_activityimage_image_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityimage',
            name='image_description',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='图片描述'),
        ),
        migrations.AlterField(
            model_name='activitytext',
            name='text',
            field=models.TextField(verbose_name='文本正文'),
        ),
    ]