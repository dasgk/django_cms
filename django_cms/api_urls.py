"""django_cms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django_cms.app.Http.Controller.Api.ArticleController import ArticleController
from django_cms.app.Http.Controller.Api.CateController import CateController
from django_cms.app.Http.Controller.Api.LabelController import LabelController

urlpatterns = [
    url('/article_list', ArticleController.article_list, name='api.article.article_list'),
    url('/article_detail', ArticleController.article_detail, name='api.article.article_detail'),
    url('/cate_list', CateController.cate_list, name='api.cate.cate_list'),
    url('/label_list', LabelController.label_list, name='api.label.label_list'),
    url('/comment_update', ArticleController.comment_update, name='api.comment.comment_update'),
    url('/article_look_num_incr', ArticleController.article_look_num_incr, name='api.article.article_look_num_incr'),
    url('/rate_value_submit', ArticleController.rate_value_submit, name='api.article.rate_value_submit'),
]
