<template>
  <div class="search" v-title data-title="搜索博客">
    <el-container>
      <el-aside width="200px">
        <myselectsort style="float: left; margin-top: 50px"></myselectsort>
        <mytransfer style="float: left; margin-top: 50px"></mytransfer>
      </el-aside>
      <el-main>
        <el-row>
          <div v-for="o in pageSize" :key="o">
            <mycard></mycard>
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
import mycard from './Card.vue'
import myselectsort from './SelectSort.vue'
import mytransfer from './Transfer.vue'
import Page from '../ViewComponents/Page'
export default {
  name: 'search',
  data () {
    return {
      pageSize: 10
    }
  },
  components: {
    mycard,
    myselectsort,
    mytransfer,
    Page
  },
  methods: {
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

<style>
#search {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
}
</style>
