<template>
  <div v-title data-title="个人中心-修改信息">
    <UserNav></UserNav>
    <el-col span="20"><!-- v-if="rightUser"-->
      <el-main style="background-color: white; margin-right: 200px;">
        <el-form ref="infoForm" :model="user" :rules="rules" >
          <el-form-item prop="head">
            <el-row>点击图片即可修改头像<br>
             <el-upload
                class="avatar-uploader"
                action="false"
                ref="upload"
                :show-file-list="false"
                :on-success="handleAvatarSuccess"
                :auto-upload="false"
                :http-request="upload_head"
                :before-upload="beforeAvatarUpload">
                <img v-if="user.head" :src="user.head" class="avatar">
                <i v-else class="el-icon-plus avatar-uploader-icon"></i>
              </el-upload>
            </el-row>
          </el-form-item>
          <el-form-item label= "修改用户名" prop="UserName" style="margin-top: 15px; margin-left: 100px" >
              <el-input v-model="user.UserName" placeholder="请输入用户名" style="width: 400px;margin-right:150px"></el-input>
          </el-form-item>
          <br>
          <el-form-item label="修改手机号" prop="phonenumber"  style="margin-left: 100px">
            <el-input
                type="tel"
                placeholder="请输入手机号"
                v-model="user.phonenumber"
                show-word-limit
                style="width:400px; margin-right:150px"
              >
            </el-input>
          </el-form-item>
          <br>
          <el-form-item label="修改密码" prop="password1" style="margin-left: 100px">&nbsp;&nbsp;&nbsp;
              <el-input type="password" v-model="user.password1" placeholder="请输入密码" style="width: 400px; margin-right:150px">
              </el-input>
          </el-form-item>
          <br>
          <el-form-item label="确认密码" prop="password2" style="margin-left: 100px" :required="user.password1==''?false:true">
              <el-input type="password" v-model="user.password2" placeholder="确认密码" style="width: 400px;margin-right:150px">
              </el-input>
          </el-form-item>
          <br>
          <el-form-item label="修改邮箱"  prop="email" style="margin-left: 100px">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
              <el-input v-model="user.email" placeholder="请输入邮箱" style="width: 400px;margin-right:150px"></el-input>
          </el-form-item>
          <br>
          <el-form-item label="修改个性签名" prop="Intro" style="margin-left: 100px;">
              <el-input
                type="textarea"
                style="width: 400px;margin-right:150px"
                placeholder="请输入30字以内个性签名"
                maxlength="30"
                :autosize="{ minRows: 2, maxRows: 4}"
                v-model="user.Intro">
              </el-input>
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
import {changeUserInfo, getUserInfo} from '../../api/api'
import axiosInstance from '../../api'
export default {
  name: 'ChangeInfo',
  data () {
    let validatePwd2 = (rule, value, callback) => {
      if (value !== this.user.password1) {
        callback(new Error('两次密码输入不一致'))
      } else {
        callback()
      }
    }
    return {
      uploadurl: 'http://127.0.0.1:8000/users/',
      rightUser: true,
      user: {
        head: 'https://cube.elemecdn.com/9/c2/f0ee8a3c7c9638a54940382568c9dpng.png',
        UserName: '',
        phonenumber: '',
        fansNum: 13,
        followsNum: 70,
        Intro: '',
        registerDate: '2018-10-23',
        email: '',
        password1: '',
        password2: '',
        pswd: true,
        id: 0
      },
      rules: {
        UserName: [
          {required: false, message: '请输入用户名', trigger: 'blur'}
        ],
        phonenumber: [// 11位
          {required: false, message: '请输入手机号', trigger: 'blur'},
          {min: 11, max: 11, message: '手机号必须是11位', trigger: 'blur'}
        ],
        password1: [// 4位
          {required: false, message: '请输入密码', trigger: 'blur'},
          {min: 4, max: 18, message: '密码在4~18位之间', trigger: 'blur'}
        ],
        password2: [// 与上个相同
          {trigger: 'blur', validator: validatePwd2}
        ],
        email: [// 格式
          {required: false, message: '请输入邮箱', trigger: 'blur'},
          {pattern: /^[A-Za-z\d]+([-_.][A-Za-z\d]+)*@([A-Za-z\d]+[-.])+[A-Za-z\d]{3}$/, message: '请使用.com后缀邮箱', trigger: 'blur'}
        ]
      },
      formData: null,
    }
  },
  components: {
    UserNav
  },
  watch: {
  },
  methods: {
    onSubmit () {
      // this.$refs.infoForm.validate，这是表单验证
      this.$refs.upload.submit()// 提交图片
      console.log(this.user.head)
      let axios = axiosInstance
      this.$refs.infoForm.validate((valid) => {
        if (valid) {
          if (this.formData === null) {
            this.formData = new FormData()
          }
          this.formData.append('username', this.user.UserName)
          if(this.user.password1 !== ''){
            this.formData.append('password', this.user.password1)
          }
          this.formData.append('email', this.user.email)
          this.formData.append('introduction', this.user.Intro)
          axios.patch('http://127.0.0.1:8000/users/' + this.user.id + '/', this.formData).then(response => {
            if (response.status === 200) {
              console.log(response)
              this.$message({
                message: '修改信息成功',
                type: 'success'
              })
              this.user.UserName = response.data.username
              this.user.Intro = response.data.introduction
              this.user.registerDate = response.data.reg_date
              this.user.email = response.data.email
              this.user.id = response.data.id
              this.user.head = response.data.head
            } else {
              console.log(response)
              this.$message({
                message: '修改信息失败',
                type: 'error'
              })
            }
          }).catch(error =>{
            if(error.response){
              console.log(error.response)
            }
          })
        }
        // else {
        //   this.$message({
        //     message:'信息填写错误',
        //     type:'error'
        //   })
        // }
      })
    },
    upload_head(){
      console.log('uploading the head')
      this.formData = new FormData()
      console.log(this.headFile)
      this.formData.append('head', this.headFile)
    },
    handleAvatarSuccess (res, file) {
      this.user.head = URL.createObjectURL(file.raw)
      console.log(this.user.head)
    },
    beforeAvatarUpload (file) {
      const isJPG = /image/.test(file.type)
      const isLt2M = file.size / 1024 / 1024 < 2

      if (!isJPG) {
        this.$message({
          message: '上传文件只能是图片格式！',
          type: 'error'
        })
      }
      if (!isLt2M) {
        this.$message({
          message: '上传头像图片大小不能超过 2MB!',
          type: 'error'
        })
      }
      if(isJPG && isLt2M) {
        this.headFile = file
        console.log(this.headFile)
      }
      console.log(isJPG && isLt2M)
      return isJPG && isLt2M
    },
    getInfo () {
      getUserInfo().then(response => {
        if (response.status === 200) {
          console.log(response)
          this.user.UserName = response.data.username
          this.user.Intro = response.data.introduction
          this.user.registerDate = response.data.reg_date
          this.user.email = response.data.email
          this.user.id = response.data.id
          this.user.phonenumber = response.data.tel
          this.user.head = response.data.head
        } else {
          this.$message({
            message: '获取信息失败',
            type: 'error'
          })
        }
      }).catch(error => {
        console.log(error.response)
        this.$message({
          message:'获取信息失败', type:'error'
        })
      })
    },
    getUrl () {
      console.log(this.uploadurl + this.user.id + '/')
      return this.uploadurl + this.user.id + '/'
    }
  },
  mounted () {
    this.getInfo()
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
