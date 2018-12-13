from django.conf.urls import url
from django_cms.app.Http.Controller.HomeController import form

urlpatterns = [
    # 表单内容
    url(r'form', form)
]
