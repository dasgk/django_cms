# Generated by Django 2.1.2 on 2019-05-16 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_cms', '0004_articlecomment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='cate',
            name='picture',
            field=models.CharField(default='', help_text='类别图片', max_length=200, null=True),
        ),
    ]