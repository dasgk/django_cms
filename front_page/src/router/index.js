import Vue from 'vue'
import Router from 'vue-router'
import ArticleDetail from '@/components/article_detail'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: ArticleDetail
    }
  ]
})
