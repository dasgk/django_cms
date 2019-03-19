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
			<!--占位使用，不做任何处理-->
			<el-main style="margin-left: -17%;    margin-top: -50px;">

				<div v-for="article in article_list">

					<div class="day">
						<div class="dayTitle">
							<a id="homepage1_HomePageDays_ctl00_ImageLink" href="https://www.cnblogs.com/haoyifei/">置顶随笔</a>
						</div>

						<div class="postTitle">
							<a id="homepage1_HomePageDays_ctl00_DayList_TitleUrl_0" class="postTitle2" href="https://www.cnblogs.com/haoyifei/p/5641115.html">{{article.title}}</a>
						</div>
						<div class="postCon">
							<div class="c_b_p_desc">摘要:{{article.content}}
								<a href="https://www.cnblogs.com/haoyifei/p/5641115.html" class="c_b_p_desc_readmore">阅读全文</a>
							</div>
						</div>
						<div class="clear"></div>
						<div class="postDesc"><i class="el-icon-edit"></i>posted @ {{article.updated_at}} 周建业 阅读({{article.look_num}})

						</div>
						<div class="clear"></div>

					</div>

				</div>
			</el-main>
			<html_aside v-bind:article_list="article_list" v-on:change_articles="article_changed"></html_aside>
		</el-container>
		<el-footer style="height:13%;"></el-footer>
	</el-container>
</template>
<script type="text/ecmascript-6">
	import navigate from '@/components/navigate';
	import html_aside from '@/components/html_aside';
	import 'jquery'
	// 引入外部整理好的css文件
	import "@/css/article_list.css"
	var vue;
	export default({
		name: 'App',
		data() {
			return {
				article_list: [],
			}
		},
		components: {
			navigate: navigate,
			html_aside: html_aside
		},
		created: function() {
			vue = this
		},
		methods: {
			article_changed: function(event) {
				this.article_list = event;
			}
		}
	})

	$(document).ready(function() {
		//请求文章列表
		$.ajax({
			type: "GET",
			url: "http://127.0.0.1:8000/api/article_list",
			dataType: "json",
			success: function(data) {
				vue.article_list = data.data
			}
		});
	});
</script>