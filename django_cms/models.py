from django.db import models

class AdminUser(models.Model):
    admin_user_id = models.AutoField(primary_key=True, help_text="主键")
    username = models.CharField(max_length=200, help_text="管理员的用户名")
    password = models.CharField(max_length=200, help_text="管理员的密码")
    api_token = models.CharField(max_length=200, help_text="文章内容")
    status = models.IntegerField(help_text="当前用户状态1 是正常 2是禁用", default=1, null=True)
    created_at = models.DateTimeField(help_text="创建时间", null=True, default="2019-01-29 12:13:00", blank=True)
    updated_at = models.DateTimeField(help_text="更新时间")

    class Meta:
        db_table = "admin_user"


class Article(models.Model):
    article_id = models.AutoField(primary_key=True, help_text="主键")
    title = models.CharField(max_length=200, help_text="文章标题", null=True, default="")
    content = models.TextField(help_text="文章内容", null=True)
    look_num = models.IntegerField(help_text="浏览数量", default=0, null=True)
    like_num = models.IntegerField(help_text="点赞数量", default=0, null=True)
    comment_num = models.IntegerField(help_text="评论数量", default=0, null=True)
    cate_id = models.IntegerField(help_text="文章类别", default=0, null=True)
    status = models.IntegerField(help_text="1 表示草稿 2表示已经发表", default=1, null=True)
    created_at = models.CharField(help_text="创建时间", null=True, default="", max_length=20, blank=True)
    updated_at = models.CharField(help_text="更新时间", null=True, default="", max_length=20)

    class Meta:
        db_table = "article"


class Cate(models.Model):
    cate_id = models.AutoField(primary_key=True, help_text="主键")
    title = models.CharField(max_length=200, help_text="类别描述", null=True, default="")
    picture = models.CharField(max_length=200, help_text="类别图片", null=True, default="")
    created_at = models.DateTimeField(help_text="创建时间", null=True, default="2019-01-29 12:13:00", blank=True)
    updated_at = models.DateTimeField(help_text="更新时间", null=True, default="2019-01-29 12:13:00")

    class Meta:
        db_table = "cate"

class Label(models.Model):
    label_id = models.AutoField(primary_key=True, help_text="主键")
    title = models.CharField(max_length=200, help_text="类别描述", null=True, default="")
    created_at = models.DateTimeField(help_text="创建时间", null=True, default="2019-01-29 12:13:00", blank=True)
    updated_at = models.DateTimeField(help_text="更新时间", null=True, default="2019-01-29 12:13:00")

    class Meta:
        db_table = "label"


class LabelArticle(models.Model):
    label_article_id = models.AutoField(primary_key=True, help_text="主键")
    label_id = models.IntegerField( help_text="标签id", null=True, default=0)
    article_id = models.IntegerField(help_text="文章id", null=True, default=0)
    created_at = models.DateTimeField(help_text="创建时间", null=True, default="2019-01-29 12:13:00", blank=True)
    updated_at = models.DateTimeField(help_text="更新时间", null=True, default="2019-01-29 12:13:00")
    class Meta:
        db_table = "label_article"

class ArticleComment(models.Model):
    article_comment_id = models.AutoField(primary_key=True,help_text="主键")
    article_id = models.IntegerField(help_text="文章id", default=0)
    status = models.IntegerField(help_text="状态0表示草稿 1表示已经审核通过", default=0)
    comment = models.CharField(max_length=200, default="")
    remote_addr = models.CharField(max_length=30,help_text="远程ip")
    locate_area = models.CharField(max_length=20, help_text="所在区域")
    created_at = models.DateTimeField(help_text="创建时间", null=True, default="2019-01-29 12:13:00", blank=True)
    class Meta:
        db_table = "article_comment"

