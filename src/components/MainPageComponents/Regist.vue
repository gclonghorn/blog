<template>
  <div>
    <div style="display: flex;justify-content: center;margin-top: 50px">
      <el-card style="width: 400px">
        <div slot="header" class="clearfix">
          <span>注册</span>
        </div>
        <el-form ref="infoForm" :model="user" :rules="rules"  :validate-on-rule-change="true">
          <el-form-item label="手机号" prop="phonenumber">
            <el-input
                type="tel"
                placeholder="请输入手机号"
                v-model="user.phonenumber"
                show-word-limit
                style="width: 75%; float: right"
              >
            </el-input>
          </el-form-item>

          <el-form-item label="用户名" prop="username">
            <el-input
                placeholder="请输入用户名"
                v-model="user.username"
                maxlength="15"
                show-word-limit
                style="width: 75%; float: right"
              >
            </el-input>
          </el-form-item>

          <el-form-item label=" 邮箱" prop="email">
            <el-input
                type="email"
                placeholder="请输入邮箱"
                v-model="user.email"
                show-word-limit
                style="width: 75%; float: right"
              >
            </el-input>
          </el-form-item>

          <el-form-item label="密码" prop="password1">
            <el-input
                type="password"
                placeholder="请输入密码"
                v-model="user.password1"
                maxlength="20"
                show-word-limit
                style="width: 75%; float: right"
              >
            </el-input>
          </el-form-item>

          <el-form-item label="确认密码" prop="password2">
            <el-input
                type="password"
                placeholder="请再次输入密码"
                v-model="user.password2"
                maxlength="20"
                show-word-limit
                style="width: 75%; float: right"
              >
            </el-input>
          </el-form-item>

          <el-form-item prop="Intro">
            <el-row>
              个性签名：
              <el-input
                type="textarea"
                style="width: 270px; float: right"
                placeholder="请输入30字以内个性签名"
                maxlength="30"
                :autosize="{ minRows: 2, maxRows: 4}"
                v-model="user.Intro">
              </el-input>
            </el-row>
          </el-form-item>

          <el-form-item>
            <el-button type="primary" style="width: 100%"  @click="doRegister">注册</el-button>
            <tr><el-link type="primary" @click="toLogin" style="float: left">已有账号？点我注册</el-link></tr>
          </el-form-item>
        </el-form>
      </el-card>
    </div>
  </div>
</template>

<script>
import {postNewUser} from '../../api/api.js'
export default {
  data () {
    var validatePwd2 = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再次输入密码'))
      } else if (value !== this.user.password1) {
        callback(new Error('两次密码输入不一致'))
      } else {
        callback()
      }
    }
    return {
      user: {
        phonenumber: '',
        username: '',
        password1: '',
        password2: '',
        email: '',
        Intro: ''
      },
      rules: {
        phonenumber: [// 11位
          {required: true, message: '请输入手机号', trigger: 'blur'},
          {min: 11, max: 11, message: '手机号必须是11位', trigger: 'blur'}
        ],
        username: [// 可能重复
          {required: true, message: '请输入用户名', trigger: 'blur'}
        ],
        password1: [// 4位
          {required: true, message: '请输入密码', trigger: 'blur'},
          {min: 4, max: 18, message: '密码在4~18位之间', trigger: 'blur'}
        ],
        password2: [// 与上个相同
          {required: true, trigger: 'blur', validator: validatePwd2}
        ],
        email: [// 格式
          {required: false, message: '请输入邮箱', trigger: 'blur'},
          {pattern: /^[A-Za-z\d]+([-_.][A-Za-z\d]+)*@([A-Za-z\d]+[-.])+[A-Za-z\d]{3}$/, message: '请使用.com后缀邮箱', trigger: 'blur'}
        ]
      }
    }
  },

  methods: {
    doRegister () {
      this.$refs.infoForm.validate((valid) => {
        if (valid) {
          postNewUser(this.user.username, this.user.password1, this.user.password2, this.user.phonenumber, this.user.email)
            .then(response => {
              console.log(response)
              this.$message({
                message: '注册成功！',
                type: 'success'
              })
              this.$router.push({ path: '/Login' })
            }).catch(error => {
              console.log(error)
              if (error.response.status === 400) {
                this.$message({
                  message: '用户名已存在！',
                  type: 'error'
                })
              } else {
                this.$message({
                  message: '注册信息有误，请重新填写！',
                  type: 'error'
                })
              }
            })
        }
      })
    },
    toLogin(){
      this.$router.push({name:'Login'})
    }
  }
}
</script>
