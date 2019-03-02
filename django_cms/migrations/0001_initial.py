# Generated by Django 2.1.5 on 2019-03-02 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminUser',
            fields=[
                ('admin_user_id', models.AutoField(help_text='主键', primary_key=True, serialize=False)),
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
                ('article_id', models.AutoField(help_text='主键', primary_key=True, serialize=False)),
                ('title', models.CharField(default='', help_text='文章标题', max_length=200, null=True)),
                ('content', models.TextField(help_text='文章内容', null=True)),
                ('look_num', models.IntegerField(default=0, help_text='浏览数量', null=True)),
                ('cate_id', models.IntegerField(default=0, help_text='文章类别', null=True)),
                ('status', models.IntegerField(default=1, help_text='1 表示草稿 2表示已经发表', null=True)),
                ('created_at', models.DateTimeField(blank=True, default='2019-01-29 12:13:00', help_text='创建时间', null=True)),
                ('updated_at', models.DateTimeField(default='2019-01-29 12:13:00', help_text='更新时间', null=True)),
            ],
            options={
                'db_table': 'article',
            },
        ),
        migrations.CreateModel(
            name='Cate',
            fields=[
                ('cate_id', models.AutoField(help_text='主键', primary_key=True, serialize=False)),
                ('title', models.CharField(default='', help_text='类别描述', max_length=200, null=True)),
                ('created_at', models.DateTimeField(blank=True, default='2019-01-29 12:13:00', help_text='创建时间', null=True)),
                ('updated_at', models.DateTimeField(default='2019-01-29 12:13:00', help_text='更新时间', null=True)),
            ],
            options={
                'db_table': 'cate',
            },
        ),
    ]
