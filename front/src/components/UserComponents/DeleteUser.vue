<template>
  <div v-title data-title="用户注销">
    <UserNav></UserNav>
    <el-form rules="rules" ref="infoForm" :model="userd" label-width="120px">
      <el-form-item prop="passwordd">
        请输入您的密码：
        <input type="password" v-model="userd.passwordd"></input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="deleteUser">确认注销</el-button>
        <el-button type="danger" >我还不想走</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import UserNav from './UserCenter'
export default {
  name: 'DeleteUser',
  data () {
    return {
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
  methods: {
    deleteUser () {
      if (this.userd.passwordd == this.user.password) {
        this.$confirm('此操作将永久删除你的账户, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.$message({
            type: 'success',
            message: '删除成功!'
          })
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消删除'
          })
        })
      } else {
        this.$message({
          type: 'warning',
          message: '必须输入密码！'
        })
      }
    }
  }
}
</script>

<style scoped>
  .el-message-box {
    z-index: 2000;
  }
</style>
