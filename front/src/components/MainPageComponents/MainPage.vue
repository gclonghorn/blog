<template>
  <div v-title data-title="BA博客">
    <br/>
    <el-container>
      <el-aside width="200px">
        <br/><br/><br/><br/>
        <el-row>分类</el-row>
      <div
        class="each"
        v-for="(category, index) in categorys"
        :key="index"
        @click="toClassify(category.id)"
      >
        <el-button>{{ category.con }}</el-button>
        <br/>
      </div>
      </el-aside>
      <el-main>
        <el-row>
          <el-button type="primary" style="float: right" @click="login">登录</el-button>
          <el-button type="success" style="float: right" @click="regist">注册</el-button>
        </el-row>
        <el-row>推荐</el-row>
        <el-row>
          <div v-for="o in pageSize" :key="o">
            <myCard></myCard>
          </div>
        </el-row>
        <el-row>
          <Page v-on:changePage="changePage"></Page>
        </el-row>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import myCard from '../SearchComponents/Card'
import Page from '../ViewComponents/Page'
export default {
  components: {
    myCard,
    Page
  },
  data () {
    return {
      categorys: [
        { con: 'html', id: '1' },
        { con: 'Java', id: '2' },
        { con: 'Pyhton', id: '3' },
        { con: 'C', id: '4' }
      ],
      pageSize: 10,

      all: undefined, // 总页数
      cur: undefined, // 当前页码
      totalPage: undefined// 当前条数
    }
  },
  methods: {
    login () {
      this.$router.push({ path: '/Login' })
    },
    regist () {
      this.$router.push({ path: '/Register' })
    },
    toClassify (itemId) {
      this.$router.push({ path: '/Classify/' + itemId })
    },
    handleSizeChange (val) {
      console.log(`每页 ${val} 条`)
    },
    handleCurrentChange (val) {
      console.log(`当前页: ${val}`)
    },
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
