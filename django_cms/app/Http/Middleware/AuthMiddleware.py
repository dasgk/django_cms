from django.shortcuts import HttpResponseRedirect
import re
from django.utils.deprecation import MiddlewareMixin


# 用户认证判断，这里需要的比较多，不需要的少，使用白名单
class AuthMiddleWare(MiddlewareMixin):

    def process_request(self, request):
        return
        url_path = request.path
        exclued_path = ['/admin/login/']
        for each in exclued_path:
            print(each)
            print(url_path)
            if re.match(each, url_path):
                return
        if request.user.is_authenticated:
            # 不在白名单里的，用户未登录的跳转到登录界面
            return HttpResponseRedirect('/admin/login/')
        else:
            return
