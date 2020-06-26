<template>
  <div>
    <el-row>
      <el-col>
        <el-card :body-style="{ padding: '20px' }" style="position:fixed; width: 250px;">
          <el-row>
            <el-button style="padding: 0px; line-height: 0px; border: 0px;" @click="toAuthorInfo(author.username)">
              <el-avatar shape="square" :size="100" :fit="'scale-down'" :src="author.head"></el-avatar>
            </el-button>
          </el-row>
          <el-row><el-button type="text" @click="toAuthorInfo(author.username)">{{author.username}}</el-button></el-row>
          <el-row><el-button plain style="padding: 7px;" :disabled="ifFollowDisabled" @click="toFollow(author.id)">关注</el-button>
          <el-button plain style="padding: 7px;" :disabled="ifDisabled" @click="cancelFollow()">取消关注</el-button></el-row>
          <el-row style="margin-top: 10px;">
            <el-tooltip content="点赞"  placement="bottom" effect="light" >
              <el-button type="primary" icon="el-icon-thumb" circle :disabled="ifLike" @click="doLike"></el-button>
            </el-tooltip>
            <el-tooltip content="评论" placement="bottom" effect="light">
              <el-button type="primary" icon="el-icon-edit" circle @click="dialog = true"></el-button>
            </el-tooltip>
            <el-tooltip content="取消点赞"  placement="bottom" effect="light">
              <el-button type="danger" icon="el-icon-thumb" circle :disabled="ifCancelLike" @click="cancelLike"></el-button>
            </el-tooltip>
            <el-tooltip content="删除" placement="bottom" effect="light">
              <el-button type="danger" icon="el-icon-delete" circle v-if="ifBlogAuthor" @click="deleteBlog"></el-button>
            </el-tooltip>
          </el-row>
        </el-card>
      </el-col>
    </el-row>

    <el-drawer
      title="评论"
      :before-close="handleClose"
      :visible.sync="dialog"
      direction="ltr"
      custom-class="demo-drawer"
      ref="drawer"
      size="70%"
      style="z-index: 150;"
      >
      <div class="demo-drawer__content">
        <el-form :model="form" ref="infoForm" :rules="rules">
          <el-form-item label="评论：" :label-width="formLabelWidth" prop="content">
            <div class="edit_container" >
              <myEditor v-model="form.content" :isClear="isClear"></myEditor>
            </div>
          </el-form-item>
        </el-form>
        <div class="demo-drawer__footer">
          <el-button @click="cancelForm">取 消</el-button>
          <el-button type="primary" @click="$refs.drawer.closeDrawer()" :loading="loading">{{ loading ? '提交中 ...' : '提 交' }}</el-button>
        </div><!---->
      </div>
    </el-drawer>
  </div>
</template>

