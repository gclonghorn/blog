<template>
  <div v-title data-title="个人中心">
    <UserNav></UserNav>
    <el-col span="20">
      <el-main style="background-color: white; margin-right: 200px;">
        <el-row>
         <div class="block"><el-avatar shape="square" :size="100" :src="head"></el-avatar>
           <!--双击查看大图-->
         </div>
        </el-row>
        <el-row>{{UserName}}</el-row>
        <el-row><el-button plain style="padding: 7px;" :disabled="ifFollowDisabled" @click="toFollow()">关注</el-button>
          <el-button plain style="padding: 7px;" :disabled="ifDisabled" @click="cancelFollow()">取消关注</el-button></el-row><br>
        <el-row>
            粉丝数：{{fansNum}}&#8195;&#8195;
            关注数：{{followsNum}}
        </el-row><br>
        <el-row>
          注册日期：{{registerDate}}
        </el-row>
        <br>
        <el-row>
          个性签名：
          <el-input
            type="textarea"
            readonly
            style="width: 400px;"
            :autosize="{ minRows: 2, maxRows: 4}"
            v-model="Intro">
          </el-input>
        </el-row>
      </el-main>
    </el-col>
  </div>
</template>

<script>
import {getUserInfo2, toFollow, getFollowInfo} from '../../api/api.js'
import axiosInstance from '../../api/index'
import UserNav from './UserCenter'
export default {
  name: 'UserInfo',
  data () {
    return {
      ifDisabled: true,
      ifFollowDisabled: false,
      followID: '',
      UserName: 'User',
      fansNum: 13,
      followsNum: 70,
      Intro: '这个人什么也没写~',
      registerDate: '2018-10-23',
      id: '1',
      head: 'https://cube.elemecdn.com/9/c2/f0ee8a3c7c9638a54940382568c9dpng.png',
    }
  },
  components: {
    UserNav
  },
  watch: {// 用来每次重新输入关键词都可以重新查询
    '$route': {
      handler (route) {
        const that = this
        if (route.name === 'UserInfo') {
          this.getInfo(this.$route.params.RealUserId)
        }
      },
      deep: true
    },
  },
  methods: {
    getInfo (id) {
      getUserInfo2(id).then(response => {
        if (response.status === 200) {
          console.log(response)
          let i = response.data[0]
          this.UserName = i.username
          this.fansNum = i.follower
          this.followsNum = i.subscriber
          this.Intro = i.introduction
          this.registerDate = i.reg_date
          this.head = i.head
          this.id = i.id
          console.log(this.UserName)
        } else {
          this.$message({
            message: '获取信息失败' + response.message,
            type: 'error'
          })
        }
      }).catch(error =>{
        if(error.response){
          console.log(error.response)
        }
      })
    },
    toFollow () {
      toFollow(this.id).then(response => {
        if (response.status === 201) {
          this.ifDisabled = false
          this.ifFollowDisabled = true
          this.followID = response.data.id
          this.$message({
            message: '关注成功', type: 'success'})
          this.getInfo(this.id)
        }
      }).catch(error => {
        if(error.response.status === 400){
          this.$message({
            message: '关注失败！',
            type: 'error'
          })
        }
      })
    },
    cancelFollow () {
      const axios = axiosInstance
      axios.delete('http://127.0.0.1:8000/userfavs/' + this.followID).then(response => {
        if (response.status === 204) {
          this.ifDisabled = true
          this.ifFollowDisabled = false
          this.$message({
            message: '取消关注成功', type: 'success'})
          this.getInfo(this.id)
        }
      }).catch(error => {
        if(error.response.status === 404){
          this.$message({
            message:'取消关注失败',
            type:'error'
          })
        }
      })
    },
    getFollow () {
      getFollowInfo().then(response => {
        console.log('getting follow in userinfo page')
        console.log(this.id)
        console.log(response)
        let sum = response.data.length
        let i = 0
        for (i = 0; i < sum; i++) {
          if (response.data[i].goods+'' === this.id+'') {
            this.ifFollowDisabled = true
            this.ifDisabled = false
            console.log(this.ifDisabled)
            this.followID = response.data[i].id
            break
          }
        }
      }).catch(error =>{
        if(error.response){
          console.log(error.response)
        }
      })
    }
  },
  mounted () {
    this.id = this.$route.params.RealUserId
    this.getInfo(this.id)
    this.getFollow()
  }
}
</script>

<style scoped>

</style>
