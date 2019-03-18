from django_cms.models import Label,LabelArticle
from django_cms.app.Dao.LabelDao import LabelDao
from django_cms.app.utility.helps import response_json
class LabelController:
    def label_list(request):
        label_list = LabelDao.get_all_label()
        res = []
        for label in label_list:
            item = {}
            item['label_id'] = label.label_id
            item['title'] = label.title
            item['article_count'] = LabelArticle.objects.filter(label_id=label.label_id).count()
            res.append(item)
        return response_json(1,res)
