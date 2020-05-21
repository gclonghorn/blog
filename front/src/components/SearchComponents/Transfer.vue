<template>
  <div>
    <el-checkbox style="float: left; margin-left: 10px" v-model="checked1" label="html" border></el-checkbox>
    <el-checkbox style="float: left; margin-left: 10px" v-model="checked2" label="Java" border></el-checkbox>
    <el-checkbox style="float: left; margin-left: 10px" v-model="checked3" label="CSS" border></el-checkbox>
    <el-checkbox style="float: left; margin-left: 10px" v-model="checked4" label="C" border></el-checkbox>
    <el-checkbox style="float: left; margin-left: 10px" v-model="checked5" label="Python" border></el-checkbox>
    <el-checkbox style="float: left; margin-left: 10px" v-model="checked6" label="C++" border></el-checkbox>
  </div>
</template>

<script>
export default {
  data () {
    return {
      checked1: false,
      checked2: false,
      checked3: false,
      checked4: false
    }
  } // 怎么实现 点击之后出现对应的结果
}
</script>
