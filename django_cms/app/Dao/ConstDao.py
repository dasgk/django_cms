class ConstDao(object):
    @staticmethod
    def getPageNum():
        return 15

    @staticmethod
    def getPrefixUrl():
        return 'http://127.0.0.1:8000'

    @staticmethod
    def maxPageCount():
        return 4