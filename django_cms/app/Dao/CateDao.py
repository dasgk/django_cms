from django_cms.models import Cate,Article
from django.core.paginator import Paginator
from django_cms.app.Dao.ConstDao import ConstDao
from django_cms.app.Dao.TimeDao import TimeDao
import logging
import time

class CateDao(object):
    @staticmethod
    def createOrUpdate(cate_id, title,picture):
        filter_dict = dict()
        filter_dict['cate_id'] = cate_id
        cate = Cate.objects.filter(**filter_dict).first()
        if cate:
            cate.title = title
            cate.picture = picture
            cate.updated_at = TimeDao.get_current_time()
        else:
            cate = Cate()
            cate.title = title
            cate.picture = picture
            cate.updated_at = TimeDao.get_current_time()
            cate.created_at = TimeDao.get_current_time()
        cate.save()
        return cate

    @staticmethod
    def getCateList(page_num):
        skip = (int(page_num)-1)*ConstDao.getPageNum()
        cate_list = Cate.objects.order_by("cate_id").all()[skip:skip+ConstDao.getPageNum()]
        cate_count = Cate.objects.count()
        cate_filter = dict()
        for obj in cate_list:
            cate_filter['cate_id'] = obj.cate_id
            obj.article_count = Article.objects.filter(** cate_filter).count()
        return [cate_list, cate_count]

    @staticmethod
    def getAllCate():
        cate_list = Cate.objects.order_by("cate_id").all()
        return cate_list


