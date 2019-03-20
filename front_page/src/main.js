import Vue from 'vue';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import App from './components/article_list';
import 'jquery'
import routers from'./router/index'
Vue.use(ElementUI);

new Vue({
		el: '#app',
		render: h => h(App),
    router:routers
	},
);
