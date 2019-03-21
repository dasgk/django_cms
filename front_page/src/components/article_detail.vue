<template>
	<el-main style="margin-left: -17%;    margin-top: -50px;">
		<div>
			<div class="day" >
				<div class="dayTitle">
					<a href="javascript:void(0)" id="homepage1_HomePageDays_ctl00_ImageLink">置顶随笔</a>
				</div>

				<div class="postTitle">
					<a href="javascript:void(0)" id="homepage1_HomePageDays_ctl00_DayList_TitleUrl_0" class="postTitle2">2121212</a>
				</div>
				<div class="postCon">
					<div class="c_b_p_desc">摘要:21212121
						<a href="javascript:void(0)" class="c_b_p_desc_readmore">阅读全文</a>
					</div>
				</div>
				<div class="clear"></div>
				<div class="postDesc"><i class="el-icon-edit"></i>posted @11212周建业 阅读(12121)

				</div>
				<div class="clear"></div>
			</div>
		</div>
	</el-main>
</template>

<script>
	
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
		}
	})

	$(document).ready(function() {
		//请求文章列表
		$.ajax({
			type: "GET",
			url: "http://127.0.0.1:8000/api/article_list",
			dataType: "json",
			success: function(data) {
			
			}
		});
	});
</script>

<style>

</style>