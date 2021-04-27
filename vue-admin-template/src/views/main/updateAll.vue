<template>
  <el-main>
    <el-row>
      <el-col :span="24">
        <el-steps :active="active" finish-status="success" simple style="margin-top: 10px">
          <el-step title="步骤1" />
          <el-step title="步骤2" />
          <el-step title="步骤3" />
        </el-steps>
      </el-col>
    </el-row>
    <el-row v-if="active===1" type="flex" justify="left" class="active">
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <h2 style="font-weight: 300; text-align: center">更新详情</h2>
        </div>
        <div class="text item">
          <h3 style="font-weight: 300; text-align: center">处  理  进  度</h3>
          <div v-if="detailStatu!=0">共有{{ detailSize }}条数据</div>
        </div>
        <el-progress
          :text-inside="true"
          :stroke-width="20"
          :percentage="detailStatu"
          status="success"
          class="progress"
        />
        <el-table
          v-if="!debug || detailStatu===100"
          class="dataTable"
          :data="detailTableData.slice((currentPage-1)*pageSize,currentPage*pageSize)"
          style="width: 100%"
          align="center"
        >
          <el-table-column
            prop="name"
            label="姓名"
            width="200"
            align="center"
          />
          <el-table-column
            prop="organizationName"
            label="所在大学"
            width="500"
            align="center"
          />
          <el-table-column
            prop="collegeName"
            label="所在院系"
            width="300"
            align="center"
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
        <el-button class="next-button" :disabled="debug && detailNextBtn" type="primary" @click="next">下一步</el-button>
        <el-button class="exc-button" :disabled="debug && detailExcBtn" type="success" @click="axiosDetail">执行</el-button>
      </el-card>
    </el-row>
    <el-row v-if="active===2" type="flex" justify="left" class="active">
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <h2 style="font-weight: 300; text-align: center">更新反爬虫详情</h2>
        </div>
        <div class="text item">
          <h3 style="font-weight: 300; text-align: center">处  理  进  度</h3>
          <div v-if="antiCrawlerStatu!=0">共有{{ antiCrawlerSize }}条数据</div></div>
        <el-progress :text-inside="true" :stroke-width="20" :percentage="antiCrawlerStatu" status="success" class="progress" />
        <el-table
          v-if="!debug || antiCrawlerStatu===100"
          class="dataTable"
          :data="antiCrawlerTableData.slice((currentPage-1)*pageSize,currentPage*pageSize)"
          style="width: 100%"
          align="center"
        >
          <el-table-column
            prop="name"
            label="姓名"
            width="200"
            align="center"
          />
          <el-table-column
            prop="organizationName"
            label="所在大学"
            width="500"
            align="center"
          />
          <el-table-column
            prop="collegeName"
            label="所在院系"
            width="300"
            align="center"
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
        <el-button class="next-button" :disabled="debug && antiCrawlerNextBtn" type="primary" @click="next">下一步</el-button>
        <el-button class="exc-button" :disabled="debug && antiCrawlerExcBtn" type="success" @click="axiosAntiCrawler">执行</el-button>
      </el-card>
    </el-row>
    <el-row v-if="active===3" type="flex" justify="left" class="active">
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <h2 style="font-weight: 300; text-align: center">匹配学者信息</h2>
        </div>
        <div class="text item">
          <h3 style="font-weight: 300; text-align: center">处  理  进  度</h3>
          <div v-if="detailMatchStatu!=0">共有{{ detailMatchSize }}条数据</div></div>
        <el-progress :text-inside="true" :stroke-width="20" :percentage="detailMatchStatu" status="success" class="progress" />
        <el-table
          v-if=" !debug || detailMatchStatu===100"
          class="dataTable tb-edit"
          :data="detailMatchTableData.slice((currentPage-1)*pageSize,currentPage*pageSize)"
          style="width: 100%"
          highlight-current-row
          @row-click="handleCurrent"
        >
          <el-table-column
            prop="mongoid"
            label="MongoId"
            width="200"
            align="center"
          />
          <el-table-column
            prop="zhituid"
            label="知兔Id"
            width="200"
            align="center"
          />
          <el-table-column label="姓名">
            <template scope="scope">
              <el-input v-model="scope.row.name" size="small" placeholder="请输入内容" @change="handleEdit(scope.$index, scope.row)" /> <span>{{ scope.row.name }}</span>
            </template>
          </el-table-column>
          <el-table-column label="所在大学">
            <template scope="scope">
              <el-input v-model="scope.row.organizationName" size="small" placeholder="请输入内容" @change="handleEdit(scope.$index, scope.row)" /> <span>{{ scope.row.organizationName }}</span>
            </template>
          </el-table-column>
          <el-table-column label="所在院系">
            <template scope="scope">
              <el-input v-model="scope.row.collegeName" size="small" placeholder="请输入内容" @change="handleEdit(scope.$index, scope.row)" /> <span>{{ scope.row.collegeName }}</span>
            </template>
          </el-table-column>
          <el-table-column label="职称">
            <template scope="scope">
              <el-input v-model="scope.row.title" size="small" placeholder="请输入内容" @change="handleEdit(scope.$index, scope.row)" /> <span>{{ scope.row.title }}</span>
            </template>
          </el-table-column>
          <el-table-column label="邮箱">
            <template scope="scope">
              <el-input v-model="scope.row.email" size="small" placeholder="请输入内容" @change="handleEdit(scope.$index, scope.row)" /> <span>{{ scope.row.email }}</span>
            </template>
          </el-table-column>
          <el-table-column label="电话">
            <template scope="scope">
              <el-input v-model="scope.row.phone" size="small" placeholder="请输入内容" @change="handleEdit(scope.$index, scope.row)" /> <span>{{ scope.row.phone }}</span>
            </template>
          </el-table-column>
          <el-table-column label="操作">
            <template scope="scope">
              <el-button type="primary" size="small" @click="handleUpdate(scope.$index, scope.row)">上传修改</el-button>
              <!--              <el-button size="small" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>-->
            </template>
          </el-table-column>
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
        <el-button class="next-button" :disabled="debug && detailMatchNextBtn" type="primary" @click="next">下一步</el-button>
        <el-button class="exc-button" :disabled="debug && detailMatchExcBtn" type="success" @click="axiosDetailMatch">执行</el-button>
      </el-card>
    </el-row>
    <el-row v-if="errorTableData.length != 0" type="flex" justify="left" class="active">
      <el-col>
        <el-card class="box-card">
          <div class="text item">
            <h3 style="font-weight: 300; text-align: center">错 误 日 志</h3>
            <div>共有{{ errorTableData.length }}条数据</div>
          </div>
          <el-table
            :data="errorTableData"
            style="width: 100%"
            max-height="300"
          >

            <el-table-column
              fixed
              prop="id"
              label="id"
              width="150"
            />
            <el-table-column
              prop="error"
              label="错误提示"
              width="1000"
            />
          </el-table>
        </el-card>
      </el-col>
    </el-row>
  </el-main>

