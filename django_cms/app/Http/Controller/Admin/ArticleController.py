from django.template.loader import get_template
from django.http import HttpResponse
from django.views import View
from django_cms.models import Article
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class ArticleController(View):
    # 网站首页
    def index(request):
        # 获得所有数据
        article_list = Article.objects.all()
        # 进行分页操作
        p = Paginator(article_list, 3)
        page = request.GET.get('page')
        if page is None:
            page = 1
        try:
            article_list = p.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            article_list = p.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            article_list = p.page(1)
        context = {'article_list': article_list,'user_name':request.user.username}
        t = get_template('admin/article.html')
        html = t.render(context)
        return HttpResponse(html)

