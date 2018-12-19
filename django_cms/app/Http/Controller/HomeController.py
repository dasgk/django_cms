from django.template.loader import get_template
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django_cms.app.Dao.MenuDao import MenuDao
from django.template import Context
from django.views import View



class HomeController(View):
    # 网站首页
    def index(request):
        menu_list = MenuDao.getMenuListByUser()
        context = {'menu_list': menu_list}
        t = get_template('admin/index.html')
        html = t.render(context)
        return HttpResponse(html)


    # 跳转到登录页面
    def jump2login(request):
        return HttpResponseRedirect('admin/login')


    # 欢迎致辞
    def welcome(request):
        t = get_template('admin/welcome.html')
        html = t.render()
        return HttpResponse(html)
