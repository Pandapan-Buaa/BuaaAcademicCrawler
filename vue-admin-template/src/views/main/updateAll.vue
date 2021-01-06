<template>
  <el-main>
    <el-row>
      <el-col :span="24">
        <el-steps :space="2000" :active="active" finish-status="success">
          <el-step title="已完成"></el-step>
          <el-step title="进行中"></el-step>
          <el-step title="步骤 3"></el-step>
        </el-steps>
      </el-col>
    </el-row>
    <el-row>
      <el-form>

      </el-form>
      <el-button @click="next">下一步</el-button>
    </el-row>

  </el-main>

</template>

<script>
export default {
  name: 'UpdateAll',
  data() {
    return {
      active: 0
    }
  },

  methods: {
    next() {
      if (this.active++ > 2) {
        this.active = 0
      }
    }
  }
}
</script>
<style scoped>

</style>
