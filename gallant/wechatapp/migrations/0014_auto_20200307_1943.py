# Generated by Django 2.2.7 on 2020-03-07 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wechatapp', '0013_course_student_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mytrolly',
            name='checkbox',
            field=models.BooleanField(choices=[(0, '未选中'), (1, '选中')], default=False),
        ),
    ]
