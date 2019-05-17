<template>
  <div>
    <el-card class="box-card" v-for="article in article_list">
      <div class="article_list_img">
        <img :src="article.cate_url"/>
      </div>
      <div class='article_list_relative_info'>

        <div class="article_title">

          <!--   这是文章所属分类 -->
          <a class="label" href="javascript:void(0)" @click="get_article_list_by_cate_id(article.cate_id)"> <span>{{article.cate_title}}</span>
            <i class="label-arrow"></i></a>
          <!--   这是文章所属分类 结束-->

          <!---  文章标题   -->
          <h2>
            <a href="javascript:void(0)" @click="jump(article.article_id)">{{article.title}}</a>
          </h2>
          <!---  文章标题    结束--->

        </div>

        <!---  文章摘要  -->
        <div class="article_abstract">
          <p>
            {{article.content}}
          </p>
        </div>
        <!---  文章摘要    结束--->
      </div>

      <!---  文章元數據信息  開始--->
      <div class="article_num_info">

				<span class="visible-lg visible-md visible-sm pull-left">
					<a href="javascript:void(0)" @click="get_article_list_by_post_date(article.updated_at)">
						<i class="el-icon-date"></i>{{article.updated_at}}</a>
						&nbsp;&nbsp;&nbsp;&nbsp;
					<a href="javascript:void(0)" @click="jump(article.article_id)">
						<i class="el-icon-upload"></i> {{article.comment_num}}条评论</a>
					</span>

        <span class="pull-left">
						&nbsp;&nbsp;&nbsp;&nbsp;
					<a href="javascript:void(0)">
						<i class="el-icon-view"></i>{{article.look_num}}次阅读</a>
						&nbsp;&nbsp;&nbsp;&nbsp;
					<a href="javascript:void(0)">
						<i class="el-icon-star-on"></i> {{article.like_num}}人点赞</a>
		</span>
        <span class="pull-right">
			<a class="read-more" href="javascript:void(0)" @click="jump(article.article_id)" title="阅读全文">阅读全文	<i
        class="el-icon-caret-right"></i></a>
			
		</span>

      </div>
      <!---  文章元數據信息  結束--->
    </el-card>

  </div>
</template>
<script type="text/ecmascript-6">
  import "@/css/article_list.css"
  import axios from 'axios'
  import "@/request/request.js"

  var vue;
  export default ({
    name: 'App',
    data() {
      return {
        article_list: []
      }
    },
    methods: {
      jump: function (article_id) {
        //设置当前显示的文章ID，隐藏列表
        this.$root.databus.$emit('current_article_id', article_id);
      },
      //获得特定类别的文章列表
      get_article_list_by_cate_id: function (cate_id) {
        //获得特定类别的文章列表
        axios.get('/article_list', {
          params: {
            'cate_id': cate_id
          }
        }).then((response) => {
          this.article_list = response.data.data

        }).catch(function (response) {
          console.log(response); //发生错误时执行的代码
        });
      },
      //获得特定日期发表的文章列表
      get_article_list_by_post_date: function (time) {
        var post_date = time.substr(0, 10)
        //获得特定类别的文章列表
        axios.get('/article_list', {
          params: {
            'post_date': post_date
          }
        }).then((response) => {
          this.article_list = response.data.data

        }).catch(function (response) {
          console.log(response); //发生错误时执行的代码
        });
      }
    },
    created: function () {
      vue = this
      axios.get('/article_list').then((response) => {
        this.article_list = response.data.data

      }).catch(function (response) {
        console.log(response); //发生错误时执行的代码
      });

      this.$root.databus.$on('article_reset', function (newval) {
        if (newval == 1) {
          axios.get('/article_list').then((response) => {
            this.article_list = response.data.data
          }).catch(function (response) {
            console.log(response); //发生错误时执行的代码
          });
          //显示文章列表
          vue.$root.databus.$emit('article_list_show', 1)
          vue.$root.databus.$emit('article_detail_show', 0)

        }
      });
    },
    mounted: function () {

    }

  })
</script>
