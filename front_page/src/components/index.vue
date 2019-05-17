<template>
	<el-container>
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
			<el-main style="background-color: white;width:60%;overflow-x: hidden;">
				<!--  文章列表 -->
				<article_list v-show=article_list_show></article_list>
				<article_detail v-show=article_detail_show></article_detail>

			</el-main>
			<!----  文章列表结束  -->

			<el-aside style="width:25%;background-color: white;">
				<!--这里是侧边栏-->
				<html_aside></html_aside>
				<!---    npm install ele-calendar  -->
				<!-- 这里是侧边栏 -->
			</el-aside>

			<!--占位使用-->
			<el-aside height="100%" style="width:8%;background-color: white;">
			</el-aside>
			<!-- 占位结束 -->

		</el-container>
	</el-container>
</template>

<script type="text/ecmascript-6">
	import "@/css/layout.css"

	import html_header from "@/components/header"
	import html_aside from "@/components/html_aside"
	import article_list from "@/components/article_list"
	import article_detail from "@/components/article_detail"
	import 'jquery'
	var vue
	// 引入外部整理好的css文件
	export default({
		name: 'App',
		data() {
			return {
				article_list_show: true,
				article_detail_show: false
			}
		},
		created: function() {
			vue = this
		},

		mounted: function() {
			//监听显示列表还是详情			
			this.$root.databus.$on('article_list_show', function(val) {
				if(val == 1) {
					vue.article_list_show = true;
					vue.article_detail_show = false;
				} else {
					vue.article_list_show = false;
					vue.article_detail_show = true;
				}

			})
			this.$root.databus.$on('article_detail_show', function(val) {				
				if(val == 1) {
					vue.article_detail_show = true;
					vue.article_list_show = false;					
				} else {
					vue.article_list_show = true;
					vue.article_detail_show = false;
				}
			})
		},
		components: {
			html_header: html_header,
			html_aside: html_aside,
			article_list: article_list,
			article_detail: article_detail
		}
	})
</script>