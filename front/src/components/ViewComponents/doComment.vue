<template>
  <div>
    <el-tooltip content="评论" placement="bottom" effect="light">
      <el-button type="primary" icon="el-icon-edit" circle @click="dialog = true"></el-button>
    </el-tooltip>
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
          <el-form-item label="评论：" :label-width="formLabelWidth">
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
          <el-button type="primary" @click="$refs.drawer.closeDrawer()" :loading="loading">{{ loading ? '提交中 ...' : '确 定' }}</el-button>
        </div>
      </div>
    </el-drawer>
  </div>
</template>

<script>
import {addQuillTitle} from '../quill-title'

export default {
  name: 'doComment',
  data () {
    return {
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
      this.$confirm('确定要提交表单吗？')
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
    }
  }
}
</script>

<style scoped>

</style>
