<template>
    <div v-title data-title="博客分类">
      <br/>
      <el-container direction="vertical" style="margin-left:200px; margin-right:200px">
        <el-row>
          <div v-for="(item, index) in Cards" :key="index">
            <my-card :card="item"></my-card>
            <br/>
          </div>
        </el-row>
        <br/>
        <Page @changePage="changePage" @changeP="changeP"
                :total="total" :page-size="pageSize" :current-page="currentPage"></Page>
      </el-container>
    </div>
</template>

<script>
import myCard from '../SearchComponents/Card'
import Page from '../ViewComponents/Page'
import axiosInstance from '../../api/index'
export default {
  components: {
    Page,
    myCard
  },
  data () {
    return {
      categoryID: '',
      pageSize: 8,
      currentPage: 1,
      total:2,
      /* Cards: [{
        BlogId: 100,
        AuthorName: 'User',
        title: 'title',
        simple: '文章简介',
        body: '在主页如何显示博文的摘要。因为我们采用markdown语法实现文章的排版，如果采用过滤器slice或者truncatechars截取文章的前多少个字符时{{ content|safe|slice:“500” }}，当恰好截取到包含有htlm标记的语法时，比如引用或图片时：在主页如何显示博文的摘要。因为我们采用markdown语法实现文章的排版，如果采用过滤器slice或者truncatechars截取文章的前多少个字符时{{ content|safe|slice:“500” }}，当恰好截取到包含有htlm标记的语法时，比如引用或图片时：在主页如何显示博文的摘要。因为我们采用markdown语法实现文章的排版，如果采用过滤器slice或者truncatechars截取文章的前多少个字符时{{ content|safe|slice:“500” }}，当恰好截取到包含有htlm标记的语法时，比如引用或图片时：在主页如何显示博文的摘要。因为我们采用markdown语法实现文章的排版，如果采用过滤器slice或者truncatechars截取文章的前多少个字符时{{ content|safe|slice:“500” }}，当恰好截取到包含有htlm标记的语法时，比如引用或图片时：在主页如何显示博文的摘要。因为我们采用markdown语法实现文章的排版，如果采用过滤器slice或者truncatechars截取文章的前多少个字符时{{ content|safe|slice:“500” }}，当恰好截取到包含有htlm标记的语法时，比如引用或图片时：',
        postDate: '2019-01-01',
        tags: [
          {value: 'HTML', label: 'HTML'},
          {value: 'java', label: 'java'}
        ],
        imgUrl: 'https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png'
      }, {
        BlogId: 100,
        AuthorName: 'User',
        title: 'title',
        simple: '文章简介',
        body: '在主页如何显示博文的摘要。因为我们采用markdown语法实现文章的排版，如果采用过滤器slice或者truncatechars截取文章的前多少个字符时{{ content|safe|slice:“500” }}，当恰好截取到包含有htlm标记的语法时，比如引用或图片时：在主页如何显示博文的摘要。因为我们采用markdown语法实现文章的排版，如果采用过滤器slice或者truncatechars截取文章的前多少个字符时{{ content|safe|slice:“500” }}，当恰好截取到包含有htlm标记的语法时，比如引用或图片时：在主页如何显示博文的摘要。因为我们采用markdown语法实现文章的排版，如果采用过滤器slice或者truncatechars截取文章的前多少个字符时{{ content|safe|slice:“500” }}，当恰好截取到包含有htlm标记的语法时，比如引用或图片时：在主页如何显示博文的摘要。因为我们采用markdown语法实现文章的排版，如果采用过滤器slice或者truncatechars截取文章的前多少个字符时{{ content|safe|slice:“500” }}，当恰好截取到包含有htlm标记的语法时，比如引用或图片时：在主页如何显示博文的摘要。因为我们采用markdown语法实现文章的排版，如果采用过滤器slice或者truncatechars截取文章的前多少个字符时{{ content|safe|slice:“500” }}，当恰好截取到包含有htlm标记的语法时，比如引用或图片时：',
        postDate: '2019-01-01',
        tags: [
          {value: 'HTML', label: 'HTML'},
          {value: 'java', label: 'java'}
        ],
        imgUrl: 'https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png'
      }] */
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
        tags: [// 无
          {value: 'HTML', label: 'HTML'},
          {value: 'java', label: 'java'}
        ]
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
        tags: [
          {value: 'HTML', label: 'HTML'},
          {value: 'java', label: 'java'}
        ]
      }]
    }
  },
  methods: {
    getClassifyResult (p, pageSize) {
      const axios = axiosInstance
      axios.get('http://127.0.0.1:8000/list/', {
        params: {
          category: this.categoryID,
          p: p,
          page_size: pageSize
        }
      }).then(response => {
        if (response.status === 200) {
          console.log(response)
          this.Cards = response.data.results
          this.total = response.data.count
        }
      }).catch(error =>{
        if(error.response){
          console.log(error.response)
        }
      })
    },
    toViewMain (ID) {
      this.$router.push({path: 'ViewMain', query: {BlogId: ID}})
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
    this.categoryID = this.$route.params.id
    console.log(this.$route.params.id)
    this.getClassifyResult(this.currentPage, this.pageSize)
  },
  comments: {
    Page
  },
  watch: {// 用来每次重新输入关键词都可以重新查询
    // '$route': {
    //   handler (route) {
    //     const that = this
    //     if (route.name === 'SearchResult') {
    //       this.getClassifyResult(this.currentPage, this.pageSize, this.selectValue, this.check)
    //     }
    //   },
    //   deep: true
    // },
    currentPage: {
      handler (oldValue, newValue) {
        if (oldValue !== newValue) {
          this.getClassifyResult(this.currentPage, this.pageSize)
        }
      }
    },
    pageSize: {
      handler (oldValue, newValue) {
        if (oldValue !== newValue) {
          this.getClassifyResult(this.currentPage, this.pageSize)
        }
      }
    },
    selectValue: {
      handler (oldValue, newValue) {
        if (oldValue !== newValue) {
          this.getClassifyResult(this.currentPage, this.pageSize)
        }
      }
    },
  },
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
