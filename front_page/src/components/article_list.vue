<template>
	<el-container>
  <el-header style="height:145px">Header</el-header>
  <el-container>
    <el-aside width="200px" height="100%">Aside</el-aside>
    <el-main >Main</el-main>
  </el-container>
</el-container>
</template>
<script type="text/ecmascript-6">
  import "@/css/layout.css"
	import databus from "@/datacenterbus.js"

	import 'jquery'
	// 引入外部整理好的css文件

	var vue;
	export default({
		name: 'App',
		data(){
			return{

			}
		},
		created:function(){

		},
		components: {

		}
	})
</script>
