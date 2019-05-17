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

		<!----显示评论输入框 -->
		<div style="text-align: left;">
			<h4 name="a1" style="    line-height: 20px;font-size: 22px;">讨论这个项目（{{comment_num}}）</h4>
			<el-input  style="    width: 80%;margin-left: 5%;display: block;"type="textarea" :rows="4" placeholder="请输入您的高见">
			</el-input>
			  <el-button type="success" icon="el-icon-chat-line-square" plain></el-button>
		</div>
		<!----显示评论输入框结束 -->

	</div>
</template>

<script src="./js/editor.md-master/js/editormd.js"></script>
<link rel="stylesheet" type="text/css" href="./js/editor.md-master/css/editormd.css" />
<script>
	import "jQuery";
	import "@/css/layout.css";
	import "@/js/editor.md-master/css/editormd.css";
	import "@/js/editor.md-master/editormd.min.js";
	import "@/js/editor.md-master/lib/marked.min.js";
	import "@/js/editor.md-master/lib/prettify.min.js";
	import axios from 'axios'
	var current_article_id = 0;
	var vue = null;
	export default {
		data() {
			return {
				article_content: "",
				article_title: "",
				comment_num:0
			}
		},
		created: function() {
			vue = this
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
				axios.get('/article_detail', {
					params: {
						'article_id': current_article_id
					}
				}).then((response) => {
					vue.article_content = response.data.data.content
					vue.article_title = response.data.data.title
					vue.comment_num = response.data.data.comment_num
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
			})
		},
	}
</script>