from django.conf.urls import url
from django_cms.app.Http.Controller.Admin.HomeController import HomeController
from django_cms.app.Http.Controller.Admin.ArticleController import ArticleController
from django.urls import path

# 如果
urlpatterns = [
    # 网页布局
    path(r'', HomeController.jump2index),
    path(r'index', HomeController.index, name='admin.index'),
    # 欢迎页面，也是一个展示页面
    url('welcome', HomeController.welcome, name='admin.welcome'),
    # 用户登出
    url('logout', HomeController.logout, name='admin.logout'),

    # 文章列表
    url('article', ArticleController.index, name='admin.article.index'),
]
