<template>
	<div>
		<el-row>
			<el-col :span="8"><img src="@/images/index.png" alt="猪宝宝" style="width:50px;height:50px;margin-right: -41%;margin-bottom: 55px;"></el-col>
			<el-col :span="5" style="margin-left: 10%;margin-top: -0.2%;color:#FC326F;font-family:KaiTi">
				<h1>记录点滴，成就不凡</h1></el-col>
			<el-col :span="5">
				<el-row class="demo-autocomplete" style="margin-top: 1.6%;">
					<el-col :span="12">
						<el-autocomplete class="inline-input" v-model="state1" :fetch-suggestions="querySearch" placeholder="请输入内容" @select="handleSelect">
							<i slot="suffix" class="el-input__icon el-icon-search"></i>
						</el-autocomplete>
					</el-col>
				</el-row>
			</el-col>
		</el-row>
	</div>
</template>

<style>
	.el-row {
		margin-bottom: 20px;
		&:last-child {
			margin-bottom: 0;
		}
	}
	
	.el-input__inner {
		border-radius: 30px
	}
	
	.el-header {
		line-height: 18px;
	}
	
	.el-col {
		border-radius: 4px;
		height: 63px;
	}
	
	.bg-purple-dark {
		background: #99a9bf;
	}
	
	.bg-purple {
		background: #d3dce6;
	}
	
	.bg-purple-light {
		background: #e5e9f2;
	}
	
	.grid-content {
		border-radius: 4px;
		min-height: 36px;
	}
	
	.row-bg {
		padding: 10px 0;
		background-color: #f9fafc;
	}
</style>

<script>
	export default {
		name: 'html_header',
		data() {
			return {
				restaurants: [],
				state1: '',
				state2: ''
			};
		},
		methods: {
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
			}
		},
		mounted() {
			this.restaurants = this.loadAll();
		}

	}
</script>