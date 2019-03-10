import datetime
import logging

class TimeDao(object):
    @staticmethod
    def get_current_time():
        # 删除文章
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在
        return now