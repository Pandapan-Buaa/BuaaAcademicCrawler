<template>
  <el-main>
    <el-row>
      <el-col :span="24">
        <el-steps :space="2000" :active="active" finish-status="success">
          <el-step title="步骤 1" />
          <el-step title="步骤 2" />
          <el-step title="步骤 3" />
          <el-step title="步骤 4" />
          <el-step title="步骤 5" />
          <el-step title="步骤 6" />
        </el-steps>
      </el-col>
    </el-row>
    <el-row v-if="active==1" type="flex" justify="left" class="active1">
      <el-col :span="12">
        <el-card class="box-card">
          <el-upload
            ref="upload"
            class="upload-demo"
            action="http://127.0.0.1:8000/api/mongo/file/"
            name="file"
            accept=".txt,.xls,.xlsx"
            :on-preview="handlePreview"
            :on-remove="handleRemove"
            :file-list="fileList"
            :auto-upload="false"
            :headers="myHeaders"
            :before-upload="beforeUpload"
            :multiple="true"
          >
            <el-button slot="trigger" size="small" type="primary">选取文件</el-button>
            <el-button style="margin-left: 10px;" size="small" type="success" @click="submitUpload">上传到服务器</el-button>
            <div slot="tip" class="el-upload__tip">请上传包含xpath的txt文件</div>
          </el-upload>
          <el-button v-if="active<6" class="next-button" @click="next">下一步</el-button>
        </el-card>
      </el-col>
    </el-row>
  </el-main>

</template>

<script>
import { mapGetters } from 'vuex'
import { getToken } from '@/utils/auth'
export default {
  name: 'UpdateByXpath',
  computed: {
    ...mapGetters([
      'token'
    ])
  },
  data() {
    return {
      active: 1,
      myHeaders: { 'Authorization': 'JWT ' + getToken() },
      fileList: []

    }
  },

  methods: {
    next() {
      if (this.active++ > 5) {
        this.active = 1
      }
    },
    submitUpload() {
      this.$refs.upload.submit()
    },
    handleRemove(file, fileList) {
      console.log(file, fileList)
    },
    handlePreview(file) {
      console.log(file)
    },
    beforeUpload(file) {
      console.log(file)
      var testmsg = file.name.substring(file.name.lastIndexOf('.') + 1)
      const extension = testmsg === 'txt'
      // const extension2 = testmsg === 'xlsx'
      // const extension3 = testmsg === 'txt'
      // const isLt2M = file.size / 1024 / 1024 < 10
      if (!extension) {
        this.$message({
          message: '上传文件只能是 txt格式!',
          type: 'warning'
        })
      }
      // if (!isLt2M) {
      //   this.$message({
      //     message: '上传文件大小不能超过 10MB!',
      //     type: 'warning'
      //   })
      // }
      // return (extension || extension2) && isLt2M
      return extension
    }
  }
}
</script>
<style scoped>
.active1{
  margin-top: 10px;
}
.next-button{
  margin-top:10px;
  float:right;
  margin-bottom: 10px;
}
.el-upload__tip{
  float:right;
  font-size: 14px;
}
</style>
