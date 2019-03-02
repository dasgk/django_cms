from django_cms.models import Cate
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
        Cate.objects


