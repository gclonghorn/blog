<template>
    <div  v-title data-title="个人中心-博客">
      <UserNav></UserNav>
      <el-col span="20">
        <el-row>
          <div v-for="(item, index) in Cards" :key="index">
            <my-card :card="item"></my-card>
            <div > <!--v-if="rightUser"-->
              <el-button type="danger" @click="deleteBlog(item.id)"
                         style="margin-top: 75px; margin-bottom: 75px;" v-if="rightUser">删除博客</el-button>
              <el-button type="success" @click="updateBlog(item.id)"
                         style="margin-top: 75px; margin-bottom: 75px;" v-if="rightUser">更新博客</el-button>
            </div>
          </div>
        </el-row>
        <el-row>
          <Page @changePage="changePage" @changeP="changeP"
                :total="total" :page-size="pageSize" :current-page="currentPage"></Page>
        </el-row>
        <br>
      </el-col>
    </div>
</template>

<script>
// import {getUserInfo} from '../../api/api'
import axiosInstance from '../../api/index'
import UserNav from './UserCenter'
import Page from '../ViewComponents/Page'
import myCard from '../SearchComponents/Card'
export default {
  name: 'UserBlog',
  data () {
    return {
      pageSize: 10,
      rightUser: true, // this.user.UserName === this.viewuser.UserName?true:false,
      user: {
        UserName: 'User',
        id: '2'
      },
      viewuser: {
        UserName: 'User'
      },
      // 下面是新加的吗
      /* Cards: [{
        BlogID: 100,
        AuthorName: 'User',
        title: 'title',
        simple: '文章简介',
        body: '在主页如何显示博文的摘要。因为我们采用markdown语法实现文章的排版，如果采用过滤器slice或者truncatechars截取文章的前多少个字符时{{ content|safe|slice:“500” }}，当恰好截取到包含有htlm标记的语法时，比如引用或图片时：在主页如何显示博文的摘要。因为我们采用markdown语法实现文章的排版，如果采用过滤器slice或者truncatechars截取文章的前多少个字符时{{ content|safe|slice:“500” }}，当恰好截取到包含有htlm标记的语法时，比如引用或图片时：在主页如何显示博文的摘要。因为我们采用markdown语法实现文章的排版，如果采用过滤器slice或者truncatechars截取文章的前多少个字符时{{ content|safe|slice:“500” }}，当恰好截取到包含有htlm标记的语法时，比如引用或图片时：在主页如何显示博文的摘要。因为我们采用markdown语法实现文章的排版，如果采用过滤器slice或者truncatechars截取文章的前多少个字符时{{ content|safe|slice:“500” }}，当恰好截取到包含有htlm标记的语法时，比如引用或图片时：在主页如何显示博文的摘要。因为我们采用markdown语法实现文章的排版，如果采用过滤器slice或者truncatechars截取文章的前多少个字符时{{ content|safe|slice:“500” }}，当恰好截取到包含有htlm标记的语法时，比如引用或图片时：',
        postDate: '2019-01-01',
        tags: {value: 'HTML', label: 'HTML'},
        imgUrl: 'https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png'
      }, {
        BlogID: 200,
        AuthorName: 'User',
        title: 'title',
        simple: '文章简介',
        body: '在主页如何显示博文的摘要。因为我们采用markdown语法实现文章的排版，如果采用过滤器slice或者truncatechars截取文章的前多少个字符时{{ content|safe|slice:“500” }}，当恰好截取到包含有htlm标记的语法时，比如引用或图片时：在主页如何显示博文的摘要。因为我们采用markdown语法实现文章的排版，如果采用过滤器slice或者truncatechars截取文章的前多少个字符时{{ content|safe|slice:“500” }}，当恰好截取到包含有htlm标记的语法时，比如引用或图片时：在主页如何显示博文的摘要。因为我们采用markdown语法实现文章的排版，如果采用过滤器slice或者truncatechars截取文章的前多少个字符时{{ content|safe|slice:“500” }}，当恰好截取到包含有htlm标记的语法时，比如引用或图片时：在主页如何显示博文的摘要。因为我们采用markdown语法实现文章的排版，如果采用过滤器slice或者truncatechars截取文章的前多少个字符时{{ content|safe|slice:“500” }}，当恰好截取到包含有htlm标记的语法时，比如引用或图片时：在主页如何显示博文的摘要。因为我们采用markdown语法实现文章的排版，如果采用过滤器slice或者truncatechars截取文章的前多少个字符时{{ content|safe|slice:“500” }}，当恰好截取到包含有htlm标记的语法时，比如引用或图片时：',
        postDate: '2019-01-01',
        tags: {value: 'HTML', label: 'HTML'},
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
        category: [// 无
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
        category: [
          {value: 'HTML', label: 'HTML'},
          {value: 'java', label: 'java'}
        ]
      }],
      pageSize: 8,
      currentPage: 1,
      total:2,
    }
  },
  components: {
    Page,
    UserNav,
    myCard
  },
  methods: {
    getUserBlog (p,pageSize) {
      this.Cards.length = 0
      const axios = axiosInstance
      axios.get('http://127.0.0.1:8000/list/', {
        params: {
          author: this.user.id, // this.$route.params.UserId
          p: p,
          pageSize: pageSize
        }
      }).then(response => {
        if (response.status === 200) {
          this.Cards = response.data.results
          this.total = response.data.count
        } else {
          this.$message({
            message: '获取博客列表失败',
            type: 'error'
          })
        }
      })
    },
    deleteBlog (BlogID) {
      const axios = axiosInstance
      axios.delete('http://127.0.0.1:8000/edit/' + BlogID).then(response => {
        if (response.status === 204) {
          console.log(response)
          this.$message({
            message:'删除成功',
            type:'success'
          })
          this.getUserBlog(1,8)
          //this.$router.push({name: 'UserInfo', params: {UserId: this.userId}})
        } else {
          console.log(response)
          this.$message({
            message:'删除失败',
            type:'error'
          })
        }
      }).then(error => {
        console.log(error)
      })
    },
    updateBlog (ID) {
      this.$router.push({path: '/UpdateBlog/', query: {BlogId: ID}})
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
    this.user.id = this.$route.params.RealUserId
    this.user.UserName = this.$route.params.UserId
    this.getUserBlog()
    console.log(this.user)
    console.log(this.GLOBAL)
    if (this.GLOBAL.user_id+'' === this.user.id+'') this.rightUser = true
    else this.rightUser = false
  },
  watch: {// 用来每次重新输入关键词都可以重新查询
    // '$route': {
    //   handler (route) {
    //     const that = this
    //     if (route.name === 'SearchResult') {
    //       this.getUserBlog(this.currentPage, this.pageSize, this.selectValue, this.check)
    //     }
    //   },
    //   deep: true
    // },
    currentPage: {
      handler (oldValue, newValue) {
        if (oldValue !== newValue) {
          this.getUserBlog(this.currentPage, this.pageSize)
        }
      }
    },
    pageSize: {
      handler (oldValue, newValue) {
        if (oldValue !== newValue) {
          this.getUserBlog(this.currentPage, this.pageSize)
        }
      }
    },
    selectValue: {
      handler (oldValue, newValue) {
        if (oldValue !== newValue) {
          this.getUserBlog(this.currentPage, this.pageSize)
        }
      }
    },
  },
}
</script>

<style scoped>

</style>
