<template>
  <div v-title data-title="用户注销">
    <UserNav></UserNav>
        <el-button type="primary" @click="deleteUser">确认注销</el-button>
        <el-button type="danger" @click="toMainPage">我还不想走</el-button>
    <div>
      您不是本人，不可以注销！
    </div>
  </div>
</template>

<script>
import UserNav from './UserCenter'
import axiosInstance from '../../api'
import {getUserInfo} from '../../api/api'

export default {
  name: 'DeleteUser',
  data () {
    return {
      rightUser: true,
      user: {
        UserName: 'User',
        password: '12345'
      },
      userd: {
        passwordd: ''
      },
      rules: {
        passwordd: [
          {required: true, message: '必须输入密码', trigger: 'blur'}
        ]
      }
    }
  },
  components: {
    UserNav
  },
  mounted () {
    this.user.UserName = this.$route.params.UserId
    if (this.GLOBAL.username + '' === this.user.UserName + '') {
      this.rightUser = true
    } else this.rightUser = false
  },
  methods: {
    deleteUser () {
      this.$confirm('此操作将永久删除你的账户, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        let axios = axiosInstance
        axios.delete('http://127.0.0.1:8000/users/1').then(response => {
          console.log(response)
          if (response.status === 204) {
            this.$message({
              type: 'success',
              message: '删除成功!'
            })
            this.$router.push({path: '/MainPage'})
          }
        }).catch(error => {
          if (error.response) {
            console.log(error.response)
          }
        })
      }).catch((error) => {
        if (error.response) {
          console.log(error.response)
        }
        this.$message({
          type: 'info',
          message: '已取消删除'
        })
      })
    },
    toMainPage () {
      this.$router.push({path: '/MainPage'})
    }
  }
}
</script>

<style scoped>
  .el-message-box {
    z-index: 2000;
  }
</style>
