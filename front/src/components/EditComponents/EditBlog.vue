<template>
  <div v-title data-title="编辑博客">
    <el-container style="margin-right:250px;margin-left:250px; margin-top:30px;">
      <el-container style="" direction="vertical">
        <el-form ref="infoForm" :model="Blog" :rules="rules" label-width="120px">
          <el-form-item label="博客标题" prop="title">
            <el-input
                type="textarea"
                placeholder="请输入博客标题"
                v-model="Blog.title"
                maxlength="30"
                show-word-limit
                style="width: 70%; float: left"
              >
            </el-input>
          </el-form-item>

          <el-form-item label="内容简介" prop="simple">
            <el-input
                type="textarea"
                placeholder="默认为博客正文的前30字"
                v-model="Blog.simple"
                maxlength="30"
                show-word-limit
                style="width: 70%; float: left"
              >
            </el-input>
          </el-form-item>

          <el-form-item label="博客标签" prop="tags">
            <div class="grid-content" style="text-align:left; overflow:visible;">
              请选择标签：<br>
              <!--需要输入框长一点-->
              <el-select
                v-model="Blog.tags"
                multiple
                filterable
                allow-create
                default-first-option
                size="medium"
                placeholder="请选择文章标签">
                <el-option
                  v-for="item in Blog.options"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
            </div>
          </el-form-item>

          <el-form-item label="博客正文" prop="content">
            <el-upload
                    class="avatar-uploader"
                    :action="serverUrl"
                    style="width: 50px;"
                    :headers="header"
                    :show-file-list="true"
                    :on-success="uploadSuccess"
                    :on-error="uploadError"
                    :file-list="Blog.picList"
                    :before-upload="beforeUpload">
            </el-upload>
            <div class="edit_container">
              <quill-editor v-model="Blog.content"
                            ref="myQuillEditor"
                            class="editer"
                            :options="editorOption" @ready="onEditorReady($event)">
              </quill-editor>
            </div>
          </el-form-item>

          <el-form-item>
            <el-upload
              action="#"
              list-type="picture-card"
              :file-list="Blog.fileList"
              multiple
              :auto-upload="false">
                <i slot="default" class="el-icon-plus"></i>
                <div slot="file" slot-scope="{file}">
                  <img
                    class="el-upload-list__item-thumbnail"
                    :src="getUrl(file)" alt=""
                  >
                  <span class="el-upload-list__item-actions">
                    <span
                      class="el-upload-list__item-preview"
                      @click="handlePictureCardPreview(file)"
                    >
                      <i class="el-icon-zoom-in"></i>
                    </span>
                    <span
                      v-if="!disabled"
                      class="el-upload-list__item-delete"
                      @click="handleRemove(file)"
                    >
                      <i class="el-icon-delete"></i>
                    </span>
                  </span>
                </div>
            </el-upload>
            <el-dialog :visible.sync="dialogVisible">
              <img width="100%" :src="dialogImageUrl" alt="">
            </el-dialog>
          </el-form-item>

          <el-form-item>
            <el-button type="primary" @click="onSubmit">发布文章</el-button>
            <el-button type="danger" >取消</el-button>
          </el-form-item>
        </el-form>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import { addQuillTitle } from '../quill-title.js'
const toolbarOptions = [
  ['bold', 'italic', 'underline', 'strike'],
  ['blockquote', 'code-block'],
  [{ 'header': 1 }, { 'header': 2 }],
  [{ 'list': 'ordered' }, { 'list': 'bullet' }],
  [{ 'script': 'sub' }, { 'script': 'super' }],
  [{ 'indent': '-1' }, { 'indent': '+1' }],
  [{ 'direction': 'rtl' }],
  [{ 'size': ['small', false, 'large', 'huge'] }],
  [{ 'header': [1, 2, 3, 4, 5, 6, false] }],
  [{ 'color': [] }, { 'background': [] }],
  [{ 'font': [] }],
  [{ 'align': [] }],
  ['clean'],
  ['link', 'image', 'video']
]
export default {
  name: 'test',
  data () {
    return {
      Blog: {
        title: '',
        simple: '',
        content: '',
        options: [{
          value: 'HTML',
          label: 'HTML'
        }, {
          value: 'CSS',
          label: 'CSS'
        }, {
          value: 'JavaScript',
          label: 'JavaScript'
        }],
        tags: [],
        fileList: [],
        picList: []
      },
      editorOption: {
        theme: 'snow',
        boundary: document.body,
        modules: {
          toolbar: {
            container: toolbarOptions,
            handlers: {
              'image': function (value) {
                if (value) {
                  document.querySelector('.avatar-uploader input').click()
                } else {
                  this.quill.format('image', false)
                }
              }
            }
          }
        },
        placeholder: 'Insert text here ...',
        readOnly: false
      },
      quillUpdateImg: false, // 根据图片上传状态来确定是否显示loading动画，刚开始是false,不显示
      serverUrl: '', // 这里写你要上传的图片服务器地址
      header: {token: sessionStorage.token},
      // 表单验证
      rules: {
        title: [
          {required: true, message: '请输入标题', trigger: 'blur'}
        ],
        content: [
          {required: true, message: '请输入详细内容', trigger: 'blur'}
        ],
        tags: [
          {required: true, message: '标签不能为空', trigger: 'blur'}
        ]
      },
      dialogImageUrl: '',
      dialogVisible: false,
      disabled: false
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
    onEditorReady (editor) {
    },
    onSubmit () {
      // 提交
      // this.$refs.infoForm.validate，这是表单验证
      this.$refs.infoForm.validate((valid) => {
        if (valid) {
          this.$post('m/add/about/us', this.infoForm).then(res => {
            if (res.errCode === 200) { // 修改了==
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
    submitUpload () {
      this.$refs.upload.submit()
    },
    handleRemove (file, fileList) {
      console.log(file, fileList)
    },
    handlePreview (file) {
      console.log(file)
    },
    beforeUpload () {
    // 显示loading动画
      this.quillUpdateImg = true
    },
    handleDownload (file) {
      console.log(file)
    },
    uploadSuccess (res, file) {
      // res为图片服务器返回的数据
      // 获取富文本组件实例
      let quill = this.$refs.myQuillEditor.quill
      // 如果上传成功
      if (res.code === '200' && res.info !== null) {
        // 获取光标所在位置
        let length = quill.getSelection().index
        // 插入图片  res.info为服务器返回的图片地址
        quill.insertEmbed(length, 'image', res.info)
        // 调整光标到最后
        quill.setSelection(length + 1)
      } else {
        this.$message.error('图片插入失败')
      }
      // loading动画消失
      this.quillUpdateImg = false
    },

    // 富文本图片上传失败
    uploadError () {
      // loading动画消失
      this.quillUpdateImg = false
      this.$message.error('图片插入失败')
    },
    handlePictureCardPreview (file) {
      this.dialogImageUrl = file.url
      this.dialogVisible = true
    },
    getUrl (file) {
      return file.url
    }
  },
  components: {
  }
}
</script>

<style scoped>
  .el-message-box {
    z-index: 2000;
  }
</style>
