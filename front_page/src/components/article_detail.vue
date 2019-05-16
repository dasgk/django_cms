<!--这里是文章详情-->
<template id="article_main" style="background-color: white;width:60%;overflow-x: hidden;overflow-y: hidden;">
  <div id="test-editormd">
    <textarea>
      ###点点滴滴
    </textarea>
  </div>
</template>

<script src="./js/editor.md-master/js/editormd.js"></script>
<link rel="stylesheet" type="text/css" href="./js/editor.md-master/css/editormd.css"/>
<script>
  import 'jquery'
  import "@/css/layout.css"
  import "@/js/editor.md-master/css/editormd.css"
  import "@/js/editor.md-master/editormd.min.js"
  import "@/js/editor.md-master/lib/marked.min.js"
  import "@/js/editor.md-master/lib/prettify.min.js"

  export default {

  }

  var testEditor;

  $(function () {
    editormd.markdownToHTML("test-editormd", {
      htmlDecode: "style,script,iframe", // you can filter tags decode
      emoji: true,
      taskList: true,
      tex: true, // 默认不解析

      sequenceDiagram: false, // 默认不解析
      marked: true, // 默认不解析
      path: './js/editor.md-master/lib'
    });

  });
</script>
