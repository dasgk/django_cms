from django.template.loader import get_template
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View

from django.shortcuts import render_to_response,render,redirect
from django.template import RequestContext
from django_cms.models import AdminUser
from django.views.generic import TemplateView
from django_cms.app.utility.helps import set_login,is_login
class UserController(TemplateView):
    # 网站首页

    def login(request):

        if request.method == 'GET':
            admin_user = is_login(request)
            if admin_user != False:
                return HttpResponseRedirect('/')
                return render(request, 'admin/index.html',)
            else:
                return render(request, 'admin/login.html')
        else:
            parm = request.POST
            username = parm.get('username', 'not found')
            password = parm.get('password', 'not found')
            user_filter = {}
            user_filter['username'] = username
            user_filter['password'] = password
            login_admin_user = AdminUser.objects.filter(**user_filter).first()
            if login_admin_user != None:
                set_login(request, username, password)
                return HttpResponseRedirect('')
            else:
                return HttpResponse('error')




