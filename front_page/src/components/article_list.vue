<template>
	<el-main style="margin-left: -17%;    margin-top: -50px;">
		<div v-for="article in article_list">
			<div class="day" @click="article_detail(article.article_id)">
				<div class="dayTitle">
					<a href="javascript:void(0)" id="homepage1_HomePageDays_ctl00_ImageLink">置顶随笔</a>
				</div>

				<div class="postTitle">
					<a href="javascript:void(0)" id="homepage1_HomePageDays_ctl00_DayList_TitleUrl_0" class="postTitle2">{{article.title}}</a>
				</div>
				<div class="postCon">
					<div class="c_b_p_desc">摘要:{{article.content}}
						<a href="javascript:void(0)" class="c_b_p_desc_readmore">阅读全文</a>
					</div>
				</div>
				<div class="clear"></div>
				<div class="postDesc"><i class="el-icon-edit"></i>posted @ {{article.updated_at}} 周建业 阅读({{article.look_num}})

				</div>
				<div class="clear"></div>
			</div>

		</div>
	</el-main>
</template>

<script>
	import "@/css/article_list.css"
	import 'jquery'
	import databus from "@/datacenterbus.js"
	var vue;
	export default({
		name: 'App',
		data() {
			return {
				article_list: [],
			}
		},		
		created: function() {
			vue = this
			databus.$on('update_article_list',function(data){
				vue.article_list= data
			})
		},
		methods: {
			article_changed: function(event) {
				this.article_list = event;
			},
			//跳转到文章详情页面
			article_detail: function(article_id) {				
				//隐藏文章列表，显示文章详情
				databus.$emit('update_is_show_list',false);
				databus.$emit('update_is_show_detail',true);
				databus.$emit('update_article_id',article_id);
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
