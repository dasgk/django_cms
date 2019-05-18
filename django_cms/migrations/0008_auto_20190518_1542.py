# Generated by Django 2.1.2 on 2019-05-18 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_cms', '0007_articlerate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='like_num',
        ),
        migrations.AddField(
            model_name='article',
            name='rate_num',
            field=models.FloatField(default=0, help_text='评分数值', null=True),
        ),
    ]
