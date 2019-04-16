import Vue from 'vue';
import ElementUI from 'element-ui';
import App from './components/article_list';
Vue.use(ElementUI);

new Vue({
	el: '#app',
	render: h => h(App),
	},
);
