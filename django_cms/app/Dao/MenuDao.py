class MenuDao:
    @staticmethod
    def getMenuListByUser():
        menu_list = MenuDao.getMenuList()
        return menu_list

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
