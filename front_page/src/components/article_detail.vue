<template>
  <div class="markdown-view-box">
    <link rel="stylesheet" href="/js/editor.md-master/css/editormd.min.css">
    <link rel="stylesheet" href="/js/editor.md-master/examples/css/style.css" />
    <link rel="stylesheet" href="/js/editor.md-master/css/editormd.preview.min.css" />
    <div id="markdown-view">
      <textarea style="display: none;">{{doc.content}}</textarea>
    </div>
  </div>
</template>
<script>






const defaultConfig = {
  width: "100%",
  height: 600,
  path: '/js/editor.md-master/lib/',
  // theme: 'dark',
  // previewTheme: 'dark',
  // editorTheme: 'pastel-on-dark',
  markdown: '',      // 默认填充内容
  lineWrapping: true, // 编辑框不换行
  codeFold: true,                 // 代码折叠
  placeholder: '请输入...',
  syncScrolling: true,
  saveHTMLToTextarea: true,       // 保存 HTML 到 Textarea
  searchReplace: true,
  watch: true,                                // 实时预览
  htmlDecode: "style,script,iframe|on*",      // 开启 HTML 标签解析，为了安全性，默认不开启
  toolbar: true,                  //工具栏
  previewCodeHighlight: true,     // 预览 HTML 的代码块高亮，默认开启
  emoji: true,
  taskList: true,
  tocm: true,                     // Using [TOCM]
  tex: true,                      // 开启科学公式TeX语言支持，默认关闭
  flowChart: true,                // 开启流程图支持，默认关闭
  sequenceDiagram: true,          // 开启时序/序列图支持，默认关闭,
  // dialogLockScreen: false,      // 设置弹出层对话框不锁屏，全局通用，默认为true
  // dialogShowMask: false,        // 设置弹出层对话框显示透明遮罩层，全局通用，默认为true
  // dialogDraggable: false,       // 设置弹出层对话框不可拖动，全局通用，默认为true
  // dialogMaskOpacity: 0.4,       // 设置透明遮罩层的透明度，全局通用，默认值为0.1
  // dialogMaskBgColor: "#000",    // 设置透明遮罩层的背景颜色，全局通用，默认为#fff
  // imageUpload: false,
  // imageFormats: ["jpg", "jpeg", "gif", "png", "bmp", "webp"],
  // imageUploadURL: "./php/upload.php",
  // onload: function() {
  //    // this.fullscreen();
  //    // this.unwatch();
  //    // this.watch().fullscreen();
  //    // this.setMarkdown("#PHP");
  //    // this.width("100%");
  //    // this.height(480);
  //    // this.resize("100%", 640);
  // },
};
export {
  defaultConfig,
};


  import scriptjs from 'scriptjs'
  export default {
    props: {
      viewId: {
        'type': String,
        'default': 'markdown-view'
      },
      config: { // 编辑器配置
        type: Object
      },
      initData: {
        'type': String
      },
      initDataDelay: {
        'type': Number, // 延迟初始化数据时间，单位毫秒
        'default': 0
      }
    },
    data: function () {
      return {
        doc: {'content':'dhqwiodhaiowdhlandklandkla'},
        editor: null
      }
    },
    methods: {
      fetchScript: function (url) {
        return new Promise((resolve) => {
          scriptjs(url, () => {
            resolve()
          })
        })
      },
      getDoc: function () {
        return this.doc
      },
      getConfig: function () {
        return { ...defaultConfig, ...this.config }
      },
      forceUpdate: function () {
        this.$forceUpdate()
      },
      initView: function () {
        (async () => {
          await this.fetchScript('/js/editor.md-master/jquery.min.js')
          await this.fetchScript('/js/editor.md-master/lib/marked.min.js')
          await this.fetchScript('/js/editor.md-master/lib/prettify.min.js')
          await this.fetchScript('/js/editor.md-master/lib/raphael.min.js')
          await this.fetchScript('/js/editor.md-master/lib/underscore.min.js')
          await this.fetchScript('/js/editor.md-master/lib/sequence-diagram.min.js')
          await this.fetchScript('/js/editor.md-master/lib/flowchart.min.js')
          await this.fetchScript('/js/editor.md-master/lib/jquery.flowchart.min.js')
          await this.fetchScript('/js/editor.md-master/editormd.min.js')
          this.$nextTick(() => {
            this.editor = window.editormd.markdownToHTML(this.viewId, this.getConfig())
          })
        })()
      },
      setDoc (doc) {
        if (doc) {
          let vm = this
          vm.doc = doc
          let markdownViewDiv = document.getElementById('markdown-view')
          if (markdownViewDiv) {
            markdownViewDiv.innerHTML = '<textarea style="display: none;"></textarea>'
            vm.initView()
            if (doc.content) {
              markdownViewDiv.getElementsByTagName('textarea')[0].innerHTML = doc.content
            }
          }
        }
      },
      showContent () {
        let vm = this
        vm.$store.state.editor.isEditing = true

        vm.doc = doc
        let markdownViewDiv = document.getElementById('markdown-view')
        markdownViewDiv.innerHTML = '<textarea style="display: none;"></textarea>'
        vm.initView()
        markdownViewDiv.getElementsByTagName('textarea')[0].innerHTML ="eqweqiohwnqldnkas"
    },
    mounted: function () {
      let vm = this
      vm.showContent()
    },
    created:function(){
     let vm = this
      vm.showContent(docId)
    }
  }
}
</script>
