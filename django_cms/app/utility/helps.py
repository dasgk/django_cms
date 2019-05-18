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



'''
 获得文件完整得到url 
'''


def get_file_url(request,path):
    if len(path) ==0:
        return ""
    if path[0] == '/':
        return "http://"+request.get_host()+path
    return "http://" + request.get_host() + "/" + path

'''
    获得ip地址
'''
def get_client_ip(request):
    ip = ""
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        if 'REMOTE_ADDR' in request.META and len(str(request.META['REMOTE_ADDR'])) > 0:
            ip = request.META['REMOTE_ADDR']
        else:
            ip = '未知用户'
    return ip