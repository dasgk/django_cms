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
from django_cms.models import UploadFile
import json

class FileController(View):
    '''
        展示文件上传的html页面
    '''

    def show_file_upload(request):
        param = request.GET
        post_name = param.get('uploaded_type', 0)
        upload_file_type = UploadFile.objects.filter(type_key=post_name).first()
        res = {}
        res['csrfmiddlewaretoken'] = csrf(request)
        res['post_name'] = post_name
        res['type_key'] = post_name
        res['path'] = upload_file_type.path
        res['allow_type'] = upload_file_type.allow_type
        res['allow_num'] = upload_file_type.allow_num
        res['allow_size'] = upload_file_type.allow_size
        res['file_id'] = param.get('file_id','')
        res['allow_size_m'] = upload_file_type.allow_size / 1024 / 1024
        mimeArray = {};
        mimeArray['gif'] = 'image/gif';
        mimeArray['jpg'] = 'image/jpeg';
        mimeArray['jpeg'] = 'image/jpeg';
        mimeArray['png'] = 'image/png';
        mimeArray['xml'] = 'text/xml';
        mimeArray['svg'] = 'image/svg+xml';
        mimeArray['xls'] = 'application/vnd.ms-excel';
        mimeArray['xlsx'] = 'application/vnd.ms-excel';
        mimeArray['zip'] = 'application/zip';
        mimeArray['rar'] = 'application/x-rar-compressed';
        mimeArray['mp3'] = 'audio/mpeg';
        extensions_arr = res['allow_type'].split('|')
        mimeTypes_arr = []
        for i in range(len(extensions_arr)):
            mimeTypes_arr.append(mimeArray[extensions_arr[i]])
        res['mimeArray'] = ','.join(mimeTypes_arr)
        return render(request, 'admin/files/upload_resource_html.html', res)

    def file_upload_for_editormd(request):
        myFile = request.FILES.get("editormd-image-file", None)  # 获取上传的文件，如果没有文件，则默认为None
        type_key = 'FT_ARTICLE_IMG'
        res = {}
        if not myFile:
            res['success'] = 0
            res['msg'] = '未找到上传文件'
            return HttpResponse(json.dumps(res, ensure_ascii=False), content_type="application/json,charset=utf-8")
        upload_file_type = UploadFile.objects.filter(type_key=type_key).first()
        if upload_file_type == None:
            return response_json(False, {}, '未找到对应key')
        root_directory = os.path.dirname(
            django_cms.settings.__file__) + "/static/uploadfiles/" + upload_file_type.path + "/"
        if not os.path.isdir(root_directory):
            os.makedirs(root_directory)
        now = int(time.time())
        # 获得文件名称
        filename = myFile.name
        file = os.path.splitext(filename)
        filename, type = file
        destination = open(os.path.join(root_directory, str(now) + type), 'wb+')  # 打开特定的文件进行二进制的写操作
        for chunk in myFile.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()
        res['success'] = 1
        res['url'] = "/static/uploadfiles/" + upload_file_type.path + "/" + str(now) + type
        return HttpResponse(json.dumps(res, ensure_ascii=False), content_type="application/json,charset=utf-8")



    def file_upload(request):
        myFile = request.FILES.get("file", None)  # 获取上传的文件，如果没有文件，则默认为None
        type_key = request.POST.get('type_key')
        if not myFile:
            return response_json(False, {'data': {'file_path': '11', 'file_id': 0, 'file_oldname': 'test'}});
        upload_file_type = UploadFile.objects.filter(type_key=type_key).first()
        if upload_file_type == None:
            return response_json(False, {}, '未找到对应key')
        root_directory = os.path.dirname(
            django_cms.settings.__file__) + "/static/uploadfiles/" + upload_file_type.path + "/"
        if not os.path.isdir(root_directory):
            os.makedirs(root_directory)
        now = int(time.time())
        # 获得文件名称
        name = request.POST.get('name')
        file = os.path.splitext(name)
        filename, type = file
        destination = open(os.path.join(root_directory, str(now) + type), 'wb+')  # 打开特定的文件进行二进制的写操作
        for chunk in myFile.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()
        return response_json(True, {
            'data': {'file_path': "/static/uploadfiles/" + upload_file_type.path + "/" + str(now) + type, 'file_id': 0,
                     'file_oldname': myFile.name}});
