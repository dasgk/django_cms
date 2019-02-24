from django.template.loader import get_template
from django.http import HttpResponse
from django.views import View

from django.shortcuts import render_to_response,render
from django.template import RequestContext
from django_cms.models import AdminUser
from django.views.generic import TemplateView
class UserController(TemplateView):
    # 网站首页

    def login(request):
        if request.method == 'GET':
            return render(request, 'admin/login.html', {'article_list': []})
        else:
            parm = request.POST
            username = parm.get('username', 'not found')
            password = parm.get('password', 'not found')
            user_filter = {}
            user_filter['username'] = username
            user_filter['password'] = password
            login_admin_user = AdminUser.objects.filter(**user_filter).first()
            if login_admin_user:
                return render(request, 'admin/index.html', {'user':login_admin_user})
            print(login_admin_user)



