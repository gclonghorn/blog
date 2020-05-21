<template>
    <el-card class="box-card">
    <div slot="header" class="clearfix">
      <el-button circle style="float: left; padding: 0px; line-height: 0px; border: 0px;" @click="toAuthorInfo">
        <el-avatar :src="imgUrl" :fit="'fill'"></el-avatar>
      </el-button>
      <el-button type="text"
               style="float: left; margin-top: 10px; margin-left: 10px" @click="toAuthorInfo">{{AuthorName}}</el-button>
      <span style="float: right; font-size: 14px; margin-top: 10px;">{{postDate}}</span>
      <el-button style="margin-top: 10px; padding: 3px 0" type="text" @click="viewmain">{{title}}</el-button>
      <el-tag type="info" size="medium" v-for="(tag,index) in tags" :key="index" style="margin-right: 8px;">
        {{tag.label}}
      </el-tag>
    </div>
  <div class="text item">
    {{simple}}
  </div>
</el-card>
</template>

<script>
export default{
  name: 'Card',
  data () {
    return {
      AuthorName: '', // User
      title: '', // Title
      simple: '', // 简介
      postDate: '', // 2019-2-1
      tags: [
        /* {value: 'HTML', label: 'HTML'},
        {value: 'java', label: 'java'}, */
      ],
      imgUrl: 'https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png',
    }
  },
  created () {
    this.$http.get('http://localhost:8080/ssm_init/hi') // 填写后端实际接口地址
      .then(response => {
        console.log(response.data)
        this.AuthorName = response.data.AuthorName // 所有response后跟后端实际名称
        this.title = response.data.title
        this.simple = response.data.simple
        this.postDate = response.data.postDate
        this.tags = response.data.tags
      })
      .catch(error => {
        console.log(error)
      })
  },
  methods: {
    viewmain () {
      this.$router.push({path: '/ViewMain'})
    },
    toAuthorInfo () {
      this.$router.push('/UserCenter/UserInfo')
    }
  }
}
</script>

<style>
  .text {
    font-size: 14px;
  }

  .item {
    margin-top: 10px;
  }

  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }
  .clearfix:after {
    clear: both
  }

  .box-card {
    float: left;
    margin-left: 25px;
    margin-right: 25px;
    margin-top: 15px;
    width: 900px;
  }
</style>
