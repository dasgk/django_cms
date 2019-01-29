class MenuDao:
    @staticmethod
    def getMenuListByUser():
        menu_list = MenuDao.getMenuList()
        return menu_list

    # 可选的id 有 menu-article menu-product  menu-comments menu-member menu-admin menu-tongji menu-system
    @staticmethod
    def getMenuList():
        return [
            {
                'id': 'menu-article',
                'text': '文章管理',
                'icon_class': '',
                'nodes': [
                    {
                        'url': '/admin/article',
                        'title': '文章列表'
                    },
                ]
            },
        ]
