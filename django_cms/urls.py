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
from django_cms.app.Http.Controller.Admin.HomeController import HomeController
from django_cms.app.Http.Controller.Admin.UserController import UserController
from django_cms.app.Http.Controller.Admin.ArticleController import ArticleController
from django_cms.app.Http.Controller.Admin.CateController import CateController

urlpatterns = [
    url('user/login', UserController.login, name='admin.user.login'),
    url('user/logout', UserController.logout, name='admin.user.logout'),
    url('index', HomeController.index, name='admin.index'),
    url('article_list', ArticleController.index, name='admin.article.index'),
    url('show_article_form', ArticleController.show_article_form, name='admin.article.show_article_form'),
    url('cate_list', CateController.index, name='admin.cate.index'),
    url('show_cate_form', CateController.show_cate_form, name='admin.cate.show_cate_form'),
    url('', HomeController.index, name='admin.index'),
]
