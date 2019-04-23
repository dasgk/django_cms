<template>
	<div>
		<el-aside>
			<!--搜索内容开始-->
			
		</el-aside>
		<!--占位使用，不做任何处理-->
		<el-aside style="width:100px">
		</el-aside>
		<!--占位使用，不做任何处理-->
	</div>
</template>
<script type="text/ecmascript-6">
	// 引入外部整理好的css文件
	import "@/css/html_aside.css"
	import databus from "@/datacenterbus.js"
	var vue
	export default {
		name: 'html_aside',
		
		data() {
			return {
			};
		},
		methods: {
		}

	}
	$(document).ready(function() {
		//请求分类列表
		$.ajax({
			type: "GET",
			url: "http://127.0.0.1:8000/api/cate_list",
			dataType: "json",
			success: function(data) {
				vue.cate_list = data.data
			}
		});
		//我的标签
		$.ajax({
			type: "GET",
			url: "http://127.0.0.1:8000/api/label_list",
			dataType: "json",
			success: function(data) {
				vue.label_list = data.data
			}
		});
	});
</script>