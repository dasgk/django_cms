<template>
	<el-container>
		<el-header style="height:63px;background-color: white;">
			<!-- 页面头部 -->
			<html_header></html_header>
		</el-header>
		<el-container>
			<!--占位使用-->
			<el-aside width="200px" height="100%" style="background-color: white;;width:13%"></el-aside>
			<!--这里是文章列表-->
			<el-main style="background-color: white;">Main</el-main>
			<el-aside width="200px" height="100%" style="width:36%;background-color: white;">
				<!--这里是侧边栏-->
				<left_frame></left_frame>
			</el-aside>
		</el-container>
	</el-container>
</template>
<script type="text/ecmascript-6">
	import "@/css/layout.css"
	import databus from "@/datacenterbus.js"
	import html_header from "@/components/header"
	import left_frame from "@/components/left_frame"
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
			left_frame: left_frame
		}
	})
</script>