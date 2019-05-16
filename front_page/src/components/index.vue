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
			<el-main style="background-color: white;width:60%">
        <!--  文章列表 -->
        <article_list v-if=article_list_show></article_list>
        <article_detail v-if=article_detail_show></article_detail>

			</el-main>
			<!----  文章列表结束  -->


			<el-aside  style="width:25%;background-color: white;">
				<!--这里是侧边栏-->
				<html_aside></html_aside>
        <!---    npm install ele-calendar  -->
				<!-- 这里是侧边栏 -->
			</el-aside>


			<!--占位使用-->
			<el-aside  height="100%" style="width:8%;background-color: white;">
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
  import article_detail from "@/components/article_detail"

	import 'jquery'
	// 引入外部整理好的css文件
	export default({
		name: 'App',
		data() {
			return {
			  article_list_show:1,
        article_detail_show:0
			}
		},
		created: function() {
		},

      watch: {
      '$route.path': function (newVal, oldVal) {
        console.log(newVal)
      }
    },
		components: {
			html_header: html_header,
			html_aside: html_aside,
      article_list:article_list
		}
	})
</script>
