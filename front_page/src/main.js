import Vue from 'vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import App from './components/index'
//import App from './components/comments'
import ArticleDetail from './components/article_detail'
import VueRouter from 'vue-router'
import layer from 'vue-layer'
import databus from "@/datacenterbus.js"
import VueScroller from 'vue-scroller'

//使用layer

const routes = [
  { path: '/', component: {'main_content':App},'name':'article_list'},
  { path: '/detail', component: {'main_content':ArticleDetail},'name':'article_detail'},
]

var router = new VueRouter({
  mode:'history',
  routes // （缩写）相当于 routes: routes
})
Vue.use(ElementUI);
Vue.use(VueScroller);
Vue.use(VueRouter)
Vue.use(layer)
Vue.prototype.$layer = layer(Vue);
new Vue({
    el: '#app',
    router: router,
    data:{
    	databus
    },
    render: h => h(App),
  }
);
