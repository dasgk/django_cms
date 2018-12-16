from django.template.loader import get_template
from django.http import HttpResponse
from django_cms.app.Dao.MenuDao import MenuDao
from django.template import Context

def form(request):
    menu_list = MenuDao.getMenuListByUser()
    context = {'menu_list': menu_list}
    t = get_template('admin/index.html')
    html = t.render(context)
    return HttpResponse(html)
