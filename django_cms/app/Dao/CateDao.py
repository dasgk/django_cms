from django_cms.models import Cate,Article
from django.core.paginator import Paginator
from django_cms.app.Dao.ConstDao import ConstDao
class CateDao:
    @staticmethod
    def createOrUpdate(cate_id, title):
        filter_dict = dict()
        filter_dict['cate_id'] = cate_id
        cate = Cate.objects.filter(**filter_dict).first()
        if cate:
            cate.title = title
        else:
            cate = Cate()
            cate.title = title
            cate.save()
        return cate

    @staticmethod
    def getCateList(page_num):
        cate_list = Cate.objects.order_by("cate_id").all()
        page = Paginator(cate_list, ConstDao.getPageNum())
        cate_filter = dict()
        for obj in page.object_list:
            cate_filter['cate_id'] = obj.cate_id
            obj.article_count = Article.objects.filter(** cate_filter).count()
        return [page, page.page(page_num)]



