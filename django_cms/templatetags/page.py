from django import template
import logging

register=template.Library() #对象名必须为register

def get_current_uri(page_num, url, getParam):
    is_first = True
    for key, value in getParam.items():
        if is_first:
            if key == 'page':
                url += '?page=' + str(page_num)
            else:
                url += '?'+key+'='+value
            is_first = False
        else:
            if key == 'page':
                url += '&page=' + str(page_num)
            else:
                url += '&'+key+'='+value

    return url

@register.simple_tag()
def view_page(object_list, paginator, current_page, url, getParam):
    html = ' <div class="row" >'
    html +='<div class="col-sm-12"> '
    html += '<div>共 '
    html += str(paginator.count)
    html += '条记录</div>'
    html += '<ul class="pagination" id="pager">'
    if object_list.has_previous:
        html +='<li class="previous"><a href="'
        html += get_current_uri(object_list.previous_page_number, url, getParam)
        html +='">上一页</a></li>'
    else:
        html +='<li class="previous disabled"><a href="#">上一页</a></li>'

    for num in paginator.page_range:
        if num == current_page:
            html +='<li class="item active"><a href="'
            html += get_current_uri(num, url, getParam)
            html +='">'
            html += str(num)
            html +='</a></li> '
        else:
            html +='<li class="item"><a href="'
            html += get_current_uri(num, url, getParam)
            html +='">'
            html +=str(num)
            html +='</a></li>'

    if object_list.has_next:
        html +='<li class="next"><a href="'
        html += get_current_uri(object_list.next_page_number, url, getParam)
        html +='">下一页</a></li>'
    else:
        html +='<li class="next disabled"><a href="#">下一页</a></li>'
    html +='</ul>'
    html += '</div>'
    html += '</div>'
    html += '</div>'
    return html