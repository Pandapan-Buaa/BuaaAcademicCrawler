<template>
  <el-card class="box-card">
    <div slot="header" class="clearfix">
      <span>学者爬虫系统首页</span>
    </div>
    <div class="text item">
      用户: {{ name }}
    </div>
  </el-card>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'Dashboard',
  computed: {
    ...mapGetters([
      'name',
      'token'
    ])
  }
}
</script>

<style lang="scss" scoped>
.dashboard {
  &-container {
    margin: 30px;
  }
  &-text {
    font-size: 30px;
    line-height: 46px;
  }
}
</style>
