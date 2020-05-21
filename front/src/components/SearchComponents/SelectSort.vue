<template>
  <el-select v-model="value" placeholder="请选择排序方式" style="width: 150px; margin-left: 10px">
    <el-option
      v-for="item in options"
      :key="item.value"
      :label="item.label"
      :value="item.value">
    </el-option>
  </el-select>
</template>

<script>
export default {
  data () {
    return {
      options: [{
        value: '选项1',
        label: '时间升序'
      }, {
        value: '选项2',
        label: '时间降序'
      }, {
        value: '选项3',
        label: '综合'
      }],
      value: ''
    }
  }
  // method 怎么实现点击之后出现对应的排序后结果
}
</script>
