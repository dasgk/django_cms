from django.db import models


class Article(models.Model):
    article_id = models.IntegerField(primary_key=True, help_text="主键")

    title = models.CharField(max_length=200, help_text="题目")
    content = models.TextField(help_text="文章内容", null=True,default="")
    uid = models.IntegerField(help_text="添加文章的用户ID")
    visit_num = models.IntegerField(help_text="浏览量")
    created_at = models.DateTimeField(help_text="创建时间", null=True, default="2019-01-29 12:13:00",blank=True)
    updated_at = models.DateTimeField(help_text="更新时间")

    class Meta:
        db_table = "article"
