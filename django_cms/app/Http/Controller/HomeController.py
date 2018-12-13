from django.template.loader import get_template
from django.http import HttpResponse

def form(request):
    t = get_template('admin/index.html')
    html = t.render()
    return HttpResponse(html)
