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
         <el-menu-item @click="toUserInfo">个人信息</el-menu-item>
         <el-menu-item @click="toChangeInfo" v-if="this.$route.params.RealUserId+'' == this.GLOBAL.user_id+''">修改个人信息</el-menu-item>
         <el-menu-item @click="toDeleteUser" v-if="this.$route.params.RealUserId+'' == this.GLOBAL.user_id+''">注销账户</el-menu-item>
         <el-menu-item @click="toBlogList">博客列表</el-menu-item>
         <el-menu-item @click="toUploadedFiles">上传的资源</el-menu-item>
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
      userId: '1', // 用户名
      RealUserId: '0'
    }
  },
  watch: {// 用来每次重新输入关键词都可以重新查询
    '$route': {
      handler (route) {
        const that = this
        if (route.name === 'UserInfo') {
          this.RealUserId = this.$route.params.RealUserId
          if (this.RealUserId === this.GLOBAL.user_id) {
            this.user = true
          }
          console.log(this.GLOBAL.user_id+"~"+this.RealUserId+'~'+this.user)
        }
      },
      deep: true
    }
  },
  mounted () {
    this.RealUserId = this.$route.params.RealUserId
    if (this.RealUserId === this.GLOBAL.user_id) {
      this.user = true
    }
    console.log(this.GLOBAL.user_id+"~"+this.RealUserId+'~'+this.user)
  },
  methods: {
    handleOpen (key, keyPath) {
      console.log(key, keyPath)
    },
    handleClose (key, keyPath) {
      console.log(key, keyPath)
    },
    toBlogList () {
      this.$router.push({name: 'UserBlog', params: {UserId: this.userId, RealUserId: this.$route.params.RealUserId}})//
    },
    toUserInfo () {
      this.$router.push({name: 'UserInfo', params: {UserId: this.userId, RealUserId: this.$route.params.RealUserId}})
    },
    toChangeInfo () {
      this.$router.push({name: 'ChangeInfo', params: {UserId: this.userId, RealUserId: this.$route.params.RealUserId}})
    },
    toDeleteUser () {
      this.$router.push({name: 'DeleteUser', params: {UserId: this.userId, RealUserId: this.$route.params.RealUserId}})
    },
    toUploadedFiles () {
      this.$router.push({name: 'UploadedFiles', params: {UserId: this.userId, RealUserId: this.$route.params.RealUserId}})
    }
  },
  components: {
  }
}
</script>

<style scoped>

</style>
