<template>
  <div v-title data-title="个人中心-资源">
    <UserNav></UserNav>
    <el-container direction='vertical'>
      <el-main  style="margin-left: 250px;padding: 0px;">
      <div v-for="(file, index) in user.fileList" :key="index" style="margin: 10px;">
        <el-card class="box-card" shadow="hover">
          <div slot="header" class="clearfix">
            下载文件：<el-button type="plain" @click="download(file)">{{file.name}}</el-button>
            <el-button type="danger" @click="deleteFile(file.id)" v-if="rightUser">删除文件</el-button>
          </div>
          <div class="text item">
            {{file.pub_date}}
          </div>
        </el-card>
      </div></el-main>
    </el-container>
  </div>
</template>

<script>
import UserNav from './UserCenter'
import axiosInstance from '../../api'
export default {
  name: 'UploadedFiles',
  data () {
    return {
      // fileimgurl: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
      user: {
        fileList: []
      },
      RealUserId: 0,
      rightUser: true
    }
  },
  methods: {
    download (file) {
      let a = document.createElement('a')
      a.href = file.url
      a.download = file.name
      a.click()
    },
    getFiles () {
      const axios = axiosInstance
      this.user.fileList.length = 0
      axios.get('http://127.0.0.1:8000/files/', {params: {author: this.RealUserId}}).then(response => {
        if (response.status === 200) {
          console.log(response)
          this.user.fileList.length = 0
          if (response.data.count === 0) {
            this.user.fileList.length = 0
            return
          }
          response.data.results.forEach((j) => {
            // 执行代码
            let f = new Object({name: j.name, url: 'http://127.0.0.1:8000/download/' + j.name, pub_date: j.pub_date, id: j.id})
            // j.pub_date undefined
            this.user.fileList.push(f)
          })
          // 参数：value数组中的当前项, index当前项的索引, array原始数组；
          // 数组中有几项，那么传递进去的匿名回调函数就需要执行几次；
          console.log(this.user.fileList)
        }
      }).catch(error => {
        if (error.response) {
          console.log(error.response)
        }
      })
    },
    deleteFile (id) {
      const axios = axiosInstance
      axios.delete('http://127.0.0.1:8000/files/' + id).then(response => {
        if (response.status === 204) {
          this.$message({
            message: '删除成功！',
            type: 'success'
          })
          this.getFiles()
        } else {
          this.$message({
            message: '删除失败',
            type: 'error'
          })
        }
      }).catch(error => {
        if (error.response) {
          if (error.response.status === 404) {
            this.$message({
              message: '文件已删除，请刷新页面', type: 'error'
            })
          }
          console.log(error.response)
        }
      })
    }
  },
  components: {
    UserNav
  },
  mounted () {
    this.RealUserId = this.$route.params.RealUserId
    console.log(this.GLOBAL)
    if (this.RealUserId + '' === this.GLOBAL.user_id + '') {
      this.rightUser = true
    } else {
      this.rightUser = false
    }
    this.getFiles()
  }
}
</script>

<style scoped>
  .text {
    font-size: 14px;
  }

  .item {
    margin-bottom: 18px;
  }

  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }
  .clearfix:after {
    clear: both
  }

  .box-card {
    width: 480px;
  }
</style>
