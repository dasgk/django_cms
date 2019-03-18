from django_cms.models import Article
from django_cms.app.Dao.ArticleDao import ArticleDao
from django_cms.app.utility.helps import response_json
from datetime import datetime
class ArticleController:
    def article_list(request):
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
        article_list = article_list[0]
        res = []
        for article in article_list:
            item = {}
            item['article_id'] = article.article_id
            item['title'] = article.title
            item['content'] = article.content[0:138]
            item['look_num'] = article.look_num
            if type(article.updated_at) == datetime:
                item['updated_at'] = article.updated_at.strftime('%Y-%m-%d %H:%M:%S')
            else:
                item['updated_at'] = article.updated_at
            res.append(item)
        return response_json(1,res)
