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
        context = {'menu_list': menu_list, 'user_name': request.user.username}
        t = get_template('admin/1index.html')
        html = t.render(context)
        return HttpResponse(html)