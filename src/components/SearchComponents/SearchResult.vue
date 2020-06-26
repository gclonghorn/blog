<template>
  <div class="search" v-title data-title="搜索博客">
    <el-container>
      <el-aside width="200px">
        <el-select v-model="selectValue" placeholder="请选择排序方式"  @click="updateSelectValue" style="width: 150px; margin-top: 40px">
          <el-option
            v-for="item in options"
            :key="item.value"
            :label="item.label"
            :value="item.value">
          </el-option>
        </el-select>
        <br/><br/><br/>
        <div>
          <el-checkbox-group v-model="check" @change="updateCheck" :max="1" :min="0">
            <el-checkbox v-for="item in categories" :label="item.name" :key="item.id" border
            style="margin-left: 30px; width: 90px; margin-right: 30px">{{item.name}}</el-checkbox><br/>
          </el-checkbox-group>
        </div>
      </el-aside>
      <el-main style="margin-right: 200px; color: white">
        <el-row>
          <div v-for="(item, index) in Cards" :key="index">
            <myCard :card="item"></myCard>
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
import Page from '../ViewComponents/Page'
import axiosInstance from '../../api/index'
import {getCategory} from '../../api/api'
import myCard from './Card'
export default {
  name: 'search',
  data () {
    return {
      keys: '', // 原来是数组 改成字符串了
      options: [{
        value: 'pub_date',
        label: '最早发布'
      }, {
        value: '-pub_date',
        label: '最新发布'
      }, {
        value: 'read_num',
        label: '阅读量最低'
      }, {
        value: '-read_num',
        label: '阅读量最高'
      }],
      selectValue: '',
      pageSize: 8,
      currentPage: 1,
      categories: [{
        id: 1,
        name: 'Html'
      }, {
        id: 2,
        name: 'java'
      }],
      check: [], // item.name
      checkID: 0,
      // Cards: [{
      //   id: 100,
      //   author: {
      //     username: 'User',
      //     id: '14',
      //     head: 'https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png'
      //   },
      //   title: 'title',
      //   excerpt: '文章简介', // 无
      //   pub_date: '2019-01-01',
      //   tags: [// 无
      //     {value: 'HTML', label: 'HTML'},
      //     {value: 'java', label: 'java'}
      //   ]
      // }, {
      //   id: 200,
      //   author: {
      //     username: 'User',
      //     id: '14',
      //     head: 'https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png'
      //   },
      //   title: 'title',
      //   excerpt: '文章简介',
      //   pub_date: '2019-01-01',
      //   tags: [
      //     {value: 'HTML', label: 'HTML'},
      //     {value: 'java', label: 'java'}
      //   ]
      // }],
      Cards:[],
      total: 2
    }
  },
  components: {
    Page,
    myCard
  },
  inject: ['reload'],
  mounted () {
    this.getCategory()
    this.keys = this.$route.query.keys
    this.getSearchResult(this.currentPage, this.pageSize, this.selectValue, this.check)
  },
  updated () {
    // this.getSearchResult(this.currentPage, this.pageSize)
  },
  watch: {// 用来每次重新输入关键词都可以重新查询
    '$route': {
      handler (route) {
        const that = this
        if (route.name === 'SearchResult') {
          console.log(this.$route.query.keys)
          if(this.currentPage > 1){
            this.currentPage = 1
          }
          this.getSearchResult(this.currentPage, this.pageSize, this.selectValue, this.check)
        }
      },
      deep: true
    },
    currentPage: {
      handler (oldValue, newValue) {
        if (oldValue !== newValue) {
          this.getSearchResult(this.currentPage, this.pageSize, this.selectValue, this.check)
        }
      }
    },
    pageSize: {
      handler (oldValue, newValue) {
        if (oldValue !== newValue) {
          this.getSearchResult(this.currentPage, this.pageSize, this.selectValue, this.check)
        }
      }
    },
    selectValue: {
      handler (oldValue, newValue) {
        if (oldValue !== newValue) {
          this.getSearchResult(this.currentPage, this.pageSize, this.selectValue, this.check)
        }
      }
    },
  },
  methods: {
    getSearchResult (p, pageSize, order, checked) {
      this.keys = this.$route.query.keys
      const axios = axiosInstance
      for (let i = 0; i < this.categories.length; i++) {
        if (this.categories[i].name === this.check[0]) {
          checked = this.categories[i].id
          break
        }
      }
      console.log(this.checkID)
      axios.get('http://127.0.0.1:8000/list/', {
        params: {
          category: checked,
          ordering: order,
          search: this.keys,
          p: p,
          page_size: pageSize
        }
      }).then(response => {
        if (response.status === 200) {
          console.log(response)
          this.Cards = response.data.results
          this.total = response.data.count
        }
      }).catch(error => {//是错误码吗
        if (error.response.status === 404) {
          this.$message({
            message: 'No more things',
            type: 'error'
          })
        }
      })
    },
    updateSelectValue () {
      // this.getSearchResult(this.currentPage, this.pageSize)
      // this.reload()
    },
    updateCheck (newCheck) {
      // this.getSearchResult(this.currentPage, this.pageSize)
      // this.reload()
      console.log(newCheck)
      if(newCheck.length === 0){
        this.getSearchResult(this.p, this.pageSize, this.selectValue, null)
      }
      else{
        this.check = newCheck
        this.getSearchResult(this.p, this.pageSize, this.selectValue, this.check)
      }
    },
    getCategory () {
      getCategory().then(response => {
        if (response.status === 200) {
          console.log(response)
          // let sum = response.data.length
          // for (let i = 0; i < sum; i++) {
          //   this.categories[i].name = response.data[i].name
          //   this.categories[i].id = response.data[i].id
          // }
          this.categories = response.data
        }
      }).catch(error =>{
        if(error.response){
          console.log(error.response)
        }
      })
    },
    changePage (val) {
      this.pageSize = val
      console.log(this.pageSize)
    },
    changeP (val) {
      this.currentPage = val
      console.log(this.currentPage)
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
.text {
    font-size: 14px;
  }

  .item {
    margin-top: 10px;
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
    float: left;
    margin-left: 25px;
    margin-right: 25px;
    margin-top: 15px;
    width: 900px;
  }
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
