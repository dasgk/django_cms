from django.conf.urls import url
from django_cms.app.Http.Controller.HomeController import HomeController

#如果
urlpatterns = [
    # 网页布局
    url(r'index', HomeController.index),
    # 欢迎页面，也是一个展示页面
    url('welcome', HomeController.welcome,name='admin.welcome'),
    #用户登出
    url('logout', HomeController.logout,name='admin.logout'),
]
