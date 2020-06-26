<template>
  <el-card class="box-card">
    <div slot="header" class="clearfix">
      <el-button circle style="float: left; padding: 0px; line-height: 0px; border: 0px;" @click="toAuthorInfo(Card.author.username)">
        <el-avatar :src="Card.author.head" :fit="'scale-down'"></el-avatar>
      </el-button>
      <el-button type="text"
               style="float: left; margin-top: 10px; margin-left: 10px" @click="toAuthorInfo(Card.author.username)">
        {{Card.author.username}}</el-button>
      <span style="float: right; font-size: 14px; margin-top: 10px;">{{Card.pub_date}}</span>
      <el-button style="margin-top: 10px; padding: 3px 0" type="text" @click="toViewMain(Card.id)">{{Card.title}}</el-button>
      <el-tag type="info" size="medium"style="margin-right: 8px;">
        {{Card.category.name}}
      </el-tag>
    </div>
    <el-button style="margin-top: 10px; padding: 3px 0" type="text" @click="toViewMain(Card.id)">
      <div class="ql-container ql-snow" style="border: 0">
        <div class="ql-editor">
          <div v-html="Card.excerpt"></div>
        </div>
      </div>
    </el-button>
</el-card>
</template>

<script>
import {isJSON} from '../../main'
export default{
  name: 'Card',
  props: {
    Card: Object
  },
  data () {
    return {
      AuthorName: this.Card.AuthorName,
      title: this.Card.title,
      simple: this.Card.simple,
      postDate: this.Card.postDate,
      tags: this.Card.tags,
      imgUrl: this.Card.imgUrl
    }
  },
  mounted () {
    console.log(this.Card.excerpt)
    if(isJSON(this.Card.excerpt)){
      this.Card.excerpt = JSON.parse(this.Card.excerpt)
    }
  },
  methods: {
    toViewMain (ID) {
      // this.$router.push({name: 'ViewMain', params: {AuthorId: this.AuthorName, BlogTitle: this.title}}),
      this.$router.push({name: 'ViewMain', params: {AuthorName: this.Card.author.username, BlogTitle: this.Card.title, BlogId: ID}})
    },
    toAuthorInfo (username) {
      this.$router.push({name: 'UserInfo', params: {UserId: username, RealUserId: this.Card.author.id}})
    }
  },
  // watch:{
  //   Card:{
  //     handler(o,n){
  //       this.Card = n;
  //     },
  //     deep: true
  //   }
  // }
}
</script>

<style>
  .text {
    font-size: 14px;
  }

  .item {
    margin-top: 10px;
  }

  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }
  .clearfix:after {
    clear: both
  }

  .box-card {
    float: left;
    margin-left: 25px;
    margin-right: 25px;
    margin-top: 15px;
    width: 900px;
  }

  .el-button--text{
    color: black;
  }
</style>
