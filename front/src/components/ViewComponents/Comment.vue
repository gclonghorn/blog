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
            :src="imgUrl"
            :fit="'fill'"></el-avatar>
          </el-button>
        </div>
        <el-container direction="vertical">
            <el-button type="text" style="padding: 5px; width: 100px;" @click="toAuthorInfo">{{authorName}}</el-button>
            <el-button plain style="padding: 5px; width: 100px;">关注/取消关注</el-button>
        </el-container>
      </el-container>
      <hr width="98%" size="1" noshade="noshade" color="#C1D5CB"/>
      <div style="text-align: left; padding: 4px; margin-left: 8px;">
        <div class="ql-container ql-snow">
            <div class="ql-editor">
              <div v-html="contentHtml"></div>
            </div>
        </div>
      </div>
      <hr width="98%" size="1" noshade="noshade" color="#C1D5CB"/>
      <div style="text-align:left;  margin-left: 15px;">
        发布日期：{{PostDate}}
        <el-tooltip content="点赞" placement="bottom" effect="light">
          <el-button type="plain" icon="el-icon-thumb" circle></el-button>
        </el-tooltip>
        <el-tooltip content="评论" placement="bottom" effect="light">
          <el-button type="plain" icon="el-icon-edit" circle @click="dialog = true"></el-button>
        </el-tooltip>
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
      <el-form :model="form">
        <el-form-item label="回复谁的评论：" :label-width="formLabelWidth" prop="name">
          <el-input v-model="form.name"></el-input>
        </el-form-item>
        <el-form-item label="评论：" :label-width="formLabelWidth" prop="content">
          <div class="edit_container" >
            <quill-editor v-model="form.content"
                          style="width: 87%;"
                          ref="myQuillEditor"
                          class="editer"
                          :options="editorOption" @ready="onEditorReady($event)">
            </quill-editor>
          </div>
        </el-form-item>
      </el-form>
      <div class="demo-drawer__footer">
        <el-button @click="cancelForm">取 消</el-button>
        <el-button type="primary" @click="$refs.drawer.closeDrawer()" :loading="loading">{{ loading ? '提交中 ...' : '提 交' }}</el-button>
      </div>
    </div>
  </el-drawer>
  </div>
</template>

<script>
import {addQuillTitle} from '../quill-title'

export default{
  data () {
    return {
      PostDate: '2019-11-23',
      imgUrl: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
      authorName: 'User',
      contentHtml: '<h1>评论内容</h1>',
      editorOption: {
        theme: 'snow',
        boundary: document.body,
        modules: {
          toolbar:
              [
                ['bold', 'italic', 'underline', 'strike'],
                ['blockquote', 'code-block'],
                [{'header': 1}, {'header': 2}],
                [{'list': 'ordered'}, {'list': 'bullet'}],
                [{'script': 'sub'}, {'script': 'super'}],
                [{'indent': '-1'}, {'indent': '+1'}],
                [{'direction': 'rtl'}],
                [{'size': ['small', false, 'large', 'huge']}],
                [{'header': [1, 2, 3, 4, 5, 6, false]}],
                [{'color': []}, {'background': []}],
                [{'font': []}],
                [{'align': []}],
                ['clean'],
                ['link', 'image', 'video']
              ]
        },
        placeholder: 'Insert text here ...',
        readOnly: false
      },
      dialog: false,
      form: {
        name: '用户1',
        content: ''
      },
      timer: null,
      loading: false,
      formLabelWidth: '120px'
    }
  },
  computed: {
    editor () {
      return this.$refs.myQuillEditor.quill
    }
  },
  mounted () {
    // 初始化
    addQuillTitle()
  },
  methods: {
    handleClose (done) {
      if (this.loading) {
        return
      }
      this.$confirm('确定要提交评论吗？')
        .then(_ => {
          this.loading = true
          this.timer = setTimeout(() => {
            done()
            // 动画关闭需要一定的时间
            setTimeout(() => {
              this.loading = false
            }, 400)
          }, 2000)
        })
        .catch(_ => {
        })
    },
    cancelForm () {
      this.loading = false
      this.dialog = false
      clearTimeout(this.timer)
    },
    onEditorReady (editor) {
    },
    onSubmit () {
      // 提交
      // this.$refs.infoForm.validate，这是表单验证
      this.$refs.infoForm.validate((valid) => {
        if (valid) {
          this.$post('m/add/about/us', this.form).then(res => {
            if (res.errCode == 200) {
              this.$message({
                message: res.errMsg,
                type: 'success'
              })
              this.$router.push('/aboutus/aboutlist')
            } else {
              this.$message({
                message: res.errMsg,
                type: 'error'
              })
            }
          })
        }
      })
    },
    toAuthorInfo () {
      this.$router.push('/UserCenter/UserInfo')
    }
  },
  components: {
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
</style>
