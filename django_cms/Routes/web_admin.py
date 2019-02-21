from django.conf.urls import url
from django_cms.app.Http.Controller.Admin.HomeController import HomeController
from django_cms.app.Http.Controller.Admin.UserController import UserController

# 如果
urlpatterns = [
    url(r'user/login', UserController.login, name='admin.user.login'),
    url(r'index', HomeController.index, name='admin.index')
]
