<template>
  <div id="menulist">
  <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect"
    background-color="#64C3F2" text-color="#FFFFFF" active-rext-color="#ffd04b" router="true">
    <el-avatar style="float: left; margin-top: 10px; margin-left: 5px">BA</el-avatar>
    <el-menu-item  index="/MainPage" style="margin-left: 10px"><i class="el-icon-house"></i>首页</el-menu-item>
    <el-menu-item index="/EditBlog" @click="toEditBlog"><i class="el-icon-circle-plus-outline"></i>编辑博文</el-menu-item>
    <el-menu-item style="margin-left: 130px">
      <input style="height: 25px; width: 300px" type='text' index="/SearchResult" placeholder="请输入搜索内容" v-model="keywords">
      <el-button style="margin-left:10px" size="mini" icon="el-icon-search" round @click="toSearchResult"
                                                                     @keyup.enter="toSearchResult"></el-button>
    </el-menu-item>
    <el-submenu style=" float: right; margin-right: 10px">
      <template slot="title">
        <el-button type="text" style="color: white" index="/UserCenter" @click="toUserInfo">{{username}}</el-button>
        <el-button circle style="padding: 0px; line-height: 0px; float:center" index="/UserCenter" @click="toUserInfo">
          <el-avatar :src="url" @click="toUserInfo"></el-avatar>
        </el-button>
      </template>
      <el-menu-item index="/UserCenter" @click="toUserInfo">个人信息</el-menu-item>
      <el-menu-item index="/UserCenter" @click="toBlogList">博文</el-menu-item>
<!--      <el-menu-item index="/UserCenter" @click="toLogIn">注册/登录</el-menu-item>-->
      <el-menu-item index="/MainPage" @click="toLogout">退出登录</el-menu-item><!--dialog v-if="Log" v-else-->
    </el-submenu>
  </el-menu>
  <div class="line"></div>
  </div>
</template>

<script>
import {getUserInfo} from '../../api/api'
export default {
  data () {
    return {
      keywords: 'a',
      activeIndex: '/MainPage',
      username: 'User',
      url: 'https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png',
      userId: 'User',
      RealUserId: '1',
      Log: this.$store.state.Authorization ? false:true
    }
  },
  watch: {
    '$store.state.Authorization': {
      handler (oldValue, newValue) {
        console.log(oldValue)
        console.log(newValue)
        if (newValue !== null || newValue !== '') {
          this.getInfo()
        }
      }
    }
  },
  updated () {
    this.Log = this.$store.state.Authorization ? false:true
  },
  methods: {
    getInfo () {
      getUserInfo().then(response => {
        console.log(response)
        if (response.status === 200) {
          this.username = response.data.username
          this.url = response.data.head
          this.RealUserId = response.data.id
          this.GLOBAL.user_id = this.RealUserId
          this.GLOBAL.username = this.username
          this.GLOBAL.token = this.$store.state.Authorization
        } else{
          this.username = '未登录'
          this.url = null
          this.RealUserId = null
        }
      }).catch(error => {
        console.log(error.response)
        if(error.response.status === 401){
          this.$message({
            message: error.response.detail,
            type: 'error'
          })
          this.username = '未登录'
          this.url = null
          this.RealUserId = null
        }
      })
    },
    handleSelect (key, keyPath) {
      console.log(key, keyPath)
      this.activeIndex = keyPath
    },
    toUserInfo () {
      this.$router.push({name: 'UserInfo', params: {UserId: this.username, RealUserId: this.RealUserId}})
    },
    toBlogList () {
      this.$router.push({name: 'UserBlog', params: {UserId: this.username, RealUserId: this.RealUserId}})
    },
    toLogIn () {
      this.$router.push({name: 'Login'})
    },
    toLogout () {
      // this.$router.push({name: 'Logout', params: {UserId: this.username, RealUserId: this.RealUserId}})
      let self = this
      this.$confirm('您确定要登出吗?', '退出登录', {
        confirmButtonText: '确定',
        cancelButtonText: '取消'
      }).then(() => {
        if(self.$store.state.Authorization === ''){
          this.$message({
            message:'尚未登录！', type:'error'
          })
          self.$router.push({path: '/MainPage'})
        }
        self.$store.commit('logOut').then(() => {
          this.GLOBAL.user_id = null
          this.GLOBAL.username = null
          this.GLOBAL.token = null
          self.$router.push({ path: '/' })
        }).catch(() => {
        })
      }).catch(() => {
      })
    },
    toEditBlog () {
      this.$router.push({name: 'EditBlog', params: {UserId: this.username}})
    },
    toSearchResult () {
      this.$router.push({path: '/SearchResult', query: {SearchId: this.username, keys: this.keywords}})
    }
  },
  mounted () {
    this.getInfo()
  },
  updated () {
    this.getInfo()
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
