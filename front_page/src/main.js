import Vue from 'vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import App from './components/index'
import ArticleDetail from './components/article_detail'
import VueRouter from 'vue-router'
import databus from "@/datacenterbus.js"
const routes = [
  { path: '/', component: {'main_content':App},'name':'article_list'},
  { path: '/detail', component: {'main_content':ArticleDetail},'name':'article_detail'},
]

var router = new VueRouter({
  mode:'history',
  routes // （缩写）相当于 routes: routes
})
Vue.use(ElementUI);
Vue.use(VueRouter)

new Vue({
    el: '#app',
    router: router,
    data:{
    	databus
    },
    render: h => h(App),
  }
);
