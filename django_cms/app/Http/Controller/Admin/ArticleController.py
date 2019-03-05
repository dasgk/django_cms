from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django_cms.models import Article
from django_cms.app.Dao.ArticleDao import ArticleDao

from django_cms.app.Dao.CateDao import CateDao
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class ArticleController(View):
    # 网站首页
    def index(request):
        # 获得所有数据
        param = request.GET
        type_id = param.get('type_id',0)
        title = param.get('title','')
        filter_dict = dict()
        if len(title)>0:
            title = "%"+title+"%"
            filter_dict['title_contains'] = title
        if type_id:
            filter_dict['type_id'] = type_id
        article_list = ArticleDao.getArticleList(filter_dict, param.get('page',1))

        print (cate_list)
        return render(request, 'admin/article/article.html',{'article_list': article_list[1],'total_count':article_list[1],
                                                             'cate_list':cate_list})
    def show_article_form(request):
        cate_list = CateDao.getAllCate()
        return render(request, 'admin/article/article_form.html',
                      {'cate_list': cate_list})



