from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django_cms.app.utility.helps import response_json

from django.template.context_processors import csrf
import django_cms.settings
import os
import time
from django_cms.app.utility.helps import get_file_url
class FileController(View):
    '''
        展示文件上传
    '''
    def show_file_upload(request):
        param = request.GET
        post_name = param.get('post_name', 0)
        res = {}
        res['csrfmiddlewaretoken'] = csrf(request);
        res['post_name'] = post_name;
        return render(request, 'admin/files/upload_resource_html.html',res )

    def file_upload(request):
        if request.method == "POST":  # 请求方法为POST时，进行处理
            myFile = request.FILES.get("file", None)  # 获取上传的文件，如果没有文件，则默认为None
            if not myFile:
                return response_json(False,{'data':{'file_path':'11','file_id':0,'file_oldname':'test'}});
                return HttpResponse("no files for upload!")
            root_directory = os.path.dirname(django_cms.settings.__file__)+"/uploadfiles/"
            if not os.path.isdir(root_directory):
                os.makedirs(root_directory)

            now = int(time.time())
            destination = open(os.path.join(root_directory, str(now)+".png"), 'wb+')  # 打开特定的文件进行二进制的写操作
            for chunk in myFile.chunks():  # 分块写入文件
                destination.write(chunk)
            destination.close()
            return response_json(True,{'data':{'file_path':"/uploadfiles/"+str(now)+".png",'file_id':0,'file_oldname':myFile.name}});
        return


