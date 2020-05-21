<template>
    <div v-title data-title="博客分类">
      <br/>
      <el-container direction="vertical">
        <div v-for="o in pageSize" :key="o" style="margin-left: 240px;">
            <mycard></mycard>
        </div><br>
        <Page @changePage="changePage"></Page>
      </el-container>
    </div>
</template>

<script>
import mycard from '../SearchComponents/Card'
import Page from '../ViewComponents/Page'
export default {
  components: {
    Page,
    mycard
  },
  data () {
    return {
      classifyId: undefined,
      pageSize: 10
    }
  },
  created () {
    this.$http.get('http://localhost:8080/ssm_init/hi') // 要填写实际的
      .then(response => {
        console.log(response.data)
        this.items = response.data
      })
      .catch(error => {
        console.log(error)
      })
  },
  methods: {
    changePage (val) {
      this.pageSize = val
    },
    comments: {
      Page
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
