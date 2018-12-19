from django.template.loader import get_template
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django_cms.app.Dao.MenuDao import MenuDao
from django.views import View
from django.contrib import auth
from django.contrib.auth.decorators import login_required

class HomeController(View):
    # 网站首页
    def index(request):
        menu_list = MenuDao.getMenuListByUser()
        context = {'menu_list': menu_list}
        t = get_template('admin/index.html')
        html = t.render(context)
        #return HttpResponse(html)


    # 欢迎致辞
    def welcome(request):
        t = get_template('admin/welcome.html')
        html = t.render()
        return HttpResponse(html)

    def logout( request):
        auth.logout(request)
        return HttpResponseRedirect("/admin/login/")
