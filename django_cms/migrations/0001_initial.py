# Generated by Django 2.1.5 on 2019-02-24 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminUser',
            fields=[
                ('admin_user_id', models.IntegerField(help_text='主键', primary_key=True, serialize=False)),
                ('username', models.CharField(help_text='管理员的用户名', max_length=200)),
                ('password', models.CharField(help_text='管理员的密码', max_length=200)),
                ('api_token', models.CharField(help_text='文章内容', max_length=200)),
                ('status', models.IntegerField(default=1, help_text='当前用户状态1 是正常 2是禁用', null=True)),
                ('created_at', models.DateTimeField(blank=True, default='2019-01-29 12:13:00', help_text='创建时间', null=True)),
                ('updated_at', models.DateTimeField(help_text='更新时间')),
            ],
            options={
                'db_table': 'admin_user',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('article_id', models.IntegerField(help_text='主键', primary_key=True, serialize=False)),
                ('title', models.CharField(help_text='题目', max_length=200)),
                ('content', models.TextField(default='', help_text='文章内容', null=True)),
                ('uid', models.IntegerField(help_text='添加文章的用户ID')),
                ('visit_num', models.IntegerField(help_text='浏览量')),
                ('created_at', models.DateTimeField(blank=True, default='2019-01-29 12:13:00', help_text='创建时间', null=True)),
                ('updated_at', models.DateTimeField(help_text='更新时间')),
            ],
            options={
                'db_table': 'article',
            },
        ),
    ]
