<template>
	<el-container style=" background-color: white;margin-left: 12%;margin-right: 12%;margin-top: 5%;">
		<el-header style="height:13%;">
			<h1><a id="Header1_HeaderTitle" class="headermaintitle" >dagsk的文集</a></h1>
			<!--<template>-->
			<navigate> </navigate>
			<!--</template>-->
		</el-header>
		<el-container>
			<!--占位使用，不做任何处理-->
			<el-aside>

			</el-aside>
			<!--占位使用，不做任何处理-->
			<el-main></el-main>
			<el-aside>
				<!--搜索内容开始-->
				<el-row style="height: 17%;">
					<el-col :span="12" style="    margin-top: 12%; margin-bottom:-5px;margin-left: 5%;">
						<input type="text" autocomplete="off" placeholder="请输入内容" class="el-input__inner">
					</el-col>
					<el-col :span="12" style="margin-top: -12%; margin-bottom:-5px; margin-left: 59%;">
						<el-button type="primary" icon="el-icon-search">搜索</el-button>
					</el-col>
				</el-row>
				<!--搜索内容结束-->

				<!--我的分类开始-->
				<el-row style="margin-top: 7%;height:37%;    margin-left: -43%;">
					<el-col :span="24" style=" text-align:center;height: 29%;    line-height: 400%;">
						<div class="grid-content bg-purple-dark"><span style='color: black;font-size: 22px;'>我的分类</span></div>
					</el-col>
					<el-col :span="24" class="type_list">
						<div class="grid-content bg-purple-dark"><span class="type_font">我的分类</span></div>
					</el-col>
					<el-col :span="24" class="type_list">
						<div class="grid-content bg-purple-dark"><span class="type_font">我的分类</span></div>
					</el-col>
					<el-col :span="24" class="type_list">
						<div class="grid-content bg-purple-dark"><span class="type_font">我的分类</span></div>
					</el-col>
				</el-row>
				<!--我的分类结束-->

				<!--我的标签开始-->
				<el-row style="margin-top: 25%;height:37%;    margin-left: -43%;">
					<el-col :span="24" style=" text-align:center;height: 29%;    line-height: 400%;">
						<div class="grid-content bg-purple-dark"><span style='color: black;font-size: 22px;'>我的标签</span></div>
					</el-col>
					<el-col :span="24" class="type_list">
						<div class="grid-content bg-purple-dark"><span>我的分类</span></div>
					</el-col>
				</el-row>
				<!--我的标签结束-->

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
	.type_list {
		text-align: center;
		line-height: 294%;
	}
	
	.type_font {
		color: grey;
		font-size: 22px;
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
	body{
		font-family: KaiTi;
	}
</style>
<script type="text/ecmascript-6">
	import navigate from '@/components/navigate';
	export default {
		name: 'App',
		data() {
			return {
				input: ''
			}
		},
		components: {
			navigate: navigate
		}
	}
</script>