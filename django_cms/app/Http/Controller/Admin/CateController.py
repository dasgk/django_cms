from django.template.loader import get_template
from django.http import HttpResponse
from django.views import View
from django_cms.models import Article
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class CateController(View):
    # 文章类别列表
    def index(request):
        # 获得所有数据
        t = get_template('admin/cate/cate.html')
        html = t.render({'cate_list':[]})
        return HttpResponse(html)

    def show_cate_form(request):
        t = get_template('admin/cate/cate_form.html')
        html = t.render({})
        return HttpResponse(html)

    def save_cate(request):
        t = get_template('admin/cate/cate_form.html')
        html = t.render({})
        return HttpResponse(html)

    def delete_cate(request):
        t = get_template('admin/cate/cate_form.html')
        html = t.render({})
        return HttpResponse(html)


