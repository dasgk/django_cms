from django_cms.app.Dao.ConstDao import ConstDao
from django_cms.app.Dao.TimeDao import TimeDao
from django_cms.models import Article, LabelArticle,Label,ArticleComment
import random
import logging
import datetime

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
                return [[], 0]
        skip = (int(page_num) - 1) * ConstDao.getPageNum()
        article_list = Article.objects.filter(**options).order_by("-article_id").all()[skip:skip + ConstDao.getPageNum()]
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

    @staticmethod
    def getArticleDetail(article_id):
        article = Article.objects.filter(article_id=article_id).first()
        if article is None:
            return []
        article_info = {}
        article_info['title'] = article.title
        article_info['content'] = article.content
        article_info['updated_at'] = article.updated_at
        article_info['rate_num'] = article.rate_num

        if isinstance(article.updated_at, datetime.datetime):
            article_info['updated_at'] = article.updated_at.strftime('%Y-%m-%d %H:%M:%S')
        else:
            article_info['updated_at'] = article.updated_at
        article_info['comments'] = []
        comments = ArticleComment.objects.filter(article_id=article_id).filter(status=0)
        for comment in comments:
            item = {}
            item['content'] = comment.comment
            item['ip_address'] = comment.remote_addr
            created_at = comment.created_at
            if isinstance(created_at, datetime.datetime):
                created_at = created_at.strftime('%Y-%m-%d %H:%M:%S')
            item['time'] = created_at
            item['random_avatar'] = "http://127.0.0.1:8000/static/avatar/"+str(random.randint(1,6))+".jpg"
            article_info['comments'].append(item)
        article_info['comment_num'] = len(article_info['comments'])
        return article_info

