<template>
	<el-container style="height:100%">
		<el-header style="height:63px;background-color: white;">
			<!-- 页面头部 -->

			<html_header></html_header>
			<!-- 页面头部结束 -->
		</el-header>


		<el-container style="height:100%">
			<!--占位使用-->
			<el-aside height="100%" style="background-color: white;;width:10%"></el-aside>
			<!-- 占位结束 -->


			<!--这里是文章详情-->
			<el-main style="background-color: white;width:60%">
         <div id="test-editormd">

        <textarea style="display:none;">
        1. 测试文件
        </textarea>
         </div>

			</el-main>
			<!----  文章详情结束  -->

			<el-aside  style="width:25%;background-color: white;">


				<!--这里是侧边栏-->
				<html_aside></html_aside>
        <!---    npm install ele-calendar  -->
				<!-- 这里是侧边栏 -->


			</el-aside>
			<!--占位使用-->
			<el-aside  height="100%" style="width:8%;background-color: white;">
    	</el-aside>
    	<!-- 占位结束 -->

		</el-container>
	</el-container>
</template>

<script>
  import "@/css/layout.css"
  import "@/js/editor.md-master/css/editormd.css"
  import "@/js/editor.md-master/editormd.js"
  import html_header from "@/components/header"
	import html_aside from "@/components/html_aside"
	import 'jquery'
  export default {
    components: {
			html_header: html_header,
			html_aside: html_aside,
		}
  }

  var testEditor;
  $(function() {

    editormd.markdownToHTML("test-editormd", {
            htmlDecode      : "style,script,iframe",  // you can filter tags decode
            emoji           : true,
            taskList        : true,
            tex             : true,  // 默认不解析
            flowChart       : true,  // 默认不解析
            sequenceDiagram : true,  // 默认不解析
            path:'./js/editor.md-master/lib'
        });
  });
</script>
