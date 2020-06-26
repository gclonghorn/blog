<template>
  <div>
  <el-row>
  <el-col>
    <el-main style="background-color:#E9EEF3; margin-top:20px; padding:5px;"><!---->
      <el-container direction="horizontal">
        <div style="margin-top: 10px; margin-left: 15px;">
          <el-button style="padding: 0px; line-height: 0px; border: 0px;" @click="toAuthorInfo">
          <el-avatar
            shape="square"
            size="50"
            :src="comment.author.head"
            :fit="'scale-down'"></el-avatar>
          </el-button>
        </div>
          <el-button type="text" style="padding: 5px; width: 100px;" @click="toAuthorInfo(comment.author)">
            {{comment.author.username}}</el-button>
      </el-container>
      <hr width="98%" size="1" noshade="noshade" color="#C1D5CB"/>
      <div style="text-align: left; padding: 4px; margin-left: 8px;margin-right: 8px;">
<!--        <div class="ql-container ql-snow" style="border: 0">-->
<!--          <div class="ql-editor">-->
<!--            <div v-html="comment.body"></div>-->
<!--          </div>-->
<!--        </div>-->
<!--        <div ref="editor1" class="text"></div>-->
          <div v-html="JSON.parse(comment.body)"></div>

      </div>
      <hr width="98%" size="1" noshade="noshade" color="#C1D5CB"/>
      <div style="text-align:left;  margin-left: 10px;margin-right: 10px;">
        发布日期：{{comment.pub_date}}
        <el-tooltip content="评论" placement="bottom" effect="light">
          <el-button type="plain" icon="el-icon-edit" circle @click="dialog = true"></el-button>
        </el-tooltip>
        <el-button type="danger" icon="el-icon-delete"  circle @click="deleteComment(comment.id)"></el-button>
        <el-collapse v-model="activeCollapse" @click="handleChange">
          <el-collapse-item name = "1" style="padding: 5px 5px;">
            <template slot="title">
              查看回复（{{comment.replies.length}}）
            </template>
            <div v-for="(item, index) in comment.replies" :key="index">
              <div style="padding: 5px 18px;">
                <el-button type="text" style="padding: 5px; width: 100px;" @click="toAuthorInfo(item.author)">
              {{item.author.username}}</el-button>回复到：
<!--                <div class="ql-container ql-snow" style="border: 0">-->
<!--                  <div class="ql-editor">-->
<!--                    <div v-html="item.body"></div>-->
<!--                  </div>-->
<!--                </div>-->
<!--                <div ref="editor2" class="text"></div>-->
                  <div v-html="JSON.parse(item.body)"></div>

                <br>
                回复时间：{{item.pub_date}}
                <el-button type="danger" icon="el-icon-delete"  circle @click="deleteComment(item.id)"></el-button>
              </div>
              <hr width="98%" size="1" noshade="noshade" color="#C1D5CB"/>
            </div>
          </el-collapse-item>
        </el-collapse>
      </div>
    </el-main>
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
    >
    <div class="demo-drawer__content">
      <el-form :model="form" ref="infoForm" :rules="rules">
        <el-form-item label="回复谁的评论：" :label-width="formLabelWidth" prop="name">
          <el-input v-model="form.name" :disabled="true"></el-input>
        </el-form-item>
        <el-form-item label="评论：" :label-width="formLabelWidth" prop="content">
          <myEditor v-model="form.content" :isClear="isClear"></myEditor>
        </el-form-item>
      </el-form>
      <div class="demo-drawer__footer">
        <el-button @click="cancelForm">取 消</el-button>
        <el-button type="primary" @click="$refs.drawer.closeDrawer()" :loading="loading">{{ loading ? '提交中 ...' : '提 交' }}</el-button>
      </div><!--submitComment(form.content)-->
    </div>
  </el-drawer>
  </div>
</template>

<script>
import {submitComment2} from '../../api/api'
import myEditor from '../EditComponents/wangEditor'
import axiosInstance from '../../api/index'
import E from 'wangeditor'
import {isJSON} from '../../main'

export default{
  props: {
    comment: Object,
    BlogId: Number
  },
  data () {
    return {
      imgUrl: this.comment.author.head,
      isClear: false,
      dialog: false,
      form: {
        name: '用户1',
        id: '1',
        content: ''
      },
      timer: null,
      loading: false,
      formLabelWidth: '120px',
      activeCollapse: '0',
      editor: null,
      rules: {
        content: [
          {required: true, message: '评论不能为空', trigger: 'blur'}
        ]
      },
      ifDone: true
    }
  },
  methods: {
    createEditor () {
      this.editor = new E(this.$refs.editor1, this.$refs.editor2)
      this.editor.customConfig.zIndex = 100
      this.editor.create()
      this.editor.$textElem.attr('contenteditable', false)// 禁用编辑功能，在展示博文、展示评论时使用
    },
    handleClose (done) {
      if (this.loading) {
        return
      }
      this.$confirm('确定要提交评论吗？')
        .then(_ => {
          this.loading = true
          this.submitComment()
          if (this.ifDone) { done() } else return
        })
        .catch(_ => {
        })
    },
    cancelForm () {
      this.loading = false
      this.dialog = false
      clearTimeout(this.timer)
    },
    submitComment (content) {
      // 提交
      // this.$refs.infoForm.validate，这是表单验证
      console.log(this.BlogId)
      console.log(this.form.content)
      this.$refs.infoForm.validate((valid) => {
        if (valid) {
          this.ifDone = true
          submitComment2(this.BlogId, this.form.content, this.comment.id).then(response => {
            console.log(response)
            if (response.status === 201) {
              this.$message({
                message: '提交成功', type: 'success'})
              this.$refs.infoForm.resetFields()
              this.$emit('reGetBlog')
            } else {
              this.$message({
                message: response.status.message, // 后端会返回具体的错误信息吗
                type: 'error'
              })
            }
          }).catch(error => {
            if (error.response) {
              console.log(error.response)
            }
          })
        } else {
          this.ifDone = false
        }
      })
    },
    deleteComment (commentID) {
      const axios = axiosInstance
      axios.delete('http://127.0.0.1:8000/comment/' + commentID).then(response => {
        if (response.status === 204) {
          console.log(response)
          this.$message({
            message: '删除成功', type: 'success'})
          this.$emit('reGetBlog')
        } else {
          console.log(response)
          this.$message({
            message: '删除失败', type: 'error'})
        }
      }).catch(error => {
        console.log(error)
        if (error.response.status === 404) {
          this.$message({
            message: '不能删除别人的评论',
            type: 'error'
          })
        }
      })
    },
    toAuthorInfo (username) {
      this.$router.push({name: 'UserInfo', params: {UserId: username}})
    },
    handleChange () {
      if (this.activeCollapse === 0) { this.activeCollapse = 1 } else { this.activeCollapse = 0 }
    }
  },
  components: {
    myEditor
  },
  mounted () {
    this.form.name = this.comment.author.username
    console.log(this.comment.body)
    console.log('以上是父级 ')
    console.log(this.comment.replies)
    console.log('以上是子评论')
    // this.createEditor()
  }
}
</script>

<style>
  .p{
    display: block;
    margin-block-start: 0em;
    margin-block-end: 0em;
    margin-inline-start: 0px;
    margin-inline-end: 0px;
  }
  .el-drawer{
    overflow: scroll;
  }
  .el-collapse-item__header{
    line-height: 25px;
    height: 25px;
    padding: 10px 20px;
    font-size: 16px;
  }
  .w-e-toolbar{
    flex-wrap:wrap;
  }
</style>
