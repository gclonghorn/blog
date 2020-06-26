<template>
  <div v-title data-title="BA博客">
    <br/>
    <el-container>
      <el-aside width="200px">
        <br/><br/><br/><br/>
        <el-row>分类</el-row>
      <div
        class="each"
        v-for="(item, index) in items"
        :key="index"
        @click="toClassify(item.id)"
      >
        <el-button style="margin-top:10px">{{ item.name }}</el-button>
        <br/>
      </div>
      </el-aside>
      <el-main style="margin-right: 10px"> <!--原来是200px-->
        <el-row>
          <el-button type="primary" style="float: right" @click="login">登录</el-button>
          <el-button type="success" style="float: right" @click="regist">注册</el-button>
        </el-row>
        <el-row>推荐</el-row>
        <el-row>
          <div v-for="(item,index) in Cards" :key="index">
            <myCard :Card="item"></myCard>
          </div>
        </el-row>
        <el-row>
          <Page @changePage="changePage" @changeP="changeP"
                :total="total" :page-size="pageSize" :current-page="currentPage"></Page>
        </el-row>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import myCard from '../SearchComponents/Card'
import Page from '../ViewComponents/Page'
import {getCategory} from '../../api/api'
import axiosInstance from '../../api'
export default {
  components: {
    myCard,
    Page
  },
  data () {
    return {
      items: [
        { name: '分类1', id: '1' },
        { name: '分类2', id: '2' }
        // { con: '分类3', id: '3' },
        // { con: '分类4', id: '4' }
      ],
      Cards: [{
        id: 100,
        author: {
          username: 'User',
          id: '14',
          head: 'https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png'
        },
        title: 'title',
        excerpt: '文章简介', // 无
        pub_date: '2019-01-01',
        category:
          {name: 'HTML', id: 'HTML'}
      }, {
        id: 200,
        author: {
          username: 'User',
          id: '14',
          head: 'https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png'
        },
        title: 'title',
        excerpt: '文章简介',
        pub_date: '2019-01-01',
        category:
          {name: 'java', id: 'java'}
      }],
      pageSize: 8,
      currentPage: 1,
      total: 2
    }
  },
  watch: {// 用来每次重新输入关键词都可以重新查询
    // '$route': {
    //   handler (route) {
    //     const that = this
    //     if (route.name === 'SearchResult') {
    //       this.getRecommend(this.currentPage, this.pageSize, this.selectValue, this.check)
    //     }
    //   },
    //   deep: true
    // },
    currentPage: {
      handler (oldValue, newValue) {
        if (oldValue !== newValue) {
          this.getRecommend(this.currentPage, this.pageSize)
        }
      }
    },
    pageSize: {
      handler (oldValue, newValue) {
        if (oldValue !== newValue) {
          this.getRecommend(this.currentPage, this.pageSize)
        }
      }
    },
    selectValue: {
      handler (oldValue, newValue) {
        if (oldValue !== newValue) {
          this.getRecommend(this.currentPage, this.pageSize)
        }
      }
    }
  },
  methods: {
    getCategory () {
      getCategory().then(response => {
        if (response.status === 200) {
          // console.log(response)
          // let sum = response.data.length
          // for (let i = 0; i < sum; i++) {
          //   this.items[i].con = response.data[i].name
          //   this.items[i].id = response.data[i].id
          // }
          this.items = response.data
        }
      }).catch(error => {
        if (error.response) {
          console.log(error.response)
        }
      })
    },
    getRecommend (p, pageSize) {
      let axios = axiosInstance
      axios.get('http://127.0.0.1:8000/recommend/', {
        params: {
          p: p,
          page_size: pageSize
        }
      }).then(response => {
        console.log(response)
        this.Cards = response.data.results
        this.total = response.data.count
      }).catch(error => {
        if (error.response) {
          console.log(error.response)
        }
      })
    },
    login () {
      if (this.$store.state.Authorization !== '') {
        this.$message({
          message: '您已登录，无法登录', type: 'error'
        })
        return
      }
      this.$router.push({ path: '/Login' })
    },
    regist () {
      if (this.$store.state.Authorization !== '') {
        this.$message({
          message: '您已登录，无法注册', type: 'error'
        })
        return
      }
      this.$router.push({ path: '/Register' })
    },
    toClassify (itemId) {
      this.$router.push({ name: 'Classify',
        params: {
          id: itemId}})
    },
    changePage (val) {
      this.pageSize = val
      console.log(this.pageSize)
    },
    changeP (val) {
      this.currentPage = val
      console.log(this.currentPage)
    }
  },
  mounted () {
    this.getCategory()
    this.getRecommend(this.currentPage, this.pageSize)
  }
}
</script>

<style>
  .el-aside {
    background-color: #FFFFFF;
    color: #333;
    text-align: center;
  }
  .el-main {
    background-color: #FFFFFF;
    color: #333;
    text-align: center;
  }
</style>
