<template>
  <div id="menulist">
  <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect"
    background-color="#64C3F2" text-color="#FFFFFF" active-rext-color="#ffd04b" router="true">
    <el-avatar style="float: left; margin-top: 10px; margin-left: 5px">BA</el-avatar>
    <el-menu-item  index="/MainPage" style="margin-left: 10px"><i class="el-icon-house"></i>首页</el-menu-item>
    <el-menu-item index="/EditBlog"><i class="el-icon-circle-plus-outline"></i>编辑博文</el-menu-item>
    <el-menu-item index="/SearchResult" style="margin-left: 130px">
      <input style="height: 25px; width: 300px" type='text' placeholder="请输入搜索内容">
      <el-button style="margin-left:10px" size="mini" icon="el-icon-search" round></el-button>
    </el-menu-item>
    <el-submenu index="/UserCenter" style=" float: right; margin-right: 10px">
      <template slot="title">
        <el-button type="text" style="color: white" @click="toCenter">{{userId}}</el-button>
<!-- style="float: right; margin-top: 25px; margin-right: 10px"-->
<!--<el-avatar style="float: right; margin-top: 10px; margin-right: 10px"-->
        <el-button circle style="padding: 0px; line-height: 0px;" @click="toCenter">
          <el-avatar :src="url"></el-avatar>
        </el-button>
      </template>
      <el-menu-item index="/UserCenter/UserInfo">个人信息</el-menu-item>
      <el-menu-item index="/UserCenter/BlogList">博文</el-menu-item>
      <el-menu-item index="/Logout">退出登录</el-menu-item><!--dialog-->
    </el-submenu>
  </el-menu>
  <div class="line"></div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      activeIndex: '/' + this.$route.path.indexOf('/', 1),
      userId: '', // User
      url: '' // 图片网址 https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png
    }
  },
  methods: {
    handleSelect (key, keyPath) {
      console.log(key, keyPath)
    },
    toCenter () {
      this.$router.push({ path: '/UserCenter/UserInfo'})
    }
  },
  created () {
    this.$http.get('http://localhost:8080/ssm_init/hi') // 填写后端实际网址
      .then(response => {
        console.log(response.data)
        this.userId = response.data.userId // 所有response后跟后端实际名称
        this.url = response.data.url
      })
      .catch(error => {
        console.log(error)
      })
  }
}
</script>

<style>
#menulist {
  position: fixed;
  top: 0px;
  width: 100%;
  z-index: 999;
}
</style>