<script>
import {submitComment, toFollow, Like, getLikeInfo, getFollowInfo, getUserInfo2} from '../../api/api'
import axiosInstance from '../../api/index'
import myEditor from '../EditComponents/wangEditor'
export default {
  name: 'AuthorInfo',
  props: [
    'authorId',
    'BlogId'
  ],
  data () {
    return {
      ifDisabled: true,
      ifFollowDisabled: false,
      ifLike: false,
      ifCancelLike: true,
      likeID: '',
      followID: '',
      ifBlogAuthor: false, // ______________________________________________
      currentDate: new Date(),
      sizeList: ['large', 'medium', 'small'],
      dialog: false,
      loading: false,
      form: {
        content: '',
        author: {
          id: '1',
          head: '',
          username: 'U1'
        }
      },
      formLabelWidth: '80px',
      timer: null,
      isClear: false,
      author: {
        username: 'root',
        tel: '12345678911',
        email: 'root@root.com',
        introduction: null,
        id: 1,
        reg_date: '2020-06-10T21:52:58.499387+08:00',
        posts: [],
        follower: 0,
        subscriber: 0,
        head: null
      },
      rules: {
        content: [{
          required: true, message: '评论内容不能为空', trigger: 'blur'
        }]
      },
      ifDone: true
    }
  },
  components: {
    myEditor
  },
  mounted () {
    console.log(this.authorId)
    this.getUserInfo(this.authorId)
    this.getIfBlogAuthor()// ___________________________________________
    this.getLike()
    this.getFollow()
    console.log(this.author)
  },
  watch: {
    // author:{
    //   handler(o, n){
    //     this.author = n;
    //     console.log(this.author)
    //   },
    //   deep: true
    // }
  },
  methods: {
    getUserInfo (id) {
      getUserInfo2(id).then(response => {
        if (response.status === 200) {
          console.log(response)
          let i = response.data[0]
          this.author = i
          console.log(this.author)
        } else {
          this.$message({
            message: '获取信息失败' + response.message,
            type: 'error'
          })
        }
      })
    },
    handleClose (done) {
      if (this.loading) {
        return
      }
      this.$confirm('确定要提交评论吗？', '提交评论', {
        confirmButtonText: '确定',
        cancelButtonText: '取消'
      }).then(_ => {
        this.loading = true
        console.log(this.BlogId)
        console.log(this.form.content)
        this.submitComment()
        if (this.ifDone) { done() } else return
      }).catch(_ => {})
    },
    cancelForm () {
      this.loading = false
      this.dialog = false
      clearTimeout(this.timer)
    },
    onEditorReady (editor) {
    },
    submitComment () {
      // 提交
      // this.$refs.infoForm.validate，这是表单验证
      console.log('正在提交函数')
      console.log(this.BlogId)
      console.log(this.form.content)
      this.$refs.infoForm.validate((valid) => {
        if (valid) {
          this.ifDone = true
          submitComment(this.BlogId, this.form.content).then(response => {
            console.log(response)
            if (response.status === 201) {
              this.$message({
                message: '提交成功', type: 'success'})
              this.$refs.infoForm.resetFields()
              this.$emit('reGetBlog')
            } else {
              this.$message({
                message: '提交评论失败',
                type: 'error'
              })
            }
          })
        } else {
          this.ifDone = false
        }
      })
    },
    doLike () {
      Like(this.BlogId).then(response => {
        console.log(response)
        if (response.status === 201) {
          this.ifLike = true
          this.ifCancelLike = false
          this.likeID = response.data.id
          this.$emit('changeLike')
          this.$message({
            message: '点赞成功', type: 'success'})
        } else if (response.status === 400) {
          this.$message({
            message: '已经点赞过',
            type: 'error'
          })
        }
      }).catch(error => {
        if (error.code === 400) {
          this.$message({
            message: '已经点赞过',
            type: 'error'
          })
        }
      })
    },
    cancelLike () {
      const axios = axiosInstance
      axios.delete('http://127.0.0.1:8000/like/' + this.likeID).then(response => {
        if (response.status === 204) {
          this.ifLike = false
          this.ifCancelLike = true
          this.$emit('changeLike')
          this.$message({
            message: '点赞取消成功', type: 'success'})
        } else if (response.status === 404) {
          this.$message({
            message: response.status.message,
            type: 'error'})
        }
      })
    },
    getLike () {
      console.log('getting like')
      console.log(this.BlogId)
      getLikeInfo().then(response => {
        console.log(response)
        let sum = response.data.length
        let i = 0
        for (i = 0; i < sum; i++) {
          if (response.data[i].post + '' === this.BlogId + '') {
            this.ifLike = true
            this.ifCancelLike = false
            console.log(this.ifCancelLike)
            this.likeID = response.data[i].id
            break
          }
        }
        // this.$emit('changeLike')
      })
    },
    toAuthorInfo (username) {
      this.$router.push({name: 'UserInfo', params: {UserId: username, RealUserId: this.author.id}})
    },
    toFollow (authorID) {
      toFollow(authorID).then(response => {
        if (response.status === 201) {
          this.ifDisabled = false
          this.ifFollowDisabled = true
          this.followID = response.data.id
          this.$message({
            message: '关注成功', type: 'success'})
        }
      }).catch(error => {
        if (error.status === 400) {
          this.$message({
            message: '关注失败',
            type: 'error'
          })
        }
      })
    },
    cancelFollow () {
      const axios = axiosInstance
      axios.delete('http://127.0.0.1:8000/userfavs/' + this.followID).then(response => {
        if (response.status === 204) {
          this.ifDisabled = true
          this.ifFollowDisabled = false
          this.$message({
            message: '取消关注成功', type: 'success'})
        }
      }).catch(error => {
        if (error.status === 404) {
          this.$message({
            message: '取消关注失败',
            type: 'error'
          })
        }
      })
    },
    getFollow () {
      getFollowInfo().then(response => {
        console.log(response)
        let sum = response.data.length
        let i = 0
        for (i = 0; i < sum; i++) {
          if (response.data[i].goods + '' === this.authorId + '') {
            this.ifFollowDisabled = true
            this.ifDisabled = false
            console.log(this.ifDisabled)
            this.followID = response.data[i].id
            break
          }
        }
      })
    },
    deleteBlog () {
      const axios = axiosInstance
      axios.delete('http://127.0.0.1:8000/edit/' + this.BlogId).then(response => {
        if (response.status === 204) {
          console.log(response)
          this.$message({
            message: '删除成功',
            type: 'success'
          })
          this.$router.push('/MainPage')
        } else {
          console.log(response)
          this.$message({
            message: '删除失败',
            type: 'error'
          })
        }
      }).then(error => {
        console.log(error)
      })
    },
    getIfBlogAuthor () {
      if (this.authorId + '' === this.GLOBAL.user_id + '') {
        this.ifBlogAuthor = true
        console.log(this.ifBlogAuthor)
      }
    }
  }
}
</script>

<style>
  .time {
    font-size: 13px;
    color: #999;
  }

  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }

  .button {
    padding: 0;
    float: right;
  }

  .image {
    width: 100%;
    display: block;
  }

  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }

  .clearfix:after {
      clear: both
  }
  .el-row {
    margin-bottom: 0px;
    min-width: 250px;
    &:last-child {
      margin-bottom: 0;
    }
  }
  .el-col {
    border-radius: 4px;
  }
  .bg-purple-dark {
    background: #99a9bf;
  }
  .bg-purple {
    background: #d3dce6;
  }
  .bg-purple-light {
    background: #e5e9f2;
  }
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }
  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }
  .el-drawer{

    overflow: scroll
    }

  .w-e-toolbar{
    flex-wrap:wrap;
  }
</style>