</template>
<script>
import { getCollegeName, getOrganazationName } from '@/api/search'
import {
  antiCrawler,
  antiCrawlerStatus,
  detail,
  detailMatch,
  detailMatchStatus,
  detailStatus, updateStatus,
  updateScholar,
  getErrors
} from '@/api/updateAll'
import { mapGetters } from 'vuex'

export default {
  name: 'UpdateByOrganization',
  computed: {
    ...mapGetters([
      'name',
      'token'
    ])
  },
  data() {
    return {
      timeout: 1500,
      debug: true,
      active: 1,
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
      detailTableData: [],
      antiCrawlerTableData: [],
      detailMatchTableData: [],
      errorTableData: [],
      currentPage: 1, // 当前页码
      total: 20, // 总条数
      pageSize: 10 // 每页的数据条数
    }
  },
  watch: {
    organizationValue(newValue, oldValue) {
      getCollegeName(this.token, newValue).then(response => {
        this.colleges = response['data']
        this.collegeList = this.colleges.map(item => {
          return { value: `${item}`, label: `${item}` }
        })
      }).catch()
    }
  },
  mounted() {
    clearInterval(this.timer)
    getOrganazationName(this.token).then(response => {
      this.organizations = response['data']
      this.organizationList = this.organizations.map(item => {
        return { value: `${item}`, label: `${item}` }
      })
    }).catch()
  },
  beforeDestroy() {
    clearInterval(this.timer)
  },
  methods: {
    handleCurrent(row, event, column) {
      // console.log(row, event, column)
    },
    handleEdit(index, row) {
      // console.log(index, row)
    },
    handleUpdate(index, row) {
      console.log(row)
      var id = row.mongoid
      var name = row.name
      var organizationName = row.organizationName
      var collegeName = row.collegeName
      var title = row.title
      var email = row.email
      var phone = row.phone

      updateScholar(id, name, organizationName, collegeName, title, email, phone
      ).then(
        this.$message({
          message: '修改成功 ' + id + ' ' + name,
          type: 'success'
        }))
    },
    fillErrorTable() {
      getErrors(this.name).then(response => {
        var str = response['data']
        var obj = JSON.parse(str)
        console.log(obj.length)
        for (var key of Object.keys(obj)) {
          var objElement = obj[key]
          this.errorTableData.push({ id: key, error: objElement })
        }
      }).catch()
    },
    refreshDetailStatus() {
      detailStatus(this.name).then(response => {
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
      clearInterval(this.timer)
      this.timer = setInterval(this.refreshDetailStatus, this.timeout)
      this.detailExcBtn = true
      detail(this.name).then(response => {
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
        this.fillErrorTable()
      }).catch()
    },
    refreshAntiCrawlerStatus() {
      antiCrawlerStatus(this.name).then(response => {
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
      clearInterval(this.timer)
      this.timer = setInterval(this.refreshAntiCrawlerStatus, this.timeout)
      this.antiCrawlerExcBtn = true
      antiCrawler(this.name).then(response => {
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
        this.fillErrorTable()
      }).catch()
    },
    refreshDetailMatchStatus() {
      detailMatchStatus(this.name).then(response => {
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
      clearInterval(this.timer)
      this.timer = setInterval(this.refreshDetailMatchStatus, this.timeout)
      this.detailMatchExcBtn = true
      detailMatch(this.name).then(response => {
        console.log(response['data'])
        var str = response['data']
        var obj = JSON.parse(str)
        this.total = obj.len
        for (var key of Object.keys(obj)) {
          var objElement = obj[key]
          var splitStr = objElement.split(' ')
          // this.detailMatchTableData.push({ organizationName: splitStr[0], collegeName: splitStr[1], name: splitStr[2] })
          this.detailMatchTableData.push({ organizationName: splitStr[0], collegeName: splitStr[1], name: splitStr[2], title: splitStr[3], email: splitStr[4], phone: splitStr[5], mongoid: splitStr[6], zhituid: splitStr[7] })
          // console.log(objElement)
        }
        this.fillErrorTable()
      }).catch()
    },
    next() {
      if (this.active++ > 2) {
        // this.active = 1
        // this.timer = setInterval(this.refreshDetailStatus, 1000)
        location.reload()
      }
      // if (this.active === 2) {
      //
      // } else if (this.active === 3) {
      //
      // }
      updateStatus(this.name).then().catch()
      clearInterval(this.timer)
      this.errorTableData = []
      this.detailTableData = []
      this.antiCrawlerTableData = []
      this.detailMatchTableData = []
      this.pageSize = 10
      this.currentPage = 1
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
.active {
  margin-top: 10px;
}

.progress {
  margin-top: 1px;
}

.exc-button {
  margin-top: 10px;
  float: right;
  margin-bottom: 10px;
}

.next-button {
  margin-top: 10px;
  float: right;
  margin-bottom: 10px;
  margin-left: 10px;
}

.el-upload__tip {
  float: right;
  font-size: 14px;
}

.text {
  font-size: 14px;
}

.item {
  padding: 10px 0;
  margin-top: 1px;
}

.dataTable {
  margin-top: 10px;
}

.pagination {
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
  width: 1450px;
  margin-left: auto;
  margin-right: auto;
  margin: auto;
}

.tb-edit .el-input {
  display: none
}
.tb-edit .current-row .el-input {
  display: block
}
.tb-edit .current-row .el-input+span {
  display: none
}

</style>
