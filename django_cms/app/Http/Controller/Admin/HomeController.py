from django.template.loader import get_template
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django_cms.app.Dao.MenuDao import MenuDao
from django.views import View
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django_cms.app.utility.helps import is_login

class HomeController(View):
    # 网站首页
    def index(request):
        return HttpResponse(11111)
        admin_user = is_login(request)

        if admin_user!= False:
            t = get_template('admin/index.html')
            html = t.render({})
            return HttpResponse(html)
        else:
            return HttpResponseRedirect('/user/login')

