import Vue from 'vue'
import Calendar from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import App from './components/index'
Vue.use(Calendar);
Vue.config.productionTip=false;
new Vue({
	el: '#app',
	render: h => h(App),
	},
);
