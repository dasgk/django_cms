<template>
	<div>
		<h4 name="a1" v-if="is_show" style="   text-align: left; line-height: 20px;font-size: 22px;">评论列表（{{comment_num}}）</h4>
		<div class="comments" style="line-height: 20px;" v-for="comment in comments">
			<div class="comment-wrap">
				<div class="photo">
					<div class="avatar" :style="{backgroundImage: 'url(' + comment.random_avatar+ ')'}"></div>
				</div>
				<div class="comment-block" style="text-align: left;">
					<p class="comment-text" style='font-family: "PT Sans", "Helvetica Neue", "Helvetica", "Roboto", "Arial", sans-serif;color: #555f77;-webkit-font-smoothing: antialiased;'>{{comment.content}}</p>
					<div class="bottom-comment">
						<div class="comment-date">{{comment.time}}</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script type="text/ecmascript-6">
	import axios from 'axios'
	import "@/request/request.js"
	import "@/css/comments.css"
	var vue;
	export default({
		name: 'App',
		data() {
			return {
				comments: [],
				is_show:0,
				comment_num:0
			}
		},
		methods: {

		},
		created: function() {
			vue = this
		},
		mounted: function() {
			vue.$root.databus.$on('comment_list', function(comments) {
				if(comments.length>0){
					vue.is_show = 1
					vue.comment_num = comments.length
				}
				vue.comments = comments
			});

		}
	})
</script>