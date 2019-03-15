<template>
	<el-container style=" position: absolute;top: 0;left: 0;width: 100%; height: 100%;">
		<el-header style="height:13%;"></el-header>
		<el-container>
			<!--占位使用，不做任何处理-->
			<el-aside>
			</el-aside>
			<!--占位使用，不做任何处理-->
			<el-main></el-main>
			<el-aside >
				<!--搜索内容开始-->
				<el-row style="height: 17%;">
					<el-col :span="12" style="    margin-top: 12%; margin-left: 5%;">						
							<input type="text" autocomplete="off" placeholder="请输入内容" class="el-input__inner">						
					</el-col>
					<el-col :span="12"     style="margin-top: -12.8%;   margin-left: 59%;">
						
							<el-button type="primary" icon="el-icon-search">搜索</el-button>
						
					</el-col>
					
				</el-row>
			</el-aside>
			<!--占位使用，不做任何处理-->
			<el-aside>
			</el-aside>
			<!--占位使用，不做任何处理-->
		</el-container>
		<el-footer style="height:13%;"></el-footer>
	</el-container>
</template>
<style>
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
	.el-aside{
		    overflow: hidden;
	}
	body {
		background: #f6f6f6;
	}
</style>
<script>
	export default {
		data() {
			return {
				input: ''
			}
		}
	}
</script>