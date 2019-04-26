<template>
	<el-container style="height:100%">
		<el-header style="height:63px;background-color: white;">
			<!-- 页面头部 -->
			
			<html_header></html_header>
			<!-- 页面头部结束 -->
		</el-header>
		<el-container style="height:100%">


			<!--占位使用-->
			<el-aside height="100%" style="background-color: white;;width:10%"></el-aside>
			<!-- 占位结束 -->


			<!--这里是文章列表-->
			<el-main style="background-color: white;width:60%">
        <!--  文章列表 -->
          <article_list>
          </article_list>
			</el-main>
			<!----  文章列表结束  -->


			<el-aside  style="width:25%;background-color: white;height:100%">
				<!--这里是侧边栏-->
				<html_aside></html_aside>
				<!-- 这里是侧边栏 -->
			</el-aside>


			<!--占位使用-->
			<el-aside  height="100%" style="width:10%;background-color: white;">
    	</el-aside>
    	<!-- 占位结束 -->


		</el-container>
	</el-container>
</template> 
<script type="text/ecmascript-6">
	import "@/css/layout.css"
	import databus from "@/datacenterbus.js"
	import html_header from "@/components/header"
	import html_aside from "@/components/html_aside"
	import article_list from "@/components/article_list"
	import 'jquery'
	// 引入外部整理好的css文件
	var vue;
	export default({
		name: 'App',
		data() {
			return {
			}
		},
		created: function() {
		},
		components: {
			html_header: html_header,
			html_aside: html_aside,
			article_list:article_list
		}
	})
</script>
