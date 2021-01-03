<template>
  <el-container>
    <el-steps :active="active" finish-status="success">
      <el-step title="步骤 1" />
      <el-step title="步骤 2" />
      <el-step title="步骤 3" />
    </el-steps>

    <el-button @click="next">下一步</el-button>
    <h1>{{text}}</h1>
  </el-container>

</template>

<script>
export default {
  name: 'AcXpath',
  data() {
    return {
      active: 0,
      text: 'text'
    }
  },

  methods: {
    next() {
      if (this.active++ > 2) {
        this.active = 0
      }
      switch (this.active) {
        case (0):
          this.text = '0'
          break
        case (1):
          this.text = '1'
          break
        case (2):
          this.text = '2'
          break
        case (3):
          this.text = '3'
          break
      }
    }
  }
}
</script>
<style scoped>

</style>
