from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django_cms.models import Article
from django_cms.app.Dao.ArticleDao import ArticleDao

from django_cms.app.Dao.CateDao import CateDao
from django_cms.app.Dao.LabelDao import LabelDao
from django_cms.app.utility.helps import response_json
from django.urls import reverse
from django.template.context_processors import csrf

class FileController(View):
    def show_file_upload(request):
        return render(request, 'admin/files/upload_resource_html.html', csrf(request))

    def file_upload(request):
        if request.method == "POST":  # 请求方法为POST时，进行处理
            myFile = request.FILES.get("myfile", None)  # 获取上传的文件，如果没有文件，则默认为None
            if not myFile:
                return HttpResponse("no files for upload!")
            destination = open(os.path.join("E:\\upload", myFile.name), 'wb+')  # 打开特定的文件进行二进制的写操作
            for chunk in myFile.chunks():  # 分块写入文件
                destination.write(chunk)
            destination.close()
            return HttpResponse("upload over!")
        return


