<!--这里是文章详情-->
<template id="article_main" style="background-color: white;width:60%;overflow-x: hidden;overflow-y: hidden;">
	<!--文章标题开始--->
	<div>
		<div class="title" style="    line-height: 10px;font-size: 22px;">
			<h1>{{article_title}}</h1>
		</div>
		<!--文章标题结束-->

		<!--文章内容开始i --->
		<div id="test-editormd">
			<textarea v-model="article_content"></textarea>
		</div>
		<!--文章内容结束--->
	
		<!--评论列表开始-->		
		  <comments></comments>
		<!--评论列表结束-->
		<!----显示评论输入框 -->
		<div style="text-align: left;">
			<h4 name="a1" style="    line-height: 20px;font-size: 22px;">讨论这个项目</h4>
			<el-input v-model="comments" style="width: 90%;margin-left: 5%;display: block;" type="textarea" :rows="5" placeholder="请输入您的高见">
			</el-input>
			<el-button type="success" @click="submit_comment()" style="display: block;margin-left:94%;margin-top:2%" icon="el-icon-chat-line-square" plain></el-button>
		</div>
		<!----显示评论输入框结束 -->

	</div>
</template>
<script>
	import "@/css/layout.css";
	import "@/js/editor.md-master/css/editormd.css";
	import "@/js/editor.md-master/editormd.min.js";
	import "@/js/editor.md-master/lib/marked.min.js";
	import "@/js/editor.md-master/lib/prettify.min.js";
	import axios from 'axios'
import comments from "@/components/comments"
	var current_article_id = 0;
	var vue = null;

	function refresh_article(article_id) {
		axios.get('/article_detail', {
			params: {
				'article_id': article_id
			}
		}).then((response) => {
			vue.article_content = response.data.data.content
			vue.article_title = response.data.data.title
			vue.comment_num = response.data.data.comment_num
			//修改评论列表
			vue.$root.databus.$emit('comment_list',  response.data.data.comments);
			vue.$nextTick(function() {
				// 等待数据更新同步到DOM之后进行渲染
				editormd.markdownToHTML("test-editormd", {
					htmlDecode: "style,script,iframe", // you can filter tags decode
					emoji: true,
					taskList: true,
					tex: true, // 默认不解析
					sequenceDiagram: false, // 默认不解析
					marked: true, // 默认不解析
					path: './js/editor.md-master/lib'
				});
				this.$root.databus.$emit('article_detail_show', 1);
			})
		}).catch(function(response) {
			console.log(response); //发生错误时执行的代码
		});
	}

	export default {
		data() {
			return {
				article_content: "",
				article_title: "",
				comment_num: 0,
				comments: ''
			}
		},
		created: function() {
			vue = this
		},
		methods: {
			//提交评论
			submit_comment: function() {

				axios.get('/comment_update', {
					params: {
						'article_id': current_article_id,
						'comment': vue.comments
					}
				}).then((response) => {					
					var layer_index = vue.$layer.msg(response.data.msg,  function() {
						//当前文章页面刷新
						refresh_article(current_article_id)
						//清空之前评论内容
						vue.comments= '';
						//关闭当前弹出层
						vue.$layer.close(layer_index)
					});
				}).catch(function(response) {});
			},

		},
		mounted: function() {
			//修改显示的文章详情
			this.$root.databus.$on('current_article_id', function(article_id) {
				//文章阅读量自增
				axios.get('/article_look_num_incr', {
					params: {
						'article_id': article_id
					}
				});
				// 显示对应的文章详情
				current_article_id = article_id;
				refresh_article(current_article_id)
			})
		},
		  components:{
    	comments:comments
    }
	}
</script>