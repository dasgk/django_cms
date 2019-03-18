from django_cms.models import Cate,Article,Label,LabelArticle
from django.core.paginator import Paginator
from django_cms.app.Dao.ConstDao import ConstDao
from django_cms.app.Dao.TimeDao import TimeDao
import logging
class LabelDao(object):
    @staticmethod
    def update_label(tagsinput, article_id):
        labels = tagsinput.split(',')
        for label in labels:
            tag_filter = dict()
            tag_filter['title'] = label
            tag_model = Label.objects.filter(**tag_filter).first()
            if tag_model == None:
                tag_model = Label.objects.create(title=label,created_at = TimeDao.get_current_time(), updated_at=TimeDao.get_current_time())

            label_article = LabelArticle()
            label_article.label_id = tag_model.label_id
            label_article.article_id = article_id
            label_article.created_at = TimeDao.get_current_time()
            label_article.updated_at = TimeDao.get_current_time()

            label_article.save()


    @staticmethod
    def update_lable_article(labels, article_id):
        # 处理当前文章所关联的标签
        condition = {}
        condition['article_id'] = article_id
        relatives = LabelArticle.objects.filter(**condition).all()

        for relative in relatives:
            # 如果标签只关联了当前文章，则删除关联关系，并删除标签
            label_id = relative.label_id
            label_condition = {}
            label_condition['label_id'] = label_id
            label_count = Label.objects.filter(**label_condition).count()
            if label_count == 1:
                #删除该标签
                Label.objects.filter(**label_condition).delete()
            relative.delete()

        # 增加关联关系，如果标签不存在，则新建标签
        LabelDao.update_label(labels, article_id)

    @staticmethod
    def get_lables_by_article_id(article_id):
        label_article = {}
        label_article['article_id'] = article_id
        lable_ids = LabelArticle.objects.filter(**label_article).values_list('label_id',flat=True)
        titles = Label.objects.filter(label_id__in=lable_ids).values_list('title', flat=True)
        char = ','
        return char.join(titles)

    @staticmethod
    def get_label_list(page_num):
        skip = (int(page_num) - 1) * ConstDao.getPageNum()
        label_list = Label.objects.order_by("-label_id").all()[skip:skip + ConstDao.getPageNum()]
        label_count = Label.objects.count()
        return [label_list, label_count]

    def get_all_label():
        label_list = Label.objects.order_by("-label_id").all()
        return label_list
