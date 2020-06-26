<template>
  <div>
    <!--flex弹性盒子模型，justify-content：主抽 -->
    <div style="display: flex;justify-content: center;margin-top: 150px">
      <el-card style="width: 400px">
        <div slot="header" class="clearfix">
          <span>登录</span>
        </div>
        <!--<table>
          <tr>
            <td>用户名</td>
            <td>
              <el-input v-model="user.username" placeholder="请输入用户名"></el-input>
            </td>
          </tr>
          <tr>
            <td>密码</td>
            <td>
              <el-input type="password" v-model="user.password" placeholder="请输入密码" @keydown.enter.native="doLogin"></el-input>
              @keydown.enter.native="doLogin"当按下enter键的时候也会执行doLogin方法-->
            <!--</td>
          </tr>
          <tr>
            <td colspan="2">
              <el-button style="width: 350px" type="primary" @click="doLogin">登录</el-button>
            </td>
          </tr>
          <tr><el-link type="primary" @click="toRegist">没有账号？请先注册</el-link></tr>
        </table>-->
        <el-form ref="infoForm" :model="user" :rules="rules"  enctype="multipart/form-data">
          <el-form-item label="用户名" prop="username">
            <el-input
                placeholder="请输入用户名"
                v-model="user.username"
                show-word-limit
                style="width: 80%; float: right"
              >
            </el-input>
          </el-form-item>

          <el-form-item label="密码  " prop="password">
            <el-input
                type="password"
                placeholder="请输入密码"
                v-model="user.password"
                show-word-limit
                style="width: 80%; float: right"
                @keydown.enter.native="doLogin"
              >
            </el-input>
          </el-form-item>

          <el-form-item>
            <el-button type="primary" @click="doLogin" style="width: 100%">登录</el-button>
            <tr><el-link type="primary" @click="toRegist" style="float: left">没有账号？请先注册</el-link></tr>
          </el-form-item>
        </el-form>
      </el-card>
    </div>
  </div>
</template>

<script>
import {postUser} from '../../api/api.js'
import {mapMutations} from 'vuex'
export default {
  data () {
    return {
      user: {
        username: '',
        password: ''
      },
      userToken: '',
      rules: {
        username: [
          {required: true, message: '请输入用户名', trigger: 'blur'}
        ],
        password: [
          {required: true, message: '请输入密码', trigger: 'blur'}
        ]
      }
    }
  },

  mounted () {
    console.log('login mounted____________________')
  },
  methods: {
    ...mapMutations(['changeLogin']),
    doLogin () {
      this.$refs.infoForm.validate((valid) => {
        if (valid) {
          let _this = this
          postUser(_this.user.username, _this.user.password)
            .then(response => {
              if (response.status === 200) {
                console.log(response)
                localStorage.setItem('user_id', response.data.user_id)
                localStorage.setItem('username', response.data.username)
                localStorage.setItem('token', response.token)
                this.GLOBAL.username = localStorage.getItem('username')
                this.GLOBAL.user_id = localStorage.getItem('user_id')
                this.GLOBAL.token = localStorage.getItem('token')
                console.log(this.GLOBAL)
                console.log(localStorage.getItem('user_id'))
                console.log(response.data)
                this.$message({
                  message: '登录成功',
                  type: 'success'
                })
                _this.userToken = 'JWT ' + response.data.token
                _this.changeLogin({Authorization: _this.userToken})
                _this.$router.push({ path: this.$route.params.redirect || '/MainPage' })
              } else {
                console.log(response)
              }
            }).catch(error => {
            console.log(error)
            if(error.response){
              if(error.response.status === 400){
                this.$message({
                  message: '用户名或密码错误',
                  type: 'error'
                })
              }
            }
          })
        }
      })
    },
    toRegist () {
      this.$router.push({ path: '/Register' })
    }
  }
}
</script>
