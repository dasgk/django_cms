<template>
	<el-menu class="el-menu-demo" mode="horizontal">
		<el-menu-item index="1">文章数80篇；评论20条</el-menu-item>		
	</el-menu>
</template>
<style>
	.el-menu.el-menu--horizontal{
		margin-left:79%;
		border-bottom: solid 0px #e6e6e6;
	}
	.el-menu--horizontal>.el-menu-item.is-active{
		
		border-bottom: solid 0px #e6e6e6;	
	}
</style>
<script>
	export default {
		name: 'navigate',
		data() {
			return {
				activeIndex: '1',				
			};
		},		
	}
</script>