<template>
    <div  v-title data-title="个人中心-博客">
      <UserNav></UserNav>
      <el-col span="20">
        <el-row>
          <div v-for="o in pageSize" :key="o">
              <my-card></my-card>
              <div v-if="rightUser">
                <el-button type="danger" @click=""
                           style="margin-top: 75px; margin-bottom: 75px;">删除博客</el-button>
              </div>
          </div>
        </el-row>
        <br>
        <el-row>
          <Page @changePage="changePage" style="margin-right: 300px;"></Page>
        </el-row>
      </el-col>
    </div>
</template>

<script>
import myCard from '../SearchComponents/Card'
import UserNav from './UserCenter'
import Page from '../ViewComponents/Page'
export default {
  name: 'UserBlog',
  data () {
    return {
      pageSize: 10,
      rightUser: true, // this.user.UserName === this.viewuser.UserName?true:false,
      user: {
        UserName: 'User'
      },
      viewuser: {
        UserName: 'User'
      }
    }
  },
  components: {
    Page,
    myCard,
    UserNav
  },
  methods: {
    changePage (val) {
      this.pageSize = val
    },
  // 新添加的
    dataListFn: function (index) {
      this.$axios.get('http://127.0.0.1:8090/demand/selectListByPage', { // 后端实际
        params: {
          page: index,
          limit: '10',
          state: 0
        }
      }).then((res) => {
        if (res.data.message === 'success') {
          this.dataList = []
          for (let i = 0; i < res.data.data.length; i++) {
            this.dataList.push(res.data.data[i])
          }
          this.all = res.data.totalPage// 总页数
          this.cur = res.data.pageNum
          this.totalPage = res.data.totalPage
        }
      })
    },
    // 分页
    btnClick: function (data) { // 页码点击事件
      if (data !== this.cur) {
        this.cur = data
      }
      // 根据点击页数请求数据
      this.dataListFn(this.cur.toString())
    },
    pageClick: function () {
    // 根据点击页数请求数据
      this.dataListFn(this.cur.toString())
    }
  },
  computed: {
    // 分页
    indexs: function () {
      var left = 1
      var right = this.all
      var ar = []
      if (this.all >= 5) {
        if (this.cur > 3 && this.cur < this.all - 2) {
          left = this.cur - 2
          right = this.cur + 2
        } else {
          if (this.cur <= 3) {
            left = 1
            right = 5
          } else {
            right = this.all
            left = this.all - 4
          }
        }
      }
      while (left <= right) {
        ar.push(left)
        left++
      }
      return ar
    }
  }
}
</script>
