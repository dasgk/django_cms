<!--这里是文章详情-->
<template id="article_main" style="background-color: white;width:60%;overflow-x: hidden;overflow-y: hidden;">
	<div id="test-editormd">
		<textarea v-model="article_content"></textarea>

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
				article_content: ""
			}
		},
		created: function() {
			vue = this
		},
		mounted: function() {
			//修改显示的文章详情
			this.$root.databus.$on('current_article_id', function(article_id) {
				// 显示对应的文章详情
				current_article_id = article_id;
				axios.get('/article_detail', {
					params: {
						'article_id': current_article_id
					}
				}).then((response) => {
					vue.article_content = response.data.data.content
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