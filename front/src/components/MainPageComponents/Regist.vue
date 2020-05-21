<template>
  <div>
    <div style="display: flex;justify-content: center;margin-top: 150px">
      <el-card style="width: 400px">
        <div slot="header" class="clearfix">
          <span>注册</span>
        </div>
        <table>
          <tr>
            <td>手机号</td>
            <td>
              <el-input type="tel" v-model="user.phonenumber" placeholder="请输入手机号"></el-input>
            </td>
          </tr>
          <tr>
            <td>用户名</td>
            <td>
              <el-input v-model="user.username" placeholder="请输入用户名"></el-input>
            </td>
          </tr>
          <tr>
            <td>邮箱</td>
            <td>
              <el-input v-model="user.email" placeholder="请输入邮箱"></el-input>
            </td>
          </tr>
          <tr>
            <td>密码</td>
            <td>
              <el-input type="password" v-model="user.password1" placeholder="请输入密码" ></el-input>
            </td>
          </tr>
          <tr>
            <td>请确认密码</td>
            <td>
              <el-input type="password" v-model="user.password2" placeholder="请确认密码" @keydown.enter.native="doLogin"></el-input>
            </td>
          </tr>
          <tr>
           <!-- 占两行-->
            <td colspan="2">
              <el-button style="width: 350px" type="primary" @click="doRegist">注册</el-button>
            </td>
          </tr>
        </table>
      <!--  <el-form-item label="手机号" prop="phonenumber">
          <el-input type="tel" v-model="user.phonenumber" placeholder="请输入手机号"></el-input>
        </el-form-item>
        <el-form-item label="用户名" prop="username">
          <el-input v-model="user.username" placeholder="请输入用户名"></el-input>
        </el-form-item>
        <el-form-item label="邮箱" prop="email">
          <el-input type="email" v-model="user.email" placeholder="请输入邮箱"></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="password1">
          <el-input type="password" v-model="user.password1" placeholder="请输入密码" ></el-input>
        </el-form-item>
        <el-form-item label="请确认密码" prop="password2">
          <el-input type="password" v-model="user.password2" placeholder="请确认密码" @keydown.enter.native="doLogin"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button style="width: 350px" type="primary" @click="doLogin">注册</el-button> //
        </el-form-item> -->
      </el-card>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      user: {
        phonenumber: '',
        username: '',
        password1: '',
        password2: '',
        email: ''
      }
    }
  },
  methods: {
    doRegist () {
      alert(JSON.stringify(this.user)) // 可以直接把this.user对象传给后端进行校验用户名和密码
    }
  },
  mounted () { // 和doregist哪个可以？
    this.$axios({
      method: 'post',
      url: '/api/haveUser',
      headers: {
        'Content-type': 'application/x-www-form-urlencoded'
      },
      data: {
        phonenumber: this.phonenumber, // 后端实际名称
        username: this.username,
        password1: this.password1,
        password2: this.password2,
        email: this.email
      },
      transformRequest: [function (data) {
        let ret = ''
        for (let it in data) {
          ret += encodeURIComponent(it) + '=' + encodeURIComponent(data[it]) + '&'
        }
        return ret
      }]
    }).then((res) => {
      console.log(res.data)
    })
  }
}
</script>
