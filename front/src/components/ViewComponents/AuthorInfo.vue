<template>
  <div>
    <el-row>
      <el-col>
        <el-card :body-style="{ padding: '20px' }" style="position:fixed;">
          <el-row>
            <el-button style="padding: 0px; line-height: 0px; border: 0px;" @click="toAuthorInfo">
              <el-avatar shape="square" :size="100" :fit="'fill'" :src="imgUrl"></el-avatar>
            </el-button>
          </el-row>
          <el-row><el-button type="text" @click="toAuthorInfo">{{AuthorName}}</el-button></el-row>
          <el-row><el-button plain style="padding: 7px;">关注/取消关注</el-button></el-row>
          <el-row style="margin-top: 10px;">
            <el-tooltip content="点赞" placement="bottom" effect="light">
              <el-button type="primary" icon="el-icon-thumb" circle></el-button>
            </el-tooltip>
            <el-tooltip content="评论" placement="bottom" effect="light">
              <el-button type="primary" icon="el-icon-edit" circle @click="dialog = true"></el-button>
            </el-tooltip>
            <el-tooltip content="收藏/取消收藏" placement="bottom" effect="light">
              <el-button type="primary" icon="el-icon-star-off" circle></el-button>
            </el-tooltip>
            <el-tooltip content="分享" placement="bottom" effect="light">
              <el-button type="primary" icon="el-icon-share" circle></el-button>
            </el-tooltip>
            <el-tooltip content="删除" placement="bottom" effect="light">
              <el-button type="danger" icon="el-icon-delete" circle></el-button>
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
      >
      <div class="demo-drawer__content">
        <el-form :model="form">
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
</style>

<script>
import doComment from './doComment'
import {addQuillTitle} from '../quill-title'
export default {
  name: 'AuthorInfo',
  data () {
    return {
      currentDate: new Date(),
      AuthorName: 'User',
      imgUrl: 'https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png',
      squareUrl: 'https://cube.elemecdn.com/9/c2/f0ee8a3c7c9638a54940382568c9dpng.png',
      sizeList: ['large', 'medium', 'small'],
      dialog: false,
      loading: false,
      form: {
        content: ''
      },
      formLabelWidth: '80px',
      timer: null,
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
      }
    }
  },
  components: {
    doComment
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
        .catch(_ => {})
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
            if (res.errCode === 200) {
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
  }
}
</script>
