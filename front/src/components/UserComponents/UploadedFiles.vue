<template>
  <div v-title data-title="个人中心-资源">
    <UserNav></UserNav>
    <div v-for="(file, index) in user.fileList" :key="index" style="margin: 10px;">
<!--      <el-avatar-->
<!--            shape="square"-->
<!--            :size="50"-->
<!--            :src="fileimgurl"-->
<!--            :fit="'fill'"></el-avatar>-->
      <el-button type="plain" @click="download(file)">{{file.name}}</el-button>
    </div>
  </div>
</template>

<script>
import UserNav from './UserCenter'
export default {
  name: 'UploadedFiles',
  data () {
    return {
      fileimgurl: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
      user: {
        fileList:
            [{// 只有文件1可以下载。图片1直接打开了；图片2找不到图片。
              name: '文件1.txt',
              url: '/static/a.txt'
            },
            {
              name: '图片1.png',
              url: 'https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png'
            },
            {
              name: '图片2.png',
              url: '@/assets/logo.png'
            }
            ]
      }
    }
  },
  methods: {
    download (file) {
      let a = document.createElement('a')
      a.href = file.url
      a.download = file.name
      a.click()
    }
  },
  components: {
    UserNav
  },
  created () {
    this.$http.get('http://localhost:8080/ssm_init/hi') // 填写后端实际网址
      .then(response => {
        console.log(response.data)
        this.fileList = response.data.fileList // 所有response后跟后端实际名称
      })
      .catch(error => {
        console.log(error)
      })
  }
}
</script>

<style scoped>

</style>
