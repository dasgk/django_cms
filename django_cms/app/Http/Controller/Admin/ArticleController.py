from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django_cms.models import Article
from django_cms.app.Dao.ArticleDao import ArticleDao

from django_cms.app.Dao.CateDao import CateDao
from django_cms.app.Dao.LabelDao import LabelDao
from django_cms.app.utility.helps import response_json
from django.urls import reverse

class ArticleController(View):
    '''
        文章列表
    '''

    def index(request):
        # 获得所有数据
        param = request.GET
        cate_id = param.get('cate_id',0)
        title = param.get('title','')
        label_id = param.get('label_id',0)
        filter_dict = dict()
        if len(title)>0:
            title = "%"+title+"%"
            filter_dict['title_contains'] = title
        if cate_id:
            filter_dict['cate_id'] = cate_id
        article_list = ArticleDao.getArticleList(filter_dict, param.get('page',1), label_id=label_id)
        return render(request, 'admin/article/article.html',{'article_list': article_list[0],'total_count':article_list[1]})

    '''
        展示文章的编辑页面
    '''
    def show_article_form(request,article_id):
        cate_list = CateDao.getAllCate()
        article_filter = dict()
        article_filter['article_id'] = article_id
        article = Article.objects.filter(**article_filter).first()
        labels = LabelDao.get_lables_by_article_id(article_id)
        return render(request, 'admin/article/article_form.html',
                      {'cate_list': cate_list,'article':article,'labels':labels})

    ''' 
        文章信息保存
    '''
    def article_save(request):
        param = request.POST
        article = ArticleDao.createOrUpdate(article_id=param.get('article_id',0),cate_id=param.get('cate_id',1),title=param.get('title'), content=param.get('content',''))
        tagsinput = param.get('tagsinput')
        LabelDao.update_lable_article(tagsinput, article.article_id)
        return response_json(1, [], "保存成功", reverse('admin.article.index'))

    def article_delete(request, article_id):
        cate_filter = dict()
        cate_filter['article_id'] = article_id
        article = Article.objects.filter(**cate_filter).first()
        article.delete()
        return response_json(1, [], "删除成功", reverse('admin.article.index'))

