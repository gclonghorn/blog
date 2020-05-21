<template>
  <div v-title data-title="个人中心">
    <UserNav></UserNav>
    <el-col span="20">
      <el-main style="background-color: white; margin-right: 200px;">
        <el-row>
         <div class="block"><el-avatar shape="square" :size="100" :src="squareUrl"></el-avatar>
           <!--双击查看大图-->
         </div>
        </el-row>
        <el-row>{{UserName}}</el-row>
        <el-row>
            粉丝数：{{fansNum}}&#8195;&#8195;
            关注数：{{followsNum}}
        </el-row>
        <br>
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
import UserNav from './UserCenter'
export default {
  name: 'UserInfo',
  data () {
    return {
      squareUrl: '', // 图片地址 如 https://cube.elemecdn.com/9/c2/f0ee8a3c7c9638a54940382568c9dpng.png
      UserName: '',
      fansNum: undefined,
      followsNum: undefined,
      Intro: '', // 简介
      registerDate: '' // 注册日期
    }
  },
  components: {
    UserNav
  },
  created () {
    this.$http.get('http://localhost:8080/ssm_init/hi') // 填写后端实际网址
      .then(response => {
        console.log(response.data)
        this.squareUrl = response.data.squareUrl // 所有response后跟后端实际名称
        this.UserName = response.data.UserName
        this.fansNum = response.data.fansNum
        this.followsNum = response.data.followsNum
        this.Intro = response.data.Intro
        this.registerDate = response.data.registerDate
      })
      .catch(error => {
        console.log(error)
      })
  }
}
</script>

<style scoped>

</style>
