from django_cms.app.Dao.ConstDao import ConstDao
import math


class PageDao(object):
    def __init__(self, total_count, page_count , current_page):
        self.total_count = total_count  #总数量
        self.page_count = page_count   #每页元素数量
        self.current_page = current_page  #当前页码

    '''
        获得分页的数量，共有多少页
    '''
    def page_range(self):
        max_page_num = math.ceil(self.total_count / self.page_count)
        #range 是左闭右开
        return range(1, max_page_num+1)

    def has_previous(self):
        current_page = self.current_page
        for page_num in self.page_range():
            if page_num < current_page:
                return True
        return False

    def previous_page_number(self):
        current_page = self.current_page
        for page_num in reversed(self.page_range()):
            if page_num < current_page:
                return page_num
        return 1   #默认返回1

    def has_next(self):
        current_page = self.current_page
        for page_num in self.page_range():
            if page_num > current_page:
                return True
        return False

    def next_page_number(self):
        current_page = self.current_page
        for page_num in self.page_range():
            if page_num > current_page:
                return page_num
        return 1  #默认返回1

    def get_total_count(self):
        return self.total_count