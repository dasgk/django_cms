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
			<el-main style="margin-left: -17%;">

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
			<el-aside>
				<!--搜索内容开始-->
				<el-row style="height: 17%;">
					<el-col :span="12" style="    margin-top: 12%; margin-bottom:-5px;margin-left: 5%;">
						<input type="text" autocomplete="off" id="search" placeholder="请输入内容" class="el-input__inner">
					</el-col>
					<el-col :span="12" style="margin-top: -12%; margin-bottom:-5px; margin-left: 59%;">
						<el-button type="primary" @click='search_article()' icon="el-icon-search">搜索</el-button>
					</el-col>
				</el-row>
				<!--搜索内容结束-->

				<!--我的分类开始-->
				<el-row style="margin-top: 7%;height:37%;    margin-left: -43%;">
					<el-col :span="24" style=" text-align:center;height: 29%;    line-height: 400%;">
						<div class="grid-content bg-purple-dark">
							<span style='color: black;font-size: 22px;'>我的分类</span>
						</div>
					</el-col>
					<div v-for="cate in cate_list">
						<el-col :span="24" class="type_list">
							<div class="grid-content bg-purple-dark">
								<span class="type_font" @click='article_list_by_cate(cate.cate_id)'>{{cate.title}}({{cate.article_count}})</span>
							</div>
						</el-col>
					</div>
				</el-row>
				<!--我的分类结束-->

				<!--我的标签开始-->
				<el-row style="margin-top: 25%;height:37%;    margin-left: -43%;">
					<el-col :span="24" style=" text-align:center;height: 29%;    line-height: 400%;">
						<div class="grid-content bg-purple-dark">
							<span style='color: black;font-size: 22px;'>我的标签</span>
						</div>
					</el-col>
					<el-col :span="24" class="type_list">
						<div class="grid-content bg-purple-dark">
							{{labels}}
						</div>
					</el-col>
				</el-row>
				<!--我的标签结束-->

				<!--我的经常访问开始-->
				<el-row style="margin-top: 25%;height:37%;    margin-left: -43%;">
					<el-col :span="24" style=" text-align:center;height: 29%;    line-height: 400%;">
						<div class="grid-content bg-purple-dark">
							<span style='color: black;font-size: 22px;'>经常浏览</span>
						</div>
					</el-col>
					<el-col :span="24" class="type_list">
						<div class="grid-content bg-purple-dark"><span>我的分类</span></div>
					</el-col>
				</el-row>
				<!--我的经常访问结束-->

			</el-aside>
			<!--占位使用，不做任何处理-->
			<el-aside style="width:100px">
			</el-aside>
			<!--占位使用，不做任何处理-->
		</el-container>
		<el-footer style="height:13%;"></el-footer>
	</el-container>
</template>
<style>
	.postTitle {
		border-left: 3px solid #21759b;
		margin-bottom: 10px;
		font-size: 20px;
		float: right;
		width: 100%;
		clear: both;
	}
	
	.postCon {
		float: right;
		line-height: 1.5em;
		width: 100%;
		clear: both;
		padding: 10px 0;
	}
	
	.day .postTitle a {
		padding-left: 10px;
	}
	
	.postDesc {
		font-size: 13px;
		color: #757575;
		float: left;
		width: 100%;
		clear: both;
		text-align: left;
		padding-right: 5px;
		margin-top: 20px;
		line-height: 1.5;
	}
	
	.dayTitle {
		display: none;
		border: 1px solid #21759b;
		background: azure;
		border-radius: 50%;
		font-size: 12px;
		height: 65px;
		line-height: 1.5;
		margin: 15px;
		text-align: center;
		width: 63px;
		margin-left: -100px;
		clear: both;
		position: absolute;
		top: -15px;
	}
	
	.c_b_p_desc {
		font-size: 14px;
		line-height: 1.7;
	}
	
	.c_b_p_desc {
		word-wrap: break-word;
		word-break: break-all;
		overflow: hidden;
		line-height: 1.5;
	}
	
	.day {
		min-height: 10px;
		_height: 10px;
		margin-bottom: 20px;
		padding-bottom: 5px;
		position: relative;
	}
	
	.type_list {
		text-align: center;
		line-height: 294%;
	}
	
	.type_font {
		color: grey;
		font-size: 22px;
		cursor:pointer
	}
	
	.el-row {
		margin-left: 0px;
		margin-right: 0px;
		margin-top: 10px;
		height: 30%;
		background: white;
		margin-bottom: 20px;
		&:last-child {
			margin-bottom: 0;
		}
	}
	
	.el-input {
		height: 10px;
	}
	
	.el-col {
		border-radius: 4px;
		margin: auto;
	}
	
	.el-aside {
		overflow: hidden;
	}
	
	#blogTitle h1 {
		font-size: 26px;
		font-weight: bold;
		line-height: 1.5em;
		margin-top: 20px;
	}
	
	#app {
		font-family: 'Avenir', Helvetica, Arial, sans-serif;
		-webkit-font-smoothing: antialiased;
		-moz-osx-font-smoothing: grayscale;
		text-align: center;
		color: #2c3e50;
		margin-top: 60px;
	}
	
	body {
		font-family: KaiTi;
	}
</style>
<script src="https://code.jquery.com/jquery-1.11.3.js"></script>
<script type="text/ecmascript-6">
	import navigate from '@/components/navigate';
	import 'jquery'

	function privateFoo(data) {
		this.msg = data
	}
	var vue
	export default({
		name: 'App',
		data() {
			return {
				input: '',
				article_list: [],
				cate_list: [],
				labels: "",
			}
		},
		components: {
			navigate: navigate
		},
		created: function() {
			vue = this
		},
		methods:{
		   article_list_by_cate(cate_id){
  $.ajax({
		type: "GET",
		url: "http://127.0.0.1:8000/api/article_list",
		data:{'cate_id': cate_id},
		dataType: "json",
		success: function(data) {
			vue.article_list = data.data

		}
	});
},
search_article(){
var title = $("#search").val()
  $.ajax({
		type: "GET",
		url: "http://127.0.0.1:8000/api/article_list",
		data:{'title': title},
		dataType: "json",
		success: function(data) {
			vue.article_list = data.data

		}
	});



}

		}
	})


$(document).ready(function(){
 //请求文章列表
	$.ajax({
		type: "GET",
		url: "http://127.0.0.1:8000/api/article_list",
		dataType: "json",
		success: function(data) {
			vue.article_list = data.data

		}
	});
	//请求分类列表
	$.ajax({
		type: "GET",
		url: "http://127.0.0.1:8000/api/cate_list",
		dataType: "json",
		success: function(data) {
			vue.cate_list = data.data
		}
	});
	//我的标签
	$.ajax({
		type: "GET",
		url: "http://127.0.0.1:8000/api/label_list",
		dataType: "json",
		success: function(data) {
			for(var i = 0; i < data.data.length; i++) {
				if(data.data[i]['title'].length > 0) {
					vue.labels += data.data[i]['title'] + "("+data.data[i]['article_count']+"),"
				}
			}

		}
	});
});


</script>
