from django_cms.models import Cate,Article
from django.core.paginator import Paginator

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
    def getCateList(page_num = 1):
        cate_list = Cate.objects.all()
        p = Paginator(cate_list, 10)  # 3条数据为一页，实例化分页对象
        cate_filter = dict()

        for obj in p.object_list:
            cate_filter['cate_id'] = obj.cate_id
            obj.article_count = Article.objects.filter(** cate_filter).count()
        return p.page(page_num)



