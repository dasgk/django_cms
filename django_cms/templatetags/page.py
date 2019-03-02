from django import template

register=template.Library() #对象名必须为register
@register.simple_tag()
def view_page(object_list, paginator, current_page):
    html = '<ul class="pagination" id="pager">'
    #html +='    {#上一页按钮开始#}'
    #html +='   {# 如果当前页有上一页#}'
    #html +=' {% if book_list.has_previous %}'
    if object_list.has_previous :
        #html +='        {#  当前页的上一页按钮正常使用#}'
        html +='        <li class="previous"><a href="/?page={{ book_list.previous_page_number }}">上一页</a></li>'
    #html +='    {% else %}'
    else:
        #html +='        {# 当前页的不存在上一页时,上一页的按钮不可用#}'
        html +='        <li class="previous disabled"><a href="#">上一页</a></li>'
    #html +='    {% endif %}'
    #html +='    {#上一页按钮结束#}'
    #html +='    {# 页码开始#}'
    # html +='    {% for num in paginator.page_range %}'
    for num in paginator.page_range:
        html +=''
        #html +='        {% if num == currentPage %} '
        if num == current_page:
            html +='            <li class="item active"><a href="/?page={{ num }}">{{ num }}</a></li> '
    #html +='        {% else %}'
        else:
            html +='            <li class="item"><a href="/?page={{ num }}">{{ num }}</a></li>'

    #html +='        {% endif %}'
    #html +='    {% endfor %}'
    #html +='    {#页码结束#}'
    #html +='    {# 下一页按钮开始#}'
    #html +='    {% if book_list.has_next %} '
    if object_list.has_next:
        html +='        <li class="next"><a href="/?page={{ book_list.next_page_number }}">下一页</a></li>'
    #html +='    {% else %}'
    else:
        html +='        <li class="next disabled"><a href="#">下一页</a></li>'
    #html +='    {% endif %} '
    html +='</ul>'
    return html