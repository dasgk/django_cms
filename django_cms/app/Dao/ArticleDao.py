from django_cms.app.Dao.ConstDao import ConstDao
from django_cms.app.Dao.TimeDao import TimeDao
from django_cms.models import Article, LabelArticle,Label
import time
import logging

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
        if not article_id:
            article_id = 0
        else:
            article_id = int(article_id)
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
            article.created_at = TimeDao.get_current_time()
            article.updated_at = TimeDao.get_current_time()
            article.save()
        else:
            article.title = title
            article.content = content
            article.cate_id = cate_id
            article.updated_at = TimeDao.get_current_time()
            article.save()
        return article

    @staticmethod
    def deleteArticle(article_id):
        logger = logging.getLogger('scripts')
        #删除文章
        Article.objects.filter(article_id=article_id).delete()
        #删除当前文章的关联关系
        label_ids = LabelArticle.objects.filter(article_id=article_id).values_list('label_id', flat=True)
        for label_id in label_ids:
            logger.info(label_id)
        LabelArticle.objects.filter(article_id=article_id).delete()
        for label_id in label_ids:
            label_count = LabelArticle.objects.filter(label_id=label_id).count()
            logger.info(label_id)
            if not label_count:
                Label.objects.filter(label_id=label_id).delete()
