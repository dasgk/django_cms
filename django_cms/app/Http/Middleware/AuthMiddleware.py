from django.shortcuts import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin


# 用户认证判断，这里需要的比较多，不需要的少，使用白名单
class AuthMiddleWare(MiddlewareMixin):

    def process_request(self, request):
        if request.path == '/user/login' or request.path == 'user/register':
            return None
        ticket = request.COOKIES.get('ticket')
        if not ticket:
            return HttpResponseRedirect('/user/login')
        return None
