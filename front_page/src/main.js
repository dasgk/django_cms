import Vue from 'vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import App from './components/index'
import ArticleDetail from './components/article_detail'
import VueRouter from 'vue-router'
//import ArticleDetail from './components/article_detail'
//import router from './router'

const routes = [
  { path: '/', component: App,'name':'article_list'},
  { path: '/detail', component: ArticleDetail,'name':'article_detail'},
]

var router= new VueRouter({
  mode:'history',
  routes // （缩写）相当于 routes: routes
})
Vue.use(ElementUI);

new Vue({
	el: '#app',
	router,
	render: h => h(App),
	}
);
