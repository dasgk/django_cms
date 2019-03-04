from django import template
import logging
from django_cms.app.Dao.ConstDao import ConstDao

register = template.Library() #对象名必须为register

def get_current_uri(page_num, url, getParam):
    is_first = True
    # 默认情况下 page为1，可能page没有
    is_add_page = False
    for key, value in getParam.items():
        if is_first:
            if key == 'page':
                url += '?page=' + str(page_num)
                is_add_page = True
            else:
                url += '?'+key+'='+value
            is_first = False
        else:
            if key == 'page':
                url += '&page=' + str(page_num)
                is_add_page = True
            else:
                url += '&'+key+'='+value
    if not is_add_page:
        if is_first:
            url += '?page=' + str(page_num)
        else:
            url += '&page=' + str(page_num)
    return url

@register.simple_tag()
def view_page(object_list, paginator, request):
    current_page = request.GET.get('page',1)
    current_page = int(current_page)
    '''
    logger = logging.getLogger('default')
    logger.error(current_page)
    logging.error(paginator.page_range)
    '''
    html = ' <div class="row" >'
    html +='<div class="col-sm-12"> '
    html += '<div>共 '
    html += str(paginator.count)
    html += '条记录</div>'
    html += '<ul class="pagination" id="pager">'
    if object_list.has_previous():
        html +='<li class="previous"><a href="'
        html += get_current_uri(object_list.previous_page_number(),  request.path, request.GET)
        html +='">上一页</a></li>'
    else:
        html +='<li class="previous disabled"><a href="#">上一页</a></li>'
    #进行精简，如果是第一页，则不处理，如果是其他情况，开始从 current_page-1开始算起
    page_range = paginator.page_range
    if current_page != 1 and current_page != 2:
        page_range = page_range[current_page-2:]
    #分页，只取 定义最大数量的页码
    page_range = page_range[0:ConstDao.maxPageCount()]
    for num in page_range:
        if num == current_page:
            html +='<li class="item active"><a href="'
            html += get_current_uri(num, request.path, request.GET)
            html +='">'
            html += str(num)
            html +='</a></li> '
        else:
            html +='<li class="item"><a href="'
            html += get_current_uri(num, request.path, request.GET)
            html +='">'
            html +=str(num)
            html +='</a></li>'

    if object_list.has_next():
        html +='<li class="next"><a href="'
        html += get_current_uri(object_list.next_page_number(), request.path, request.GET)
        html +='">下一页</a></li>'
    else:
        html +='<li class="next disabled"><a href="#">下一页</a></li>'
    html +='</ul>'
    html += '</div>'
    html += '</div>'
    html += '</div>'
    return html