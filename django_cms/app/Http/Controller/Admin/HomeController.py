from django.template.loader import get_template
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import View
from django_cms.app.utility.helps import is_login

class HomeController(View):
    # 网站首页
    def index(request):
        admin_user = is_login(request)
        if admin_user != False:
            t = get_template('admin/index.html')
            html = t.render({'user':admin_user})
            return HttpResponse(html)
        else:
            return HttpResponseRedirect('/user/login')
