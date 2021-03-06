# Generated by Django 2.1.5 on 2019-03-22 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_cms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleComment',
            fields=[
                ('article_comment_id', models.AutoField(help_text='主键', primary_key=True, serialize=False)),
                ('article_id', models.IntegerField(default=0, help_text='文章id')),
                ('comment', models.CharField(default='', max_length=200)),
                ('remote_addr', models.CharField(help_text='远程ip', max_length=30)),
                ('locate_area', models.CharField(help_text='所在区域', max_length=20)),
                ('created_at', models.DateTimeField(blank=True, default='2019-01-29 12:13:00', help_text='创建时间', null=True)),
            ],
        ),
    ]
