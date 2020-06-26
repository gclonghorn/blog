<template>
  <div v-title data-title="浏览博客">
    <el-container style="margin-right:170px;margin-left:170px; margin-top:30px;">
      <el-aside width="350px">
        <AuthorInfo
          :author-id="author.id"
          :blog-id="BlogID"
          @changeLike="BlogMain(BlogID)"
          @reGetBlog="init"
          v-if="Author_flag"></AuthorInfo><!---->
      </el-aside>
      <el-container style="margin-left: 30px;" direction="vertical">
        <el-card style="background-color: #ffffff;">
          <div style="text-align:left;">{{Title}}</div>
          <div style="text-align:left;">发布日期：{{PostDate}}</div>
          <div style="text-align:left;">阅读量：{{readNumber}}</div>
          <div style="text-align:left;">点赞数：{{likeNumber}}</div>
          <div class="grid-content" style="text-align:right; overflow:visible;">
            <el-tag  style="margin-right: 8px;">{{tag.label}}</el-tag>
          </div>
        </el-card>
        <el-card style=" shadow:always;margin-top: 20px; margin-bottom: 20px;">
          <el-main style="background-color: #ffffff; text-align:left;">
<!--            <div class="ql-container ql-snow">-->
<!--              <div class="ql-editor">-->
<!--                <div v-html="contenthtml"></div>-->
<!--              </div>-->
<!--            </div>-->
<!--            <div ref="editor-read" class="text"></div>-->
              <div v-html="contenthtml"></div>

          </el-main>
        </el-card>
        <el-card style="text-align:left; background-color:#E9EEF3;" shadow="hover">
          评论区<br>
          </el-card>
        <div v-for="(item,index) in comments" :key="index">
          <Comment :comment="item" :BlogId="BlogID" @reGetBlog="init"></Comment>
        </div>
      </el-container>
    </el-container>

  </div>
</template>

<script>
import AuthorInfo from './AuthorInfo.vue'
import Comment from './Comment.vue'
import Page from './Page.vue'
import axiosInstance from '../../api/index'
import E from 'wangeditor'
import {isJSON} from '../../main'

export default{
  name: 'ViewMain',
  data () {
    return {
      BlogID: 300,
      Title: '',
      PostDate: '2019-07-03',
      author: {
        username: 'AUTHOR',
        head: 'https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png',
        id: '9'
      },
      commentSize: 10, // 评论条数
      pageSize: 10,
      readNumber: 30,
      likeNumber: 10,
      tag: {id: '1', label: 'java'},
      contenthtml: '<h2 class="ql-indent-1"><strong>文本编辑器</strong><a href="https://quilljs.com/" ' +
          'target="_blank"><strong>Quill</strong></a><strong>的介绍：</strong></h2><ol><li><span style="color: rgb(0, 102, 204);">' +
          'Quill</span>是一个免费开源文本API编辑器工具，帮助开发人员解决编辑问题。</li><li><span style="color: rgb(0, 102, 204);">' +
          'Quill</span>编辑器旨在通过自身的编辑模块提供强大的API来构建自定义式的编辑器。</li><li>最重要的是，' +
          '<span style="color: rgb(0, 102, 204);">Quill</span>没有规定样式，你可以自定义自己的编辑器以符合自己的使用需求。' +
          '</li><li><span style="color: rgb(0, 102, 204);">Quill</span>是一个轻量级的开源编辑器，拥有良好的可扩展构架和表现力出色的API' +
          '接口，标准化的HTML规则。</li><li><span style="color: rgb(0, 102, 204);">Quill</span>支持的浏览器有<strong class="ql-font-m' +
          'onospace">Firefox</strong>、<strong class="ql-font-monospace">Safari</strong>和<strong class="ql-font-monospace">IE9+</str' +
          'ong>、<strong class="ql-font-monospace">Chorme</strong>等。</li></ol>',
      comments: [
        {
          author: {
            username: 'ME',
            head: 'https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png',
            id: '2'
          },
          body: '<h1>TITLE</h1>',
          pub_date: '2020-09-78',
          replies: [
            {
              author: {
                username: 'YOU',
                head: 'https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png',
                id: '10'
              },
              body: '<Strong>REPLY</Strong>',
              pub_date: '2021-21-21',
              replies: null,
              reps: null
            },
            {
              author: {
                username: 'YOU',
                head: 'https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png',
                id: '10'
              },
              body: '<Strong>REPLY</Strong>',
              pub_date: '2021-21-21',
              replies: null,
              reps: null
            }
          ]
        },
        {
          author: {
            username: 'YOU',
            head: 'https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png',
            id: '17'
          },
          body: '<h1>TITLE</h1>',
          pub_date: '2020-09-78',
          replies: [
          ],
        }
      ],
      Author_flag: false,
      editor: null
    }
  },
  components: {
    AuthorInfo,
    Comment,
    Page,
  },
  methods: {
    BlogMain (BlogID) {
      this.comments = []
      const axios = axiosInstance
      axios.get('http://127.0.0.1:8000/list/' + BlogID).then(response => {
        if (response.status === 200) {
          console.log(response)
          this.Title = response.data.title
          this.PostDate = response.data.pub_date
          this.contenthtml = response.data.body
          this.commentSize = response.data.comments.length
          this.tag.label = response.data.category.name
          this.tag.id = response.data.category.id
          this.comments = response.data.comments // 循环赋值
          this.author = response.data.author
          this.likeNumber = response.data.like_num
          this.readNumber = response.data.read_num
          this.Author_flag = true
          console.log(this.contenthtml)
          if(isJSON(this.contenthtml)){
            this.contenthtml = JSON.parse(this.contenthtml)
          }
          console.log(this.contenthtml)
        } else {
          this.$message({
            message: '获取详情失败' + response.message,
            type: 'error'
          })
        }
      }).catch(error =>{
        if(error.response){
          console.log(error.response)
        }
      })
    },
    changePage (pageSize) {
      this.pageSize = pageSize
    },
    createEditor () {
      this.editor = new E(this.$refs.editor)
      this.editor.customConfig.zIndex = 100
      this.editor.create()
      this.editor.$textElem.attr('contenteditable', false)// 禁用编辑功能，在展示博文、展示评论时使用
    },
    init(){
      this.BlogID = this.$route.params.BlogId
      //this.$refs.BlogText.innerHTML = this.contenthtml
      this.BlogMain(this.BlogID)
      //this.createEditor()
    }
  },
  mounted () {
    this.init()
  },
}
</script>

<style>
  .el-header, .el-footer {
    background-color: #E9EEF3;
    color: #333;
    text-align: center;
    line-height: 50px;
    border-radius: 4px;
  }

  .el-aside {
    color: #333;
    line-height: 110%;
    text-align:center;
    padding: 20px;
  }

  .el-main {
    background-color: #E9EEF3;
    color: #333;
    text-align: center;
    line-height: 180%;
    border-radius: 4px;
    min-height: 70px;
  }

  body > .el-container {
    margin: 40px;
  }

  .el-container:nth-child(5) .el-aside,
  .el-container:nth-child(6) .el-aside {
    line-height: 260px;
  }

  .el-container:nth-child(7) .el-aside {
    line-height: 320px;
  }

  .el-row {
    margin-bottom: 20px;
    &:last-child {
      margin-bottom: 0;
    }
  }
  .el-col {
    border-radius: 4px;
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
    // border-radius: 4px;
    min-height: 36px;
    margin:0;
  }
  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }
  .w-e-toolbar{
    flex-wrap:wrap;
  }
</style>
