from django.template.loader import get_template
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from django_cms.app.Dao.CateDao import CateDao
from django_cms.models import Cate,Article
from django.urls import reverse
from django_cms.app.utility.helps import response_json


import logging


class CateController(View):
    # 文章类别列表
    def index(request):
        # 获得所有数据
        page_num = request.GET.get('page',1)
        cate_list = CateDao.getCateList(page_num)
        return render(request, 'admin/cate/cate.html', {'cate_list': cate_list[0],'total_count':cate_list[1]})


    def show_cate_form(request,cate_id):
        cate_filter = dict()
        cate_filter['cate_id'] = cate_id
        cate = Cate.objects.filter(**cate_filter).first()
        return render(request, 'admin/cate/cate_form.html', {'cate':cate})

    def save_cate(request):
        parm = request.POST
        cate_id = parm.get('cate_id', 0)
        title = parm.get('title', '')
        cate = CateDao.createOrUpdate(cate_id, title)
        if type(cate) == Cate:
            return response_json(1, [], "保存成功", reverse('admin.cate.index'))
        else:
            return response_json(0, "")

    def delete_cate(request, cate_id):
        cate_filter = dict()
        cate_filter['cate_id'] = cate_id
        count = Article.objects.filter(**cate_filter).count()
        if count>0:
            return response_json(0, [], "该类别下有文章，不允许删除")
        cate = Cate.objects.filter(**cate_filter).first()
        cate.delete()
        return response_json(1, [], "删除成功", reverse('admin.cate.index'))