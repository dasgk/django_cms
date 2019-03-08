from django.views import View
from django.shortcuts import render
from django_cms.app.Dao.LabelDao import LabelDao
from django_cms.models import LabelArticle

import logging


class LabelController(View):
    # 标签列表
    def index(request):
        # 获得所有数据
        param = request.GET
        res = LabelDao.get_label_list(param.get('page',1))
        label_list = res[0]
        total_count = res[1]
        for label in label_list:
            label_filter = dict()
            label_filter['label_id'] = label.label_id
            label.article_count = LabelArticle.objects.filter(**label_filter).count()
        return render(request, 'admin/label/label.html', {'label_list': label_list,'total_count':total_count})