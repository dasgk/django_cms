from django.template.loader import get_template
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from django_cms.app.Dao.CateDao import CateDao
from django_cms.models import Cate

from django_cms.app.utility.helps import response_json


class CateController(View):
    # 文章类别列表
    def index(request):
        # 获得所有数据
        t = get_template('admin/cate/cate.html')
        html = t.render({'cate_list': []})
        return HttpResponse(html)

    def show_cate_form(request):
        return render(request, 'admin/cate/cate_form.html', {})

    def save_cate(request):
        parm = request.POST
        cate_id = parm.get('cate_id', 0)
        title = parm.get('title', '')
        cate = CateDao.createOrUpdate(cate_id, title)
        if type(cate) == Cate:
            return response_json(1,[], "保存成功")
        else:
            return response_json(0, "")

    def delete_cate(request):
        t = get_template('admin/cate/cate_form.html')
        html = t.render({})
        return HttpResponse(html)
