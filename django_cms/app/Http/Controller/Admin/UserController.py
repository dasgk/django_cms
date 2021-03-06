from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django_cms.app.Dao.UserDao import AdminUserDao
from django_cms.models import AdminUser
from django.views.generic import TemplateView
from django_cms.app.utility.helps import set_login, is_login, do_logout, response_json


class UserController(TemplateView):

    '''
        用户登录操作，GET请求显示登录页面，判断已登录，跳转到首页
                     POST请求，判断输入用户名密码是否正确
    '''
    def login(request):
        if request.method == 'GET':
            admin_user = is_login(request)
            if admin_user != False:
                return HttpResponseRedirect('admin/index')
            else:
                return render(request, 'admin/login.html')
        else:
            parm = request.POST
            username = parm.get('username', 'not found')
            password = parm.get('password', 'not found')
            login_admin_user = AdminUserDao.getUser(username, password)
            if type(login_admin_user) == AdminUser:
                set_login(request, username, password)
                return HttpResponseRedirect('admin/index')
            else:
                return HttpResponse('error')
    '''
        用户登出操作，删除session的值
    '''
    def logout(request):
        do_logout(request)
        return response_json(1, "")
