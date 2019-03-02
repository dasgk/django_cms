from django_cms.models import AdminUser
class AdminUserDao:
    @staticmethod
    def getUser(username, password):
        user_filter = {}
        user_filter['username'] = username
        user_filter['password'] = password
        login_admin_user = AdminUser.objects.filter(**user_filter).first()
        return login_admin_user



