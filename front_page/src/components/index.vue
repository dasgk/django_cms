<template>
	<el-container>
		<el-header style="height:63px;background-color: white;">
			<!-- 页面头部 -->
			<html_header></html_header>
		</el-header>
		<el-container>
			<!--占位使用-->
			<el-aside height="100%" style="background-color: white;;width:10%"></el-aside>
			<!--这里是文章列表-->
			<el-main style="background-color: white;width:60%">
        <!--    文章列表   -->
          <article_list>
          </article_list>
        <!----  文章列表结束  -->
			</el-main>
			<el-aside  height="100%" style="width:20%;background-color: white;">
				<!--这里是侧边栏-->
				<left_frame></left_frame>
				<!-- 这里是侧边栏 -->
			</el-aside>
			<el-aside  height="100%" style="width:10%;background-color: white;">

			</el-aside>
		</el-container>
	</el-container>
</template>
<script type="text/ecmascript-6">
	import "@/css/layout.css"
	import databus from "@/datacenterbus.js"
	import html_header from "@/components/header"
	import left_frame from "@/components/left_frame"
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
			left_frame: left_frame,
			article_list:article_list
		}
	})
</script>
