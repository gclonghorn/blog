<template>
  <div v-title data-title="编辑博客">
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
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
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
  </div>
</template>

<script>
import axiosInstance from '../../api/index'
import myEditor from './wangEditor'
import {getCategory} from '../../api/api'
import {isJSON} from "../../main";

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
      BlogID: '',
      Blog: {
        title: '',
        simple: '',
        content: '',
        options: [{
          value: 'HTML',
          label: 'HTML'
        }, {
          value: 'java',
          label: 'java'
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
      dialogImageUrl: '',
      dialogVisible: false,
      disabled: false,
      fileList: [],
      isClear: false
      // param:''
    }
  },
  methods: {
    handleChange (file, fileList) {
      this.fileList = fileList
    },
    uploadFile () {
      console.log('uploading files')
      let axios = axiosInstance
      let formData = new FormData()
      formData.append('file', this.fileList[0].raw)
      formData.append('post', this.BlogID)
      formData.append('name', this.fileList[0].name)
      axios.post(this.url, formData, {headers: {'Content-Type': 'multipart/form-data' }}).then(response => {
        if (response.status === 201) {
          this.$message({
            message: '上传成功！',
            type: 'success'
          })
        }
        else{
          this.$message({
            message: '文件上传失败！',
            type: 'error'
          })
        }
      }).catch(error =>{
        if(error.response){
          console.log(error.response)
        }
      })
    },
    onSubmit () {
      this.$refs.infoForm.validate((valid) => {
        if (valid) { // 更新博客
          const axios = axiosInstance
          axios.put('http://127.0.0.1:8000/edit/' + this.BlogID + '/', {
            title: this.Blog.title,
            body: this.Blog.content,
            category: this.Blog.tags
          }).then(response => {
            if (response.status === 200) {
              console.log(response)
              this.$message({
                message: '更新成功！',
                type: 'success'
              })
              this.$refs.upload.submit()
              this.$router.push('/MainPage')// 想跳转到博客展示页面，但是需要用户名和文章名
            } else {
              console.log(response)
              this.$message({
                message: '更新失败！',
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
    beforeUpload (file) {
      this.Blog.files.push(file.name, file.raw)// ???????
      return false
    },
    getCategory () {
      getCategory().then(response => {
        if (response.status === 200) {
          let i = 0
          let sum = response.data.length
          for (i = 0; i < sum; i++) {
            this.Blog.options[i].label = response.data[i].name
            this.Blog.options[i].value = response.data[i].id
          }
        }
      }).catch(error =>{
        if(error.response){
          console.log(error.response)
        }
      })
    },
    getBlog (ID) {
      const axios = axiosInstance
      axios.get('http://127.0.0.1:8000/list/' + ID).then(response => {
        if (response.status === 200) {
          console.log(response)
          this.Blog.title = response.data.title
          this.Blog.simple = response.data.excerpt
          if(isJSON(response.data.body)){
            response.data.body = JSON.parse(response.data.body)
          }
          this.Blog.content = response.data.body
          this.Blog.tags = response.data.category.id
          // 文件 图片
        } else {
          this.$message({
            message: '获取详情失败' + response.message,
            type: 'error'
          })
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
    this.BlogID = this.$route.query.BlogId
    if (this.$route.query.BlogId !== '') {
      this.getBlog(this.$route.query.BlogId)
    }
  }
}

</script>

<style scoped>
  .el-message-box {
    z-index: 2000;
  }
</style>
