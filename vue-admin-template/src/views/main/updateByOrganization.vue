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
        <el-select
          v-model="organizationValue"
          filterable
          reserve-keyword
          placeholder="请输入待查询高校名称"
          style="border-radius: 25%; margin:auto"
        >
          <el-option
            v-for="item in organizationList"
            :key="item.value"
            :label="item.label"
            :value="item.value"
          />
        </el-select>
        <el-select v-model="collegeValue" filterable placeholder="请选择待查询院系名称">
          <el-option
            v-for="item in collegeList"
            :key="item.value"
            :label="item.label"
            :value="item.value"
          />
        </el-select>
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
        <el-button class="exc-button" :disabled="debug && antiCrawlerNextBtn" type="success" @click="axiosAntiCrawler">执行</el-button>
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
        <el-table :data="tableData" class="tb-edit" style="width: 100%" highlight-current-row @row-click="handleCurrent">
          <el-table-column label="日期" width="180">
            <template scope="scope">
              <el-input v-model="scope.row.date" size="small" placeholder="请输入内容" @change="handleEdit(scope.$index, scope.row)" /> <span>{{ scope.row.date }}</span>
            </template>
          </el-table-column>
          <el-table-column label="姓名" width="180">
            <template scope="scope">
              <el-input v-model="scope.row.name" size="small" placeholder="请输入内容" @change="handleEdit(scope.$index, scope.row)" /> <span>{{ scope.row.name }}</span>
            </template>
          </el-table-column>
          <el-table-column prop="address" label="地址">
            <template scope="scope">
              <el-input v-model="scope.row.address" size="small" placeholder="请输入内容" @change="handleEdit(scope.$index, scope.row)" /> <span>{{ scope.row.address }}</span>
            </template>
          </el-table-column>
          <el-table-column label="操作">
            <template scope="scope">
              <!--<el-button size="small" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>-->
              <el-button size="small" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
        <el-table
          v-if=" !debug || detailMatchStatu===100"
          class="dataTable"
          :data="detailMatchTableData.slice((currentPage-1)*pageSize,currentPage*pageSize)"
          style="width: 100%"
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
          <el-table-column
            prop="title"
            label="职称"
            width="300"
            align="center"
          />
          <el-table-column
            prop="email"
            label="邮箱"
            width="300"
            align="center"
          />
          <el-table-column
            prop="phone"
            label="电话"
            width="300"
            align="center"
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
        <el-button class="next-button" :disabled="debug && detailMatchNextBtn" type="primary" @click="next">下一步</el-button>
        <el-button class="exc-button" :disabled="debug && detailMatchExcBtn" type="success" @click="axiosDetailMatch">执行</el-button>
      </el-card>
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
  detailStatus, updateStatus
} from '@/api/updateByOrganization'

export default {
  name: 'UpdateByOrganization',
  data() {
    return {
      debug: false,
      active: 1,
      organizationValue: '', // 选中
      organizationList: [], // select框数据
      collegeValue: '', // 选中
      collegeList: [],
      organizations: [],
      colleges: [],
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
      currentPage: 1, // 当前页码
      total: 20, // 总条数
      pageSize: 10, // 每页的数据条数
      tableData: [{
        date: '2016-05-02',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1518 弄'
      }, {
        date: '2016-05-04',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1517 弄'
      }, {
        date: '2016-05-01',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1519 弄'
      }, {
        date: '2016-05-03',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1516 弄'
      }]
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
    this.timer = setInterval(this.refreshDetailStatus, 1000)
    getOrganazationName(this.token).then(response => {
      this.organizations = response['data']
      this.organizationList = this.organizations.map(item => {
        return { value: `${item}`, label: `${item}` }
      })
    }).catch()
  },
  methods: {
    handleCurrent(row, event, column) {
      console.log(row, event, column, event.currentTarget)
    },
    handleEdit(index, row) {
      console.log(index, row)
    },
    handleDelete(index, row) {
      console.log(index, row)
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
      detail(this.organizationValue, this.collegeValue).then(response => {
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
      antiCrawler(this.organizationValue, this.collegeValue).then(response => {
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
      detailMatch(this.organizationValue, this.collegeValue).then(response => {
        console.log(response['data'])
        var str = response['data']
        var obj = JSON.parse(str)
        this.total = obj.len
        for (var key of Object.keys(obj)) {
          var objElement = obj[key]
          var splitStr = objElement.split(' ')
          this.detailMatchTableData.push({ organizationName: splitStr[0], collegeName: splitStr[1], name: splitStr[2], title: splitStr[3], email: splitStr[4], phone: splitStr[5], mongoid: splitStr[6], zhituid: splitStr[7] })
          // console.log(objElement)
        }
      }).catch()
    },
    next() {
      if (this.active++ > 2) {
        this.active = 1
      }
      if (this.active === 2) {
        clearInterval(this.timer)
        this.timer = setInterval(this.refreshAntiCrawlerStatus, 1000)
      } else if (this.active === 3) {
        clearInterval(this.timer)
        this.timer = setInterval(this.refreshDetailMatchStatus, 1000)
      }
      updateStatus().then().catch()
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
  margin-top: 10px;
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
body {
  font-family: Helvetica Neue, Helvetica, PingFang SC, Hiragino Sans GB, Microsoft YaHei, SimSun, sans-serif;
  overflow: auto;
  font-weight: 400;
  -webkit-font-smoothing: antialiased;
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
