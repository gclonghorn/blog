<template>
  <div v-title data-title="个人中心-修改信息">
    <UserNav></UserNav>
    <el-col span="20">
      <el-main style="background-color: white; margin-right: 200px;">
        <el-form ref="infoForm" :model="User" :rules="rules" >
          <el-form-item prop="url">
            <el-row>点击图片即可修改头像<br>
             <el-upload
                class="avatar-uploader"
                action="https://jsonplaceholder.typicode.com/posts/"
                :show-file-list="false"
                :on-success="handleAvatarSuccess"
                auto-upload="'false'"
                :before-upload="beforeAvatarUpload">
                <img v-if="user.url" :src="user.url" class="avatar">
                <i v-else class="el-icon-plus avatar-uploader-icon"></i>
              </el-upload>
            </el-row>
          </el-form-item>
          <el-form-item prop="UserName" style="margin-top: 15px;">
            <el-row>修改用户名:
              <el-input v-model="user.UserName" style="width: 220px;"></el-input>
            </el-row>
          </el-form-item>
          <br>
          <el-form-item prop="password1">
            <el-row>修改密码：
              <el-input type="password" v-model="user.passwordo" placeholder="请输入密码" style="width: 220px;">
              </el-input>
            </el-row>
          </el-form-item>
          <br>
          <el-form-item prop="password2">
            <el-row>确认密码：
              <el-input type="password" v-model="user.password2" placeholder="确认密码" style="width: 220px;">
              </el-input>
            </el-row>
          </el-form-item>
          <br>
          <el-form-item prop="email">
            <el-row>修改邮箱：
              <el-input v-model="user.email" placeholder="请输入邮箱" style="width: 220px;"></el-input>
            </el-row>
          </el-form-item>
          <br>
          <el-form-item prop="Intro">
            <el-row>
              修改个性签名：
              <el-input
                type="textarea"
                style="width: 400px;"
                :autosize="{ minRows: 2, maxRows: 4}"
                v-model="Intro">
              </el-input>
            </el-row>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="onSubmit">确认修改</el-button>
          </el-form-item>
        </el-form>
      </el-main>
    </el-col>
  </div>
</template>

<script>
import UserNav from './UserCenter'
export default {
  name: 'ChangeInfo',
  data () {
    return {
      user: {
        url: 'https://cube.elemecdn.com/9/c2/f0ee8a3c7c9638a54940382568c9dpng.png',
        UserName: 'User',
        fansNum: 13,
        followsNum: 70,
        Intro: '这个人什么也没写~',
        registerDate: '2018-10-23',
        email: '123@123.com',
        passwordo: '123',
        password1: '',
        password2: '',
        pswd: true
      },
      rules: {
        UserName: [
          {required: false, message: '在15个字符以内', trigger: 'blur'}
        ]
      }
    }
  },
  components: {
    UserNav
  },
  methods: {
    doLogin () {
      alert(JSON.stringify(this.user)) // 可以直接把this.user对象传给后端进行校验用户名和密码
    },
    onSubmit () {
      // 提交
      // this.$refs.infoForm.validate，这是表单验证
      this.$refs.upload.submit()// 提交图片
      this.$refs.infoForm.validate((valid) => {
        if (valid) {
          this.$post('m/add/about/us', this.infoForm).then(res => { // 后端
            if (res.errCode === 200) { // 修改了==
              this.$message({
                message: res.errMsg,
                type: 'success'
              })
              this.$router.push('/aboutus/aboutlist')
            } else {
              this.$message({
                message: res.errMsg,
                type: 'error'
              })
            }
          })
        }
      })
    },
    handleAvatarSuccess (res, file) {
      this.user.url = URL.createObjectURL(file.raw)
    },
    beforeAvatarUpload (file) {
      const isJPG = /image/.test(file.type)
      const isLt2M = file.size / 1024 / 1024 < 2

      if (!isJPG) {
        alert('上传头像图片只能是图片格式!')
      }
      if (!isLt2M) {
        alert('上传头像图片大小不能超过 2MB!')
      }
      return isJPG && isLt2M
    }
  }
}
</script>

<style scoped>
    .avatar-uploader .el-upload {
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
  }
  .avatar-uploader .el-upload:hover {
    border-color: #409EFF;
  }
  .avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 178px;
    height: 178px;
    line-height: 178px;
    text-align: center;
  }
  .avatar {
    width: 178px;
    height: 178px;
    display: block;
  }
  .el-message-box{
    z-index: 2000;
  }
</style>
