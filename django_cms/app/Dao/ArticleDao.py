from django_cms.app.Dao.ConstDao import ConstDao
from django_cms.models import Article, LabelArticle


class ArticleDao(object):
    @staticmethod
    def getArticleList(options, page_num, label_id):
        if label_id:
            label_filter = dict()
            label_filter['label_id'] = label_id
            article_ids = LabelArticle.objects.filter(**label_filter).values_list('article_id', flat=True)
            if article_ids:
                options['article_id__in'] = article_ids
            else:
                return [[], 0];
        skip = (int(page_num) - 1) * ConstDao.getPageNum()
        article_list = Article.objects.filter(**options).order_by("article_id").all()[skip:skip + ConstDao.getPageNum()]
        article_count = Article.objects.filter(**options).count()
        return [article_list, article_count]

    @staticmethod
    def createOrUpdate(article_id, title, content, cate_id):
        if type(article_id) != int and len(article_id) == 0:
            article_id = 0
        article = None
        if article_id > 0:
            article_filter = dict()
            article_filter['article_id'] = article_id
            article = Article.objects.filter(**article_filter).first()

        if article == None:
            article = Article()
            article.title = title
            article.content = content
            article.cate_id = cate_id
            article.save()
        else:
            article.title = title
            article.content = content
            article.cate_id = cate_id
            article.save()
        return article
