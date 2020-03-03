# Generated by Django 2.2.7 on 2020-03-03 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wechatapp', '0015_auto_20200301_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='activity_name',
            field=models.CharField(max_length=100, unique=True, verbose_name='活动名'),
        ),
        migrations.CreateModel(
            name='ActivityText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='文本标题')),
                ('text', models.TextField(blank=True, verbose_name='文本正文')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_text', to='wechatapp.Activity')),
            ],
            options={
                'verbose_name': 'ActivityText',
                'verbose_name_plural': '活动文本表',
            },
        ),
    ]
