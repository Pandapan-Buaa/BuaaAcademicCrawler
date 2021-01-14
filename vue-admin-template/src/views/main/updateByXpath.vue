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
    <el-row v-if="active==1" type="flex" justify="left" class="active">
      <el-col :span="12">
        <el-card class="box-card">
          <el-upload
            ref="upload"
            class="upload-demo"
            action="http://127.0.0.1:8000/api/crawler/file/"
            name="file"
            accept=".txt"
            :on-preview="handlePreview"
            :on-remove="handleRemove"
            :file-list="fileList"
            :auto-upload="true"
            :headers="myHeaders"
            :before-upload="beforeUpload"
            :multiple="true"
          >
            <el-button slot="trigger" size="small" type="primary">选取文件</el-button>
            <!--            <el-button style="margin-left: 10px;" size="small" type="success" @click="submitUpload">上传到服务器</el-button>-->
            <div slot="tip" class="el-upload__tip">请上传包含xpath的txt文件</div>
          </el-upload>
          <div class="text item">导入xpath，处理进度<div v-if="configStatu!=0">共有{{ configSize }}条xpath数据</div></div>
          <el-progress :text-inside="true" :stroke-width="20" :percentage="configStatu" status="success" class="progress" />
          <el-button class="next-button" :disabled="debug && configNextBtn" @click="next">下一步</el-button>
          <el-button class="exc-button" :disabled="debug && configExcBtn" @click="axiosLoadConfig">执行</el-button>
        </el-card>
      </el-col>
    </el-row>
    <el-row v-if="active==2" type="flex" justify="left" class="active">
      <el-col :span="12">
        <el-card class="box-card">
          <div class="text item">更新学者路径，处理进度<div v-if="crawlerStatu!=0">共有{{ crawlerSize }}条数据</div></div>
          <el-progress :text-inside="true" :stroke-width="20" :percentage="crawlerStatu" status="success" class="progress" />
          <el-table
            class="dataTable"
            v-if="!debug || crawlerStatu===100"
            :data="crawlerTableData.slice((currentPage-1)*pageSize,currentPage*pageSize)"
            style="width: 100%"
          >
            <el-table-column
              prop="name"
              label="姓名"
              width="180"
            />
            <el-table-column
              prop="organizationName"
              label="所在大学"
              width="180"
            />
            <el-table-column
              prop="collegeName"
              label="所在院系"
            />
          </el-table>
          <el-pagination
            v-if="!debug || crawlerStatu===100"
            class="pagination"
            align="center"
            :current-page="currentPage"
            :page-sizes="[1,5,10,20]"
            :page-size="pageSize"
            layout="total, sizes, prev, pager, next, jumper"
            :total="crawlerTableData.length"
            @size-change="handleSizeChange"
            @current-change="handleCurrentChange"
          />
          <el-button class="next-button" :disabled="debug && crawlerNextBtn" @click="next">下一步</el-button>
          <el-button class="exc-button" :disabled="debug && crawlerExcBtn" @click="axiosCrawler">执行</el-button>
        </el-card>
      </el-col>
    </el-row>
    <el-row v-if="active==3" type="flex" justify="left" class="active">
      <el-col :span="12">
        <el-card class="box-card">
          <div class="text item">处理特殊数据，处理进度<div v-if="imgCrawlerStatu!=0">共有{{ imgCrawlerSize }}条数据</div></div>
          <el-progress :text-inside="true" :stroke-width="20" :percentage="imgCrawlerStatu" status="success" class="progress" />
          <el-table
            class="dataTable"
            v-if="!debug || imgCrawlerStatu===100"
            :data="imgCrawlerTableData.slice((currentPage-1)*pageSize,currentPage*pageSize)"
            style="width: 100%"
          >
            <el-table-column
              prop="name"
              label="姓名"
              width="180"
            />
            <el-table-column
              prop="organizationName"
              label="所在大学"
              width="180"
            />
            <el-table-column
              prop="collegeName"
              label="所在院系"
            />
          </el-table>
          <el-pagination
            v-if="!debug || imgCrawlerStatu===100"
            class="pagination"
            align="center"
            :current-page="currentPage"
            :page-sizes="[1,5,10,20]"
            :page-size="pageSize"
            layout="total, sizes, prev, pager, next, jumper"
            :total="imgCrawlerTableData.length"
            @size-change="handleSizeChange"
            @current-change="handleCurrentChange"
          />
          <el-button class="next-button" :disabled="debug && imgCrawlerNextBtn" @click="next">下一步</el-button>
          <el-button class="exc-button" :disabled="debug && imgCrawlerExcBtn" @click="axiosImgCrawler">执行</el-button>
        </el-card>
      </el-col>
    </el-row>
    <el-row v-if="active==4" type="flex" justify="left" class="active">
      <el-col :span="12">
        <el-card class="box-card">
          <div class="text item">更新详情，处理进度<div v-if="detailStatu!=0">共有{{ detailSize }}条数据</div></div>
          <el-progress :text-inside="true" :stroke-width="20" :percentage="detailStatu" status="success" class="progress" />
          <el-table
            class="dataTable"
            v-if="!debug || detailStatu===100"
            :data="detailTableData.slice((currentPage-1)*pageSize,currentPage*pageSize)"
            style="width: 100%"
          >
            <el-table-column
              prop="name"
              label="姓名"
              width="180"
            />
            <el-table-column
              prop="organizationName"
              label="所在大学"
              width="180"
            />
            <el-table-column
              prop="collegeName"
              label="所在院系"
            />
          </el-table>
          <el-pagination
            v-if="!debug || detailStatu===100"
            class="pagination"
            align="center"
            :current-page="currentPage"
            :page-sizes="[1,5,10,20]"
            :page-size="pageSize"
            layout="total, sizes, prev, pager, next, jumper"
            :total="detailTableData.length"
            @size-change="handleSizeChange"
            @current-change="handleCurrentChange"
          />
          <el-button class="next-button" :disabled="debug && detailNextBtn" @click="next">下一步</el-button>
          <el-button class="exc-button" :disabled="debug && detailExcBtn" @click="axiosDetail">执行</el-button>
        </el-card>
      </el-col>
    </el-row>
    <el-row v-if="active==5" type="flex" justify="left" class="active">
      <el-col :span="12">
        <el-card class="box-card">
          <div class="text item">更新反爬虫详情，处理进度<div v-if="antiCrawlerStatu!=0">共有{{ antiCrawlerSize }}条数据</div></div>
          <el-progress :text-inside="true" :stroke-width="20" :percentage="antiCrawlerStatu" status="success" class="progress" />
          <el-table
            class="dataTable"
            v-if="!debug || antiCrawlerStatu===100"
            :data="antiCrawlerTableData.slice((currentPage-1)*pageSize,currentPage*pageSize)"
            style="width: 100%"
          >
            <el-table-column
              prop="name"
              label="姓名"
              width="180"
            />
            <el-table-column
              prop="organizationName"
              label="所在大学"
              width="180"
            />
            <el-table-column
              prop="collegeName"
              label="所在院系"
            />
          </el-table>
          <el-pagination
            v-if="!debug || antiCrawlerStatu===100"
            class="pagination"
            align="center"
            :current-page="currentPage"
            :page-sizes="[1,5,10,20]"
            :page-size="pageSize"
            layout="total, sizes, prev, pager, next, jumper"
            :total="antiCrawlerTableData.length"
            @size-change="handleSizeChange"
            @current-change="handleCurrentChange"
          />
          <el-button class="next-button" :disabled="debug && antiCrawlerNextBtn" @click="next">下一步</el-button>
          <el-button class="exc-button" :disabled="debug && antiCrawlerExcBtn" @click="axiosAntiCrawler">执行</el-button>
        </el-card>
      </el-col>
    </el-row>
    <el-row v-if="active==6" type="flex" justify="left" class="active">
      <el-col :span="12">
        <el-card class="box-card">
          <div class="text item">匹配学者信息，处理进度<div v-if="detailMatchStatu!=0">共有{{ detailMatchSize }}条数据</div></div>
          <el-progress :text-inside="true" :stroke-width="20" :percentage="detailMatchStatu" status="success" class="progress" />
          <el-table
            class="dataTable"
            v-if=" !debug || detailMatchStatu===100"
            :data="detailMatchTableData.slice((currentPage-1)*pageSize,currentPage*pageSize)"
            style="width: 100%"
          >
            <el-table-column
              prop="name"
              label="姓名"
              width="180"
            />
            <el-table-column
              prop="organizationName"
              label="所在大学"
              width="180"
            />
            <el-table-column
              prop="collegeName"
              label="所在院系"
            />
          </el-table>
          <el-pagination
            v-if="!debug || detailMatchStatu===100"
            class="pagination"
            align="center"
            :current-page="currentPage"
            :page-sizes="[1,5,10,20]"
            :page-size="pageSize"
            layout="total, sizes, prev, pager, next, jumper"
            :total="detailMatchTableData.length"
            @size-change="handleSizeChange"
            @current-change="handleCurrentChange"
          />
          <el-button class="next-button" :disabled="debug && detailMatchNextBtn" @click="next">下一步</el-button>
          <el-button class="exc-button" :disabled="debug && detailMatchExcBtn" @click="axiosDetailMatch">执行</el-button>
        </el-card>
      </el-col>
    </el-row>
  </el-main>

