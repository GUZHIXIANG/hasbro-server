# Generated by Django 2.2.7 on 2020-03-07 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wechatapp', '0006_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wechatapp.Type'),
        ),
    ]
