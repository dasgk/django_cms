from django_cms.models import Cate,Article
from django_cms.app.Dao.CateDao import CateDao
from django_cms.app.utility.helps import response_json,get_file_url
from django.db.models import Sum
class CateController:
    def cate_list(request):
        cate_list = CateDao.getAllCate()
        res = []
        for cate in cate_list:
            item = {}
            item['cate_id'] = cate.cate_id
            item['title'] = cate.title
            item['cate_img_url'] = get_file_url(request,cate.picture)
            item['article_count'] = Article.objects.filter(cate_id=cate.cate_id).count()
            item['look_num'] = Article.objects.filter(cate_id=cate.cate_id).aggregate(Sum('look_num')).get('look_num__sum')

            res.append(item)
        return response_json(1,res)
