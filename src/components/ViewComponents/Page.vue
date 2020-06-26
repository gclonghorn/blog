<template>
  <div >
    <el-pagination
      @size-change="handleSizeChange"
      @current-change="handleCurrentChange"
      :current-page="currentPage"
      :page-sizes="[2, 4, 8, 16]"
      :page-size="pageSize"
      layout="total, sizes, prev, pager, next, jumper"
      :total="total">
    </el-pagination>
  </div>
</template>

<script>
export default {
  methods: {
    handleSizeChange (val) {
      console.log(`每页 ${val} 条`)
      this.pageSize = val
      this.$emit('changePage', this.pageSize)
    },
    handleCurrentChange (val) {
      console.log(`当前页: ${val}`)
      this.currentPage = val
      this.$emit('changeP', this.currentPage)
    }
  },
  props: {
    total: Number,
    currentPage: Number,
    pageSize:Number
  },
  data () {
    return {
      // currentPage: 1,
      // pageSize: 8
    }
  }
}
</script>
