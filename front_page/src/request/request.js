/**axios封装
 * 请求拦截、相应拦截、错误统一处理
 */
import axios from 'axios';
import QS from 'qs';

 
// 环境的切换
if (process.env.NODE_ENV == 'development') { 
 axios.defaults.baseURL = 'http://127.0.0.1:8000/api';
} else if (process.env.NODE_ENV == 'debug') { 
 axios.defaults.baseURL = '';
} else if (process.env.NODE_ENV == 'production') { 
 axios.defaults.baseURL = 'http://api.123dailu.com/';
}
 
// 请求超时时间
axios.defaults.timeout = 10000;
 
// post请求头
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=UTF-8';

