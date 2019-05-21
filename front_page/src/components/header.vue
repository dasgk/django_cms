<template>
	<div>
		<el-row>
			<el-col :span="8">
				<img src=''>
			</el-col>

			<el-col :span="2.3" style="margin-left: -9%;margin-top: -0.3%;color:#FC326F;font-family:KaiTi">
				<a href="javascript:void(0)" @click="jump_index()" style="color:#FC326F;">
					<h1>一个被动向前码农的自述</h1></a>
			</el-col>
			<el-col :span="2.3" style="margin-left: 10%;margin-top: 1%;color:rgb(50, 112, 252);;font-family:KaiTi">
				<h3>记录点滴，慢慢成长</h3></el-col>

		</el-row>
		<el-row>

			<el-breadcrumb separator="/" style="margin-left: 10.2%;">				
				<el-breadcrumb-item v-for="breadcrumb in breadcrumb_list" >{{breadcrumb}}</el-breadcrumb-item>				
			</el-breadcrumb>
		</el-row>

	</div>

</template>

<script>
	import "@/css/header.css";
	var vue;
	export default {
		name: 'html_header',
		data() {
			return {
				restaurants: [],
				state1: '',
				state2: '',
				breadcrumb_list:['首页']
			};
		},
		created:function(){
			vue = this		
		},
		methods: {
			jump_index: function() {
				this.$root.databus.$emit('article_list', {})
			},
			querySearch(queryString, cb) {
				var restaurants = this.restaurants;
				var results = queryString ? restaurants.filter(this.createFilter(queryString)) : restaurants;
				// 调用 callback 返回建议列表的数据
				cb(results);
			},
			createFilter(queryString) {
				return(restaurant) => {
					return(restaurant.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0);
				};
			},
			loadAll() {
				return [{
						"value": "三全鲜食（北新泾店）",
						"address": "长宁区新渔路144号"
					},
					{
						"value": "南拳妈妈龙虾盖浇饭",
						"address": "普陀区金沙江路1699号鑫乐惠美食广场A13"
					}
				];
			},
			handleSelect(item) {
				console.log(item);
			},
			update_Breadcrumb: function() {

			}
		},
		mounted:function(){
			
			this.$root.databus.$on('breadcrumb_list', function(breadcrumb_list){
				vue.breadcrumb_list = breadcrumb_list				
			})
		}
	}
</script>