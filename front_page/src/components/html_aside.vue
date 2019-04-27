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
        </div>
			</el-card>
		</div>
		<!--  站內搜索结束  -->


    <!--  文章归档  -->
		<div>
			<el-card id="article_zips" class="box-card" style="margin-top: 20%;height:100%;margin-left: 9%;width:84%; text-align: center;padding: 0px;">
      <ele-calendar
                  :render-content="renderContent"
                  :data="datedef"
                  :prop="prop"
            ></ele-calendar>
			</el-card>
		</div>
		<!--  文章归档  -->

	</div>
</template>

<script type="text/ecmascript-6">
	// 引入外部整理好的css文件
	import "@/css/html_aside.css"
    import eleCalendar from 'ele-calendar'
    import 'ele-calendar/dist/vue-calendar.css'
	export default {
		name: 'html_aside',
		data() {
			return{
                datedef:[
                    {"date":"2018-06-30","content":null,"cid":null},
                    {"date":"2018-06-26","content":null,"cid":null},
                ],
                prop:'date' //对应日期字段名
            }
		},
     components: {
            eleCalendar
        },
		methods: {
		  renderContent(h,parmas) {
            const loop = data =>{
              return (
                data.defvalue.value ? (<div><div>{data.defvalue.text}</div>
                <span  >备选项</span>
                </div>) : <div>{data.defvalue.text}</div>
              )
           }
           return (
            <div  style="min-height:60px;">
             {loop(parmas)}
            </div>
            );
             },
    },
	}
</script>
