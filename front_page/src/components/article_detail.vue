<template>
	<el-main style="margin-left: -17%;    margin-top: -50px;">
		<div>
			<div class="day">
				<div class="dayTitle">
					<a href="javascript:void(0)" id="homepage1_HomePageDays_ctl00_ImageLink">置顶随笔</a>
				</div>

				<div class="postTitle">
					<span id="homepage1_HomePageDays_ctl00_DayList_TitleUrl_0" class="postTitle2">{{title}}</span>
				</div>
				<div class="postCon">
					<div class="c_b_p_desc">{{content}}
					</div>
				</div>
				<div class="clear"></div>
				<div class="postDesc"><i class="el-icon-edit"></i>posted @{{updated_at}} 阅读(12121)
				</div>
				<div class="clear"></div>

				<section class="comments">
					<h1>评论内容</h1>
					<article class="comment ">
						<div class="meta">
							<img src="/assets/coolboy.jpg" class="avatar">
							<h3><a href="#" class="author">John Doe</a></h3>
							<a href="#" class="date">
								<time datetime="2015-01-01">Jan 1, 2015 at 9:18 AM</time>
							</a>
						</div>
						<div class="content">
							<p>Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.</p>
							<p>Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo.</p>
						</div>
					</article>
					<article class="comment ">
						<div class="meta">
							<img src="/assets/coolgirl.jpg" class="avatar">
							<h3><a href="#" class="author">Jane Doe</a></h3>
							<a href="#" class="date">
								<time datetime="2015-01-01">Jan 1, 2015 at 10:24 AM</time>
							</a>
						</div>
						<div class="content">
							<p>Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo. Quisque sit amet est et sapien ullamcorper pharetra. Vestibulum erat wisi, condimentum sed, commodo vitae, ornare sit amet, wisi. Aenean fermentum, elit eget tincidunt condimentum, eros ipsum rutrum orci, sagittis tempus lacus enim ac dui. </p>
						</div>
					</article>
				</section>

				<div style="background-color: #fff;border: 1px solid #dadada;height: 185px;border-radius: 4px;padding: 22px 25px;position: relative;margin-left: 22px;margin-right: 22px;">
					<div class="grid-content bg-purple-dark">我来回答</div>
					<form method="post" action="answer.php" target="_send" id="dform" onsubmit="return check();">
						<input type="hidden" name="qid" value="1407844">
						<input type="hidden" name="qtype" value="fanyi">
						<div class="px14">
							<table width="100%" cellpadding="8" cellspacing="1">
								<tbody>
									<tr>

										<td>
											<el-input type="textarea" :autosize="{ minRows: 4, maxRows: 4}" placeholder="请输入内容" v-model="comment">
											</el-input>
											<br><span id="dicontent" class="f_red px12"></span>
										</td>
									</tr>

									<tr>
										
										<td class="px12">
											<el-button plain style="margin-left:5%">提交评论</el-button>
										</td>
									</tr>
								</tbody>
							</table>
						</div>
					</form>
				</div>

			</div>
		</div>
	</el-main>
</template>



<style>
	.el-textarea__inner {
		min-height: 86px;
		height: 86px;

		resize: none;
		width: 600px;
		height: 100px;
		max-width: 800px;
		margin-left:5%;
		max-height: 100px;
	}
	
	.radius {
		height: 60px;
		width: 70%;
		border: 1px solid #d7dae2;
		border-radius: 0;
		margin-top: 20px;
	}
	
	@import url(http://fonts.googleapis.com/css?family=Merriweather:700|Open+Sans);
	body {
		background-color: #f8f8f8;
		color: #333;
		font-family: 'Open Sans', sans-serif;
		font-size: 16px;
		line-height: 25px;
	}
	
	h1,
	h2,
	h3,
	h4,
	h5,
	h6 {
		font-family: 'Merriweather', serif;
		font-weight: 700;
	}
	
	.comments {
		padding: 20px;
	}
	
	.comments article.comment {
		position: relative;
		margin-bottom: 30px;
	}
	
	.comments article.comment .meta {
		height: 60px;
		margin-bottom: 17px;
		position: relative;
	}
	
	.comments article.comment .meta img.avatar {
		position: absolute;
		border-radius: 30px;
		width: 60px;
		height: 60px;
		left: 0px;
		top: 0px;
	}
	
	.comments article.comment .meta a.author,
	.comments article.comment .meta a.date {
		text-decoration: none;
		position: absolute;
	}
	
	.comments article.comment .meta a.author {
		color: inherit;
		left: 73px;
		line-height: 29px;
		padding: 0px 7px;
		top: 3px;
	}
	
	.comments article.comment .meta a.date {
		font-size: 14px;
		line-height: 19px;
		color: #666;
		left: 80px;
		top: 35px;
	}
	
	.comments article.comment .content {
		background-color: #fff;
		border: 1px solid #dadada;
		border-radius: 4px;
		padding: 22px 25px;
		position: relative;
	}
	
	.comments article.comment .content:after,
	.comments article.comment .content:before {
		bottom: 100%;
		left: 30px;
		border: solid transparent;
		content: " ";
		height: 0;
		width: 0;
		position: absolute;
		pointer-events: none;
	}
	
	.comments article.comment .content:after {
		border-color: rgba(255, 255, 255, 0);
		border-bottom-color: #fff;
		border-width: 12px;
		margin-left: -12px;
	}
	
	.comments article.comment .content:before {
		border-color: rgba(245, 47, 47, 0);
		border-bottom-color: #dadada;
		border-width: 13px;
		margin-left: -13px;
	}
</style>

<script>
	import 'jquery'
	import databus from "@/datacenterbus.js"
	var vue;
	export default({
		name: 'App',
		data() {
			return {
				article_id: 0,
				title: '',
				updated_at: '',
				content: '',
				comment: ''
			}
		},
		created: function() {
			vue = this
			databus.$on('update_article_list', function(data) {
				vue.article_list = data
			})
			databus.$on('update_article_id', function(data) {
				vue.article_id = data
				$.ajax({
					type: "GET",
					url: "http://127.0.0.1:8000/api/article_detail",
					data: {
						'article_id': vue.article_id
					},
					dataType: "json",
					success: function(data) {
						vue.title = data.data['title']
						vue.content = data.data['content']
						vue.updated_at = data.data['updated_at']
					}
				});
			})
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