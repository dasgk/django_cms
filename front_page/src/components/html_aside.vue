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
		
		
    	<!--  文章分类  -->
		<div>
			<el-card id="label_all_in_site" class="box-card" style="margin-top: 20%;margin-left: 9%;width:84%; text-align: center;">
				<div slot="header" class="clearfix">
					<span style="text-align:center">个人分类</span>
				</div>
				<div style=" width:87%;line-height: 50x;;" class="tag_clouds"  v-for="cate in cate_list">
					<el-row>
  						<el-col style="height: 50px;" :span="24" @click="article_list_by_cate(cate.cate_id)">
  							<div class="grid-content"  style="float: left;">
  								<img :src="cate.cate_img_url" style="width:50px;height:50px"/>
  							</div>
  							<div @click="article_list_by_cate(cate.cate_id,cate.title)" style="cursor:pointer;margin-left: 5px;float: left; margin-top: 23px;;"class="grid-content">{{cate.title}}</div>
  							
  						<div style="float: right;margin-top: 25px;color: gray; font-size: 13PX;"class="grid-content">文章{{cate.article_count}}篇,访问量{{cate.look_num}}</div></el-col>
					</el-row>					
        		</div>
			</el-card>
		</div>
		<!-- 文章分类 -->
		

		<!--  站內搜索开始  -->
		<div>
			<el-card id="label_all_in_site" class="box-card" style="margin-top: 20%;margin-left: 9%;width:84%; text-align: center;">
				<div slot="header" class="clearfix">
					<span style="text-align:center">标签聚合</span>
				</div>
				<div style=" width:87%;" class="tag_clouds"  v-for="label in label_list">
				<a href="javascript:void(0)" @click="article_list_by_label(label.label_id, label.title)" class="tag-cloud-link tag-link-48 tag-link-position-1" style="text-decoration:none;font-size: 14px;">{{label.title}}</a>
        </div>
			</el-card>
		</div>
		<!--  站內搜索结束  -->


	</div>
</template>

<script type="text/ecmascript-6">
	// 引入外部整理好的css文件	
	import "@/css/html_aside.css"    
    import axios from 'axios'
	export default {
		name: 'html_aside',
		data() {
			return{                
                label_list:[],
                cate_list:[]
            }
		},     
        created:function(){
        	axios.get('/label_list').then((response) => {
				this.label_list = response.data.data
				}).catch(function(response) {
					console.log(response); //发生错误时执行的代码
				});
			axios.get('/cate_list').then((response) => {
					this.cate_list = response.data.data

				}).catch(function(response) {
					console.log(response); //发生错误时执行的代码
				});
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
           article_list_by_cate:function(cate_id,title){
           	this.$root.databus.$emit('breadcrumb_list', ['首页',"'"+title+"'相关文章"]);
           		this.$root.databus.$emit('article_list', {'cate_id':cate_id})
           },
           article_list_by_label:function(label_id,title){
           	this.$root.databus.$emit('breadcrumb_list', ['首页',"'"+title+"'相关文章"]);
           		this.$root.databus.$emit('article_list', {'label_id':label_id})
           },
    },
	}
</script>
