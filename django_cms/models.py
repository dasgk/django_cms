from django.db import models

class AdminUser(models.Model):
    admin_user_id = models.IntegerField(primary_key=True, help_text="主键")
    username = models.CharField(max_length=200, help_text="管理员的用户名")
    password = models.CharField(max_length=200, help_text="管理员的密码")
    api_token = models.CharField(max_length=200,help_text="文章内容")
    status = models.IntegerField(help_text="当前用户状态1 是正常 2是禁用",default=1,null=True)
    created_at = models.DateTimeField(help_text="创建时间", null=True, default="2019-01-29 12:13:00",blank=True)
    updated_at = models.DateTimeField(help_text="更新时间")

    class Meta:
        db_table = "admin_user"