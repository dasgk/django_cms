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


def set_login(request, username, password):
    request.session['username'] = username
    request.session['password'] = password


def do_logout(request):
    request.session['username'] = ''
    request.session['password'] = ''


from django.http import HttpResponse
import json

'''
    返回json数据
'''


def response_json(statusCode, data, msg='', url=''):
    res = {}
    res['status'] = statusCode
    res['data'] = data
    res['msg'] = msg
    res['url'] = url
    return HttpResponse(json.dumps(res, ensure_ascii=False), content_type="application/json,charset=utf-8")


