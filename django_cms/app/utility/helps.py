'''
    判断用户是否登陆
'''
from django_cms.models import AdminUser

def is_login(request):
    username = request.session.get("username")
    password = request.session.get("password")
    filters = {}
    filters['username'] = username
    filters['password'] = password
    user = AdminUser.objects.filter(**filters).first()
    if user != None:
        return user
    return False

'''
    植入cookie，设置为登陆状态
'''
from django.http import HttpResponse
def set_login(request, username,password):
    request.session['username'] = username
    request.session['password'] = password