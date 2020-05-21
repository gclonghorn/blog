<template>
  <div v-title data-title="浏览博客">
    <el-container style="margin-right:170px;margin-left:170px; margin-top:30px;">
      <el-aside width="350px">
        <AuthorInfo></AuthorInfo>
      </el-aside>
      <el-container style="margin-left: 30px;" direction="vertical">
        <el-card style="background-color: #ffffff;">
          <div style="text-align:left;">博文名称</div>
          <div style="text-align:left;">发布日期：{{PostDate}}</div>
          <div class="grid-content" style="text-align:right; overflow:visible;">
            <el-tag v-for="(tag,index) in tags" :key="index" style="margin-right: 8px;">{{tag.label}}</el-tag>
          </div>
        </el-card>
        <el-card style=" shadow:always;margin-top: 20px; margin-bottom: 20px;">
          <el-main style="background-color: #ffffff; text-align:left;">
            <div class="ql-container ql-snow">
              <div class="ql-editor">
                <div v-html="contenthtml"></div>
              </div>
            </div>
          </el-main>
        </el-card>
        <el-card style="text-align:left; background-color:#E9EEF3;" shadow="hover">
          评论区<br>
          <Page v-on:changePage="changePage"></Page>
        </el-card>
        <div v-for="o in pageSize" :key="o">
          <Comment></Comment>
        </div>
      </el-container>
    </el-container>

  </div>
</template>

<script>
import AuthorInfo from './AuthorInfo.vue'
import Comment from './Comment.vue'
import Page from './Page.vue'

export default{
  name: 'ViewMain',
  data () {
    return {
      PostDate: '2019-07-03',
      url: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
      pageSize: 10,
      tags: [
        {value: 'HTML', label: 'HTML'},
        {value: 'java', label: 'java'}
      ],
      contenthtml: '<h2 class="ql-indent-1"><strong>文本编辑器</strong><a href="https://quilljs.com/" ' +
          'target="_blank"><strong>Quill</strong></a><strong>的介绍：</strong></h2><ol><li><span style="color: rgb(0, 102, 204);">' +
          'Quill</span>是一个免费开源文本API编辑器工具，帮助开发人员解决编辑问题。</li><li><span style="color: rgb(0, 102, 204);">' +
          'Quill</span>编辑器旨在通过自身的编辑模块提供强大的API来构建自定义式的编辑器。</li><li>最重要的是，' +
          '<span style="color: rgb(0, 102, 204);">Quill</span>没有规定样式，你可以自定义自己的编辑器以符合自己的使用需求。' +
          '</li><li><span style="color: rgb(0, 102, 204);">Quill</span>是一个轻量级的开源编辑器，拥有良好的可扩展构架和表现力出色的API' +
          '接口，标准化的HTML规则。</li><li><span style="color: rgb(0, 102, 204);">Quill</span>支持的浏览器有<strong class="ql-font-m' +
          'onospace">Firefox</strong>、<strong class="ql-font-monospace">Safari</strong>和<strong class="ql-font-monospace">IE9+</str' +
          'ong>、<strong class="ql-font-monospace">Chorme</strong>等。</li></ol>'

    }
  },
  components: {
    AuthorInfo,
    Comment,
    Page
  },
  methods: {
    changePage (pageSize) {
      this.pageSize = pageSize
    }
  }
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
</style>
