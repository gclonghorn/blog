<template>
  <div v-title data-title="编辑博客">
    <br><br>
    <el-tabs v-model="activeName" type="card">
      <el-tab-pane label="发布博客" name="first">
        <el-container style="margin-right:250px;margin-left:250px; margin-top:30px;">
          <el-container style="" direction="vertical">
            <el-form ref="infoForm" :model="Blog" :rules="rules" label-width="120px" enctype="multipart/form-data">
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
                    filterable
                    default-first-option
                    size="medium"
                    placeholder="请选择文章标签">
                    <el-option
                      v-for="item in Blog.options"
                      :key="item.id"
                      :label="item.name"
                      :value="item.id">
                    </el-option>
                  </el-select>
                </div>
              </el-form-item>

              <el-form-item label="博客正文" prop="content">
                <myEditor v-model="Blog.content" :isClear="isClear"></myEditor>

              </el-form-item>

              <el-form-item>
                <el-upload
                  class="upload-demo"
                  drag
                  ref="upload"
                  action="url"
                  :auto-upload="false"
                  :http-request="uploadFile"
                  :file-list="fileList"
                  :on-change="handleChange"
                  :limit=1>
                  <i class="el-icon-upload"></i>
                  <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
                </el-upload>
              </el-form-item>

              <el-form-item>
                <el-button type="primary" @click="onSubmit">发布文章</el-button>
                <el-button type="danger" >取消</el-button>
              </el-form-item>
            </el-form>
          </el-container>
        </el-container>
      </el-tab-pane>
      <el-tab-pane label="仅上传资源" name="second">
        <el-upload
          class="upload-demo"
          drag
          ref="upload2"
          action="url"
          :auto-upload="false"
          :http-request="uploadFile"
          :file-list="fileList"
          :on-change="handleChange"
          :limit=1>
          <i class="el-icon-upload"></i>
          <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
        </el-upload>
        <el-button @click="Submit2">上传资源</el-button>
      </el-tab-pane>
    </el-tabs>

  </div>
</template>

<script>
// import axiosInstance from '../../api/index'
import myEditor from './wangEditor'
import {getCategory, submitBlog} from '../../api/api'
import axiosInstance from '../../api/index'
export default {
  name: 'test',
  data () {
    return {
      url: 'http://127.0.0.1:8000/files/',
      activeName: 'first',
      UserId: 'User',
      urls: {
        Home: '/',
        UpdateBlog: '/UpdateBlog'
      },
      Blog: {
        title: '',
        simple: '',
        content: '',
        options: [{
          name: 'HTML',
          id: 'HTML'
        }, {
          name: 'java',
          id: 'java'
        }],
        tags: '' // 为被选中标签的value属性值
      },
      header: {token: sessionStorage.token},
      // 表单验证
      rules: {
        title: [
          {required: true, message: '请输入标题', trigger: 'blur'}
        ],
        tags: [
          {required: true, message: '标签不能为空', trigger: 'blur'}
        ],
        content: [
          {required: true, message: '必须填写正文或资源的简介', trigger: 'blur'}
        ]
      },
      newBlogId: '',
      dialogImageUrl: '',
      dialogVisible: false,
      disabled: false,
      fileList: [],
      isClear: false
      // param:''
    }
  },
  methods: {
    log (value) {
      this.tags = value
      console.log(this.tags, value)
    },
    Submit2(){
      console.log(this.activeName)
      console.log(this.fileList)
      if(this.activeName === 'second' && this.fileList.length === 0){
        this.$message({
          message:'必须上传文件',
          type: 'warning'
        })
        return
      }
      this.$refs.upload2.submit()
      this.$message({
        message:'上传资源成功！', type: 'success'
      })
      console.log('upload file only done')
      this.$router.push('/MainPage')
    },
    handleChange (file, fileList) {
      this.fileList = fileList
      console.log(this.fileList)
    },
    uploadFile () {
      let axios = axiosInstance
      let formData = new FormData()
      formData.append('file', this.fileList[0].raw)
      formData.append('post', this.newBlogId)
      formData.append('name', this.fileList[0].name)
      axios.post(this.url, formData, {headers: {'Content-Type': 'multipart/form-data' }}).then(response => {
        if (response.status === 201) {
          this.$message({
            message: '上传文件成功！',
            type: 'success'
          })
        } else {
          this.$message({
            message: '文件上传失败！',
            type: 'error'
          })
        }
      }).catch(error => {
        if(error.response){
          console.log(error.response)
        }
      })
    },
    onSubmit () {
      this.$refs.infoForm.validate((valid) => {
        if (valid) { // 创建新博客
          submitBlog(this.Blog.title, this.Blog.content, this.Blog.tags, this.Blog.simple).then(response => {
            if (response.status === 201) {
              console.log(response)
              this.newBlogId = response.data.id
              this.$refs.upload.submit()
              this.$message({
                message:'发布新博客成功！', type:'success'
              })
              this.$router.push('/MainPage')// 想跳转到博客展示页面，但是需要用户名和文章名
            } else {
              console.log(response)
              this.$message({
                message: '发布新博客失败',
                type: 'error'
              })
            }
          }).catch(error =>{
            if(error.response){
              console.log(error.response)
            }
          })
        }
      })
    },
    getCategory () {
      getCategory().then(response => {
        if (response.status === 200) {
          // let i = 0
          // let sum = response.data.length
          // for (i = 0; i < sum; i++) {
          //   this.Blog.options[i].label = response.data[i].name
          //   this.Blog.options[i].value = response.data[i].id
          // }
          this.Blog.options = response.data
        }
      }).catch(error =>{
        if(error.response){
          console.log(error.response)
        }
      })
    }
  },
  components: {
    myEditor
  },
  mounted () {
    this.getCategory()
  }
}

</script>

<style scoped>
  .el-message-box {
    z-index: 2000;
  }
</style>
