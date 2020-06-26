<template>
  <div>
    <div class="editor">
      <div ref="editor"style="min-height: 300px;text-align: left"></div>
    </div>
  </div>
</template>

<script>
  import E from 'wangeditor'
  export default {
    name: "wangEditor",
    data(){
      return{
        editor:null,
        info:'请输入...'
      }
    },
    model:{
      prop: 'value',
      event: 'change'
    },
    props:{
      value:String,
      isClear:Boolean
    },
    watch:{
      isClear(val){
        if(val){
          this.editor.txt.clear()
          this.info = null
        }
      },
      value(val){
        this.editor.txt.html(val)
      }
    },
    mounted() {
      this.setEditor()
    },
    methods:{
      setEditor(){
        this.editor = new E(this.$refs.editor)//通过refs.后面的（和ref=的一致）来控制
          this.editor.customConfig.onchange = (html) => {
            this.info = html
            this.$emit('change', this.info)
          }
        this.editor.customConfig.uploadImgShowBase64 = true  // 或者上传图片到服务器
        this.editor.customConfig.pasteFilterStyle = false// 关闭粘贴样式的过滤
        // 表情面板可以有多个 tab ，因此要配置成一个数组。数组每个元素代表一个 tab 的配置
        this.editor.customConfig.emotions = [
            {
                // tab 的标题
                title: '默认',
                // type -> 'emoji' / 'image'
                type: 'image',
                // content -> 数组
                content: [
                    {
                        alt: '[坏笑]',
                        src: 'http://img.t.sinajs.cn/t4/appstyle/expression/ext/normal/50/pcmoren_huaixiao_org.png'
                    },
                    {
                        alt: '[舔屏]',
                        src: 'http://img.t.sinajs.cn/t4/appstyle/expression/ext/normal/40/pcmoren_tian_org.png'
                    }
                ]
            },
            {
                // tab 的标题
                title: 'emoji',
                // type -> 'emoji' / 'image'
                type: 'emoji',
                // content -> 数组
                content: ['😀', '😃', '😄', '😁', '😆']
            }
        ]
        this.editor.customConfig.menus=[
           'head',  // 标题
          'bold',  // 粗体
          'fontSize',  // 字号
          'fontName',  // 字体
          'italic',  // 斜体
          'underline',  // 下划线
          'strikeThrough',  // 删除线
          'foreColor',  // 文字颜色
          'backColor',  // 背景颜色
          'link',  // 插入链接
          'list',  // 列表
          'justify',  // 对齐方式
          'quote',  // 引用
          'emoticon',  // 表情
          'image',  // 插入图片
          'table',  // 表格
          //'video',  // 插入视频
          'code',  // 插入代码
          'undo',  // 撤销
          'redo'  // 重复
        ]
        this.editor.customConfig.zIndex = 100
        this.editor.create()
        //editor.$textElem.attr('contenteditable', false)//禁用编辑功能，在展示博文、展示评论时使用
      }
    }
  }
</script>

<style scoped>
  .editor{
    width: 100%;
    text-align: left;
  }
  .toolbar{
    border: 1px solid #ccc;
  }
  .text{
    border: 1px solid #ccc;
    height: 500px;
  }
  .w-e-toolbar{
    flex-wrap:wrap;
  }
  .w-e-text-container{
    height: 700px !important;
  }
</style>
