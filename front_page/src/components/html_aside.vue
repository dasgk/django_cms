<template>
	<div>
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
		<el-row style="height:37%;margin-left: -43%;    margin-top: -15px;">
			<el-col :span="24" style=" text-align:center;height: 29%;    line-height: 400%;">
				<div class="grid-content bg-purple-dark" style="margin-left: 10px;">
					<span style='color: black;font-size: 22px;'>我的标签</span>
				</div>
			</el-col>
			<el-col :span="24" class="type_list" style='margin-left: 40px;'>
				<div class="grid-content bg-purple-dark">
					<span id="label_list" v-for="label in label_list" @click='article_list_by_label(label.label_id)'>
								{{label.title}}({{label.article_count}}),
							</span>
				</div>
			</el-col>
		</el-row>
		<!--我的标签结束-->

		<!--我的经常访问开始-->
		<el-row style="margin-top: -15px;height:37%;    margin-left: -43%;">
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
	</div>
</template>
<script type="text/ecmascript-6">	
	// 引入外部整理好的css文件
	import "@/css/html_aside.css"	
	var vue
	export default {
		name: 'html_aside',
		props:['article_list'],
		data() {
			return {				
				cate_list :[],
				label_list :[],
			};
		},		
		methods: {
			article_list_by_cate(cate_id) {
				$.ajax({
					type: "GET",
					url: "http://127.0.0.1:8000/api/article_list",
					data: {
						'cate_id': cate_id
					},
					dataType: "json",
					success: function(data) {
						vue.$emit("change_articles",data.data)
					}
				});
			},
			article_list_by_label(label_id) {
				$.ajax({
					type: "GET",
					url: "http://127.0.0.1:8000/api/article_list",
					data: {
						'label_id': label_id
					},
					dataType: "json",
					success: function(data) {
						vue.$emit('change_articles',data.data)
					}
				});
			},
			search_article() {
				var title = $("#search").val()
				$.ajax({
					type: "GET",
					url: "http://127.0.0.1:8000/api/article_list",
					data: {
						'title': title
					},
					dataType: "json",
					success: function(data) {
						vue.$emit('change_articles',data.data)
					}
				});
			}
		},
		created: function() {
			vue = this
		},
		
	}
	$(document).ready(function() {		
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
				vue.label_list = data.data
			}
		});
	});
</script>