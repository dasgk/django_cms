import Vue from 'vue'
import Router from 'vue-router'

import index from '@/components/index'
import ArticleDetail from '@/components/article_detail'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: index
    },
    {
      path: '/index',
      name: 'index',
      component: index
    },
    {
      path: '/article_detail',
      name: 'article_detail',
      component: ArticleDetail
    }
  ]
})
