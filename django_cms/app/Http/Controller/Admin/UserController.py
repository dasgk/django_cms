from django.template.loader import get_template
from django.http import HttpResponse
from django.views import View

from django.shortcuts import render_to_response,render
from django.template import RequestContext

from django.views.generic import TemplateView
class UserController(TemplateView):
    # 网站首页

    def login(request):
        if request.method == 'GET':
            return render(request, 'admin/login.html', {'article_list': []})
        else:
            return render(request, 'admin/index.html', {'article_list': []})
            parm = request.POST
            new_user = UserInfo()
            new_user.user_name = parm.get('user_name', 'not found')
            new_user.password = parm.get('pwd', 'not found')
            new_user.email = parm.get('email', 'not found')


