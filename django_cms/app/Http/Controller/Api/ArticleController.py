from django_cms.models import Article,ArticleComment,Cate
from django_cms.app.Dao.ArticleDao import ArticleDao
from django_cms.app.utility.helps import response_json
from datetime import datetime
from django_cms.app.utility.helps import get_file_url
class ArticleController:
    def article_list(request):
        # 获得所有数据
        param = request.GET
        cate_id = param.get('cate_id',0)
        title = param.get('title','')
        label_id = param.get('label_id',0)
        filter_dict = dict()
        if len(title)>0:
            filter_dict['title__icontains'] = title
        if cate_id:
            filter_dict['cate_id'] = cate_id
        article_list = ArticleDao.getArticleList(filter_dict, param.get('page',1), label_id=label_id)
        article_list = article_list[0]
        res = []
        for article in article_list:
            item = {}
            item['article_id'] = article.article_id
            item['title'] = article.title
            item['content'] = article.content[0:138]
            item['look_num'] = article.look_num
            item['like_num'] = article.like_num
            item['comment_num'] = article.comment_num
            item['cate_id'] = article.cate_id
            cate = Cate.objects.filter(cate_id=article.cate_id).first()
            if cate:
                item['cate_url'] = get_file_url(request,cate.picture)
                item['cate_title'] = cate.title
            else:
                item['cate_url'] = ''
                item['cate_title'] = ''
            if type(article.updated_at) == datetime:
                item['updated_at'] = article.updated_at.strftime('%Y-%m-%d %H:%M:%S')
            else:
                item['updated_at'] = article.updated_at
            res.append(item)
        return response_json(1,res)

    def article_detail(request):
        article_id = request.GET.get('article_id',0)
        article_info = ArticleDao.getArticleDetail(article_id)
        return response_json(1, article_info)

    def comment_update(request):
        param = request.GET
        article_id = param.get('article_id', 0)
        comments = param.get('comment', "")
        article_comment = ArticleComment()
        article_comment.article_id = article_id;
        article_comment.comment = comments;
        ip = ""
        if 'HTTP_X_FORWARDED_FOR' in request.META:
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            if 'REMOTE_ADDR' in request.META and len(str(request.META['REMOTE_ADDR']))>0:
                ip = request.META['REMOTE_ADDR']
            else:
                ip = '未知用户'
        article_comment.remote_addr = ip
        article_comment.locate_area = "中国"
        article_comment.save()
        return response_json(1,[])

    def article_look_num_incr(request):
        param = request.GET
        article_id = param.get('article_id')
        article = Article.objects.filter(article_id=article_id).first()
        if article is None:
            return response_json(0,[],'参数有误')
        article.look_num = article.look_num+1
        article.save()
        return response_json(1, [], '操作成功')