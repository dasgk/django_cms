<template>
	<div>
		<!--  站內搜索开始  -->
		<div>
			<el-card id="search_in_site" class="box-card" style="margin-top: 20%;margin-left: 9%;width:84%; text-align: center;">
				<div slot="header" class="clearfix">
					<span style="text-align:center">站内搜索</span>
				</div>
				<div style=" width:60%; margin-top: -3%;margin-right: auto;margin-bottom: 0px;margin-left: auto;">
					<el-input class="inline-input" id='input_search_in_site' placeholder="请输入内容">
						<i slot="suffix" class="el-input__icon el-icon-search"></i>
					</el-input>
				</div>
			</el-card>
		</div>
		<!--  站內搜索结束  -->

		<!--  站內搜索开始  -->
		<div>
			<el-card id="label_all_in_site" class="box-card" style="margin-top: 20%;margin-left: 9%;width:84%; text-align: center;">
				<div slot="header" class="clearfix">
					<span style="text-align:center">标签聚合</span>
				</div>
				<div style=" width:87%;" class="tag_clouds">
					<a href="https://www.qdtalk.com/tag/%e6%9e%84%e9%80%a0%e5%87%bd%e6%95%b0/" class="tag-cloud-link tag-link-48 tag-link-position-1" style="font-size: 14px;">构造函数</a>
<a href="https://www.qdtalk.com/tag/%e4%bd%9c%e7%94%a8%e5%9f%9f/" class="tag-cloud-link tag-link-59 tag-link-position-2" style="font-size: 14px;">作用域</a>
<a href="https://www.qdtalk.com/tag/%e5%8e%9f%e5%9e%8b/" class="tag-cloud-link tag-link-47 tag-link-position-3" style="font-size: 14px;">原型</a>
<a href="https://www.qdtalk.com/tag/%e9%9d%a2%e8%af%95/" class="tag-cloud-link tag-link-49 tag-link-position-4" style="font-size: 14px;">面试</a>
<a href="https://www.qdtalk.com/tag/css/" class="tag-cloud-link tag-link-11 tag-link-position-5" style="font-size: 14px;">css</a>
<a href="https://www.qdtalk.com/tag/%e5%89%8d%e7%ab%af/" class="tag-cloud-link tag-link-31 tag-link-position-6" style="font-size: 14px;">前端</a>
<a href="https://www.qdtalk.com/tag/javascript/" class="tag-cloud-link tag-link-10 tag-link-position-7" style="font-size: 14px;">javascript</a>
<a href="https://www.qdtalk.com/tag/%e8%a7%84%e8%8c%83/" class="tag-cloud-link tag-link-40 tag-link-position-8" style="font-size: 14px;">规范</a>
<a href="https://www.qdtalk.com/tag/vue/" class="tag-cloud-link tag-link-34 tag-link-position-9" style="font-size: 14px;">vue</a>
<a href="https://www.qdtalk.com/tag/%e9%9a%8f%e7%ac%94/" class="tag-cloud-link tag-link-38 tag-link-position-10" style="font-size: 14px;">随笔</a>
<a href="https://www.qdtalk.com/tag/webpack/" class="tag-cloud-link tag-link-44 tag-link-position-11" style="font-size: 14px;">webpack</a>
<a href="https://www.qdtalk.com/tag/gongju/" class="tag-cloud-link tag-link-12 tag-link-position-12" style="font-size: 14px;">工具</a>
<a href="https://www.qdtalk.com/tag/%e5%af%b9%e8%b1%a1/" class="tag-cloud-link tag-link-56 tag-link-position-13" style="font-size: 14px;">对象</a>
<a href="https://www.qdtalk.com/tag/%e7%86%8a%e7%8c%ab%e7%ac%94%e8%ae%b0/" class="tag-cloud-link tag-link-28 tag-link-position-14" style="font-size: 14px;">熊猫笔记</a>
<a href="https://www.qdtalk.com/tag/%e9%98%85%e8%af%bb%e6%84%9f%e6%82%9f/" class="tag-cloud-link tag-link-30 tag-link-position-15" style="font-size: 14px;">阅读感悟</a>
<a href="https://www.qdtalk.com/tag/this/" class="tag-cloud-link tag-link-60 tag-link-position-16" style="font-size: 14px;">this</a>
<a href="https://www.qdtalk.com/tag/%e6%ad%a3%e5%88%99/" class="tag-cloud-link tag-link-54 tag-link-position-17" style="font-size: 14px;">正则</a>
<a href="https://www.qdtalk.com/tag/es6/" class="tag-cloud-link tag-link-45 tag-link-position-18" style="font-size: 14px;">es6</a>
<a href="https://www.qdtalk.com/tag/%e6%8e%92%e5%ba%8f/" class="tag-cloud-link tag-link-55 tag-link-position-19" style="font-size: 14px;">排序</a>
<a href="https://www.qdtalk.com/tag/%e5%bc%82%e6%ad%a5/" class="tag-cloud-link tag-link-57 tag-link-position-20" style="font-size: 14px;">异步</a></div>
				
			</el-card>
		</div>
		<!--  站內搜索结束  -->

	</div>
</template>

<script type="text/ecmascript-6">
	// 引入外部整理好的css文件
	import "@/css/html_aside.css"
	import databus from "@/datacenterbus.js"
	var vue
	export default {
		name: 'html_aside',
		data() {
			return {};
		},
		methods: {}

	}
</script>
