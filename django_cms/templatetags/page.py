from django import template
import logging

register=template.Library() #对象名必须为register

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

    for num in paginator.page_range:
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