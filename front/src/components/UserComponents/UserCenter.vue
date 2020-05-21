<template>
  <div>
    <br><br><br>
    <el-col span="4">
     <el-menu
      default-active="2"
      class="el-menu-vertical-demo"
      @open="handleOpen"
      router
      :default-active="this.$route.path">
         <el-menu-item index="/UserCenter/UserInfo">个人信息</el-menu-item>
         <el-menu-item index="/UserCenter/ChangeInfo" v-if="user">修改个人信息</el-menu-item>
         <el-menu-item index="/UserCenter/DeleteUser" v-if="user">注销账户</el-menu-item>
         <el-menu-item index="/UserCenter/BlogList">博客列表</el-menu-item>
         <el-menu-item index="/UserCenter/UploadedFiles">上传的资源</el-menu-item>
     </el-menu>
    </el-col>
  </div>
</template>

<script>
export default {
  name: 'UserCenter',
  data () {
    return {
      activeIndex: '/UserCenter/UserInfo/',
      user: false,
      userId: 'User'
    }
  },
  mounted () {
    if (this.userId === 'User') {
      this.user = true
    }
  },
  methods: {
    handleOpen (key, keyPath) {
      console.log(key, keyPath)
    },
    handleClose (key, keyPath) {
      console.log(key, keyPath)
    }
  },
  components: {
  }
}
</script>

<style scoped>

</style>
