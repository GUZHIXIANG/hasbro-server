# Generated by Django 2.2.7 on 2020-03-08 18:18

from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('wechatapp', '0027_delete_ptypeimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='PTypeImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', stdimage.models.StdImageField(default='', upload_to='PTypeImage', verbose_name='图片路径')),
                ('ptype', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='type_image', to='wechatapp.PType', verbose_name='商品类型')),
            ],
            options={
                'verbose_name': '商品类型图标*',
                'verbose_name_plural': '商品类型图标管理*',
            },
        ),
    ]