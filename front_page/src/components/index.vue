<template>
	<el-container style=" background-color: white;margin-left: 12%;margin-right: 12%;margin-top: 5%;">
		<el-header style="height:13%;">
			<h1><a id="Header1_HeaderTitle" class="headermaintitle" >dagsk的文集</a></h1>
			<!--引入的组件不需要增加template-->
			<navigate> </navigate>
			<!--引入的组件不需要增加template-->
		</el-header>
		<el-container>
			<!--占位使用，不做任何处理-->
			<el-aside>
			</el-aside>
			<!--默认进来是文章列表-->
			<article_list v-show=is_show_list></article_list>
			<!--默认进来是文章列表-->
			<article_detail v-show=is_show_detail></article_detail>
			<html_aside ></html_aside>
		</el-container>
		<el-footer style="height:13%;"></el-footer>
	</el-container>
</template>
<script type="text/ecmascript-6">
	import navigate from '@/components/navigate';
	import html_aside from '@/components/html_aside';
	import article_list from '@/components/article_list';
	import article_detail from '@/components/article_detail';
	import databus from "@/datacenterbus.js"

	import 'jquery'
	// 引入外部整理好的css文件

	var vue;
	export default({
		name: 'App',
		data(){
			return{
				is_show_list:true,
				is_show_detail:false
			}
		},
		created:function(){
			vue = this
			databus.$on('update_is_show_list',function(data){
				vue.is_show_list= data				
			}),
			databus.$on('update_is_show_detail',function(data){
				vue.is_show_detail= data
			})
		},
		components: {
			navigate: navigate,
			html_aside: html_aside,
			article_list: article_list,
			article_detail: article_detail
		}
	})
</script>