from django.template.loader import get_template
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import View
from django_cms.app.utility.helps import is_login
from django_cms.models import  Article,Label,Cate

class HomeController(View):
    # 网站首页
    def index(request):
        admin_user = is_login(request)
        if admin_user != False:
            t = get_template('admin/index.html')
            cate_count = Cate.objects.count()
            label_count = Label.objects.count()
            html = t.render({'user':admin_user,'cate_count':cate_count,'label_count':label_count})
            return HttpResponse(html)
        else:
            return HttpResponseRedirect('admin/user/login')

    def jump2Index(request):
        return HttpResponseRedirect('admin/index')
