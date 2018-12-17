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
                'text': '测试菜单',
                'icon_class': '',
                'url': 'http://www.baidu.com',
                'nodes':[
                    {
                        'url':'http://www.baidu.com',
                        'title':'测试菜单'
                    },
                ]
            },
        ];
