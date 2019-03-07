from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django_cms.models import Article
from django_cms.app.Dao.ArticleDao import ArticleDao

from django_cms.app.Dao.CateDao import CateDao
from django_cms.app.Dao.LabelDao import LabelDao
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django_cms.app.utility.helps import response_json
from django.urls import reverse

class ArticleController(View):
    '''
        文章列表
    '''

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
        return render(request, 'admin/article/article.html',{'article_list': article_list[0],'total_count':article_list[1]})

    '''
        展示文章的编辑页面
    '''
    def show_article_form(request,article_id):
        cate_list = CateDao.getAllCate()
        article_filter = dict()
        article_filter['article_id'] = article_id
        article = Article.objects.filter(**article_filter).first()
        LabelDao.get_lables_by_artocle_id(article_id)

        return render(request, 'admin/article/article_form.html',
                      {'cate_list': cate_list,'article':article})

    ''' 
        文章信息保存
    '''
    def article_save(request):
        dic = {}
        param = request.POST
        cate_id = param.get('cate_id', 1)
        dic['cate_id'] = cate_id
        dic['content'] = param.get('content')
        dic['title'] = param.get('title')
        # 暂时不处理
        tagsinput = param.get('tagsinput')
        article = Article.objects.create(**dic)
        LabelDao.update_lable_article(tagsinput, article.article_id)
        return response_json(1, [], "保存成功", reverse('admin.article.index'))

    def article_delete(request, article_id):
        cate_filter = dict()
        cate_filter['article_id'] = article_id
        article = Article.objects.filter(**cate_filter).first()
        article.delete()
        return response_json(1, [], "删除成功", reverse('admin.article.index'))

