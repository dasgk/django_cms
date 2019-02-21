from django.template.loader import get_template
from django.http import HttpResponse
from django.views import View


class UserController(View):
    # 网站首页
    def login(request):
        context = {}
        t = get_template('admin/login.html')
        html = t.render(context)
        return HttpResponse(html)
