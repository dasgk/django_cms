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

					<article class="comment" v-for="comment in comment_list">
						<div class="meta">
							<img :src='comment.random_avatar' class="avatar">
							<h3><a href="#" class="author">{{comment.ip_address}}</a></h3>
							<a href="#" class="date">
								<time datetime="2015-01-01">{{comment.time}}</time>
							</a>
						</div>
						<div class="content">
							<p>{{comment.content}}</p>
						</div>
					</article>
				</section>

				<div style="background-color: #fff;border: 1px solid #dadada;height: 185px;border-radius: 4px;padding: 22px 25px;position: relative;margin-left: 22px;margin-right: 22px;">
					<div class="grid-content bg-purple-dark">我来回答</div>
					<form method="post" action="" target="_send" id="dform">
						<input type="hidden" name="qid" value="1407844">
						<input type="hidden" name="qtype" value="fanyi">
						<div class="px14">
							<table width="100%" cellpadding="8" cellspacing="1">
								<tbody>
									<tr>
										<td>
											<el-input  type="textarea" v-model="textarea" :autosize="{ minRows: 4, maxRows: 4}" placeholder="请输入内容" style="width:100%" >
											</el-input>
											<br><span id="dicontent" class="f_red px12"></span>
										</td>
									</tr>
									<tr>
										<td class="px12">
											<el-button plain style="margin-left:5%" @click="monisubmit()" >提交评论</el-button>
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


<script>
	import 'jquery'
	import databus from "@/datacenterbus.js"
	import "@/css/article_detail.css"
	import "@/js/layer/layer.js"

	var vue;
	export default({
		name: 'App',
		data() {
			return {
				article_id: 0,
				title: '',
				updated_at: '',
				content: '',
				comment_list: [],
				textarea:'',
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
						vue.comment_list = data.data['comments']
					}
				});
			})
		},
		methods:{
	  	monisubmit:function(){
      var comments = vue.textarea
	  		$.ajax({
					type: "GET",
					url: "http://127.0.0.1:8000/api/comment_update",
					data: {
						'article_id': vue.article_id,
						'comment':comments
					},
					dataType: "json",
					success: function(data) {

					alert('操作成功')
          vue.textarea = '';


					}
				});

	  	}
		}
	})
</script>



<style>

</style>