</template>

<script>
import { mapGetters } from 'vuex'
import { getToken } from '@/utils/auth'
import { updateStatus, loadConfig, loadConfigStatus, crawler, crawlerStatus, imgCrawler, imgCrawlerStatus, detail, detailStatus, antiCrawler, antiCrawlerStatus, detailMatch, detailMatchStatus } from '@/api/updateByXpath'
export default {
  name: 'UpdateByXpath',
  computed: {
    ...mapGetters([
      'token'
    ])
  },
  data() {
    return {
      debug: false,
      active: 1,
      myHeaders: { 'Authorization': 'JWT ' + getToken() },
      configStatu: 0,
      configSize: -1,
      configNextBtn: true,
      configExcBtn: false,
      crawlerStatu: 0,
      crawlerSize: -1,
      crawlerNextBtn: true,
      crawlerExcBtn: false,
      imgCrawlerStatu: 0,
      imgCrawlerSize: -1,
      imgCrawlerNextBtn: true,
      imgCrawlerExcBtn: false,
      detailStatu: 0,
      detailSize: -1,
      detailNextBtn: true,
      detailExcBtn: false,
      antiCrawlerStatu: 0,
      antiCrawlerSize: -1,
      antiCrawlerNextBtn: true,
      antiCrawlerExcBtn: false,
      detailMatchStatu: 0,
      detailMatchSize: -1,
      detailMatchNextBtn: true,
      detailMatchExcBtn: false,
      fileList: [],
      crawlerTableData: [],
      imgCrawlerTableData: [],
      detailTableData: [],
      antiCrawlerTableData: [],
      detailMatchTableData: [],
      currentPage: 1, // 当前页码
      total: 20, // 总条数
      pageSize: 10 // 每页的数据条数

    }
  },
  mounted() {
    this.timer = setInterval(this.refreshConfigStatus, 1000)
  },
  beforeDestroy() {
    clearInterval(this.timer)
  },
  methods: {
    refreshConfigStatus() {
      loadConfigStatus().then(response => {
        var str = response['data']
        var obj = JSON.parse(str)
        this.configStatu = obj.progress
        this.configSize = obj.size
        if (obj.progress === 100 || obj.size === 0) {
          this.configNextBtn = false
        }
      }).catch()
    },
    axiosLoadConfig() {
      this.configExcBtn = true
      loadConfig().then(response => {
        console.log(response)
      }).catch()
    },
    refreshCrawlerStatus() {
      crawlerStatus().then(response => {
        var str = response['data']
        var obj = JSON.parse(str)
        this.crawlerStatu = obj.progress
        this.crawlerSize = obj.size
        console.log(response)
        if (obj.progress === 100) {
          this.crawlerNextBtn = false
        }
      }).catch()
    },
    axiosCrawler() {
      this.crawlerExcBtn = true
      crawler().then(response => {
        console.log(response['data'])
        var str = response['data']
        var obj = JSON.parse(str)
        this.total = obj.len
        for (var key of Object.keys(obj)) {
          var objElement = obj[key]
          var splitStr = objElement.split(' ')
          this.crawlerTableData.push({ organizationName: splitStr[0], collegeName: splitStr[1], name: splitStr[2] })
          // console.log(objElement)
        }
      }).catch()
    },
    refreshImgCrawlerStatus() {
      imgCrawlerStatus().then(response => {
        var str = response['data']
        var obj = JSON.parse(str)
        this.imgCrawlerStatu = obj.progress
        this.imgCrawlerSize = obj.size
        console.log(response)
        if (obj.progress === 100) {
          this.imgCrawlerNextBtn = false
        }
      }).catch()
    },
    axiosImgCrawler() {
      this.imgCrawlerExcBtn = true
      imgCrawler().then(response => {
        console.log(response['data'])
        var str = response['data']
        var obj = JSON.parse(str)
        this.total = obj.len
        for (var key of Object.keys(obj)) {
          var objElement = obj[key]
          var splitStr = objElement.split(' ')
          this.imgCrawlerTableData.push({ organizationName: splitStr[0], collegeName: splitStr[1], name: splitStr[2] })
          // console.log(objElement)
        }
      }).catch()
    },
    refreshDetailStatus() {
      detailStatus().then(response => {
        var str = response['data']
        var obj = JSON.parse(str)
        this.detailStatu = obj.progress
        this.detailSize = obj.size
        console.log(response)
        if (obj.progress === 100) {
          this.detailNextBtn = false
        }
      }).catch()
    },
    axiosDetail() {
      this.detailExcBtn = true
      detail().then(response => {
        // console.log(response['data'])
        var str = response['data']
        var obj = JSON.parse(str)
        this.total = obj.len
        for (var key of Object.keys(obj)) {
          var objElement = obj[key]
          var splitStr = objElement.split(' ')
          this.detailTableData.push({ organizationName: splitStr[0], collegeName: splitStr[1], name: splitStr[2] })
          // console.log(objElement)
        }
      }).catch()
    },
    refreshAntiCrawlerStatus() {
      antiCrawlerStatus().then(response => {
        var str = response['data']
        var obj = JSON.parse(str)
        this.antiCrawlerStatu = obj.progress
        this.antiCrawlerSize = obj.size
        console.log(response)
        if (obj.progress === 100) {
          this.antiCrawlerNextBtn = false
        }
      }).catch()
    },
    axiosAntiCrawler() {
      this.detailExcBtn = true
      antiCrawler().then(response => {
        // console.log(response['data'])
        var str = response['data']
        var obj = JSON.parse(str)
        this.total = obj.len
        for (var key of Object.keys(obj)) {
          var objElement = obj[key]
          var splitStr = objElement.split(' ')
          this.antiCrawlerTableData.push({ organizationName: splitStr[0], collegeName: splitStr[1], name: splitStr[2] })
          // console.log(objElement)
        }
      }).catch()
    },
    refreshDetailMatchStatus() {
      detailMatchStatus().then(response => {
        var str = response['data']
        var obj = JSON.parse(str)
        this.detailMatchStatu = obj.progress
        this.detailMatchSize = obj.size
        // console.log(response)
        if (obj.progress === 100) {
          this.detailMatchNextBtn = false
        }
      }).catch()
    },
    axiosDetailMatch() {
      this.detailMatchExcBtn = true
      detailMatch().then(response => {
        console.log(response['data'])
        var str = response['data']
        var obj = JSON.parse(str)
        this.total = obj.len
        for (var key of Object.keys(obj)) {
          var objElement = obj[key]
          var splitStr = objElement.split(' ')
          this.detailMatchTableData.push({ organizationName: splitStr[0], collegeName: splitStr[1], name: splitStr[2] })
          // console.log(objElement)
        }
      }).catch()
    },
    next() {
      if (this.active++ > 5) {
        this.active = 1
      }
      if (this.active === 2) {
        clearInterval(this.timer)
        this.timer = setInterval(this.refreshCrawlerStatus, 1000)
      } else if (this.active === 3) {
        clearInterval(this.timer)
        this.timer = setInterval(this.refreshImgCrawlerStatus, 1000)
      } else if (this.active === 4) {
        clearInterval(this.timer)
        this.timer = setInterval(this.refreshDetailStatus, 1000)
      } else if (this.active === 5) {
        clearInterval(this.timer)
        this.timer = setInterval(this.refreshAntiCrawlerStatus, 1000)
      } else if (this.active === 6) {
        clearInterval(this.timer)
        this.timer = setInterval(this.refreshDetailMatchStatus, 1000)
      }
      updateStatus().then().catch()
      this.crawlerTableData = []
      this.imgCrawlerTableData = []
      this.detailTableData = []
      this.antiCrawlerTableData = []
      this.detailMatchTableData = []
      this.pageSize = 10
      this.currentPage = 1
    },
    // submitUpload() {
    //   this.$refs.upload.submit()
    // },
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
    },
    // 每页条数改变时触发 选择一页显示多少行
    handleSizeChange(val) {
      // console.log(`每页 ${val} 条`)
      this.currentPage = 1
      this.pageSize = val
    },
    // 当前页改变时触发 跳转其他页
    handleCurrentChange(val) {
      // console.log(`当前页: ${val}`)
      this.currentPage = val
    }
  }
}
</script>
<style scoped>
.active{
  margin-top: 10px;
}
.progress{
  margin-top: 1px;
}
.exc-button{
  margin-top:10px;
  float:right;
  margin-bottom: 10px;
}
.next-button{
  margin-top:10px;
  float:right;
  margin-bottom: 10px;
  margin-left: 10px;
}
.el-upload__tip{
  float:right;
  font-size: 14px;
}

.text {
  font-size: 14px;
}

.item {
  padding: 10px 0;
  margin-top: 10px;
}
.dataTable{
  margin-top:10px;
}
.pagination{
  margin-top:10px;
}
</style>
