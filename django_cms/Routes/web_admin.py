from django.conf.urls import url
from django_cms.app.Http.Controller.Admin.HomeController import HomeController
from django_cms.app.Http.Controller.Admin.ArticleController import ArticleController
from django.urls import path

# 如果
urlpatterns = [
    # 网页布局
    path(r'', HomeController.index, name='admin.index')
]
