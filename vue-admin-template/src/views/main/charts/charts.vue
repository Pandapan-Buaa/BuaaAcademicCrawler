<template>
  <el-main>
    <el-card class="card1">
      <h2>学者信息查询</h2>
      <div style="margin-bottom: 20px">
        <el-row class="search">
          <el-col :span="4">
            <el-select
              v-model="organizationValue"
              filterable
              reserve-keyword
              placeholder="请输入待查询高校名称"
            >
              <el-option
                v-for="item in organizationList"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              />
            </el-select>
          </el-col>
          <el-col :span="4">
            <el-select v-model="collegeValue" filterable placeholder="请选择待查询院系名称">
              <el-option
                v-for="item in collegeList"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              />
            </el-select>
          </el-col>
          <el-col :span="4">
            <el-select v-model="nameValue" filterable placeholder="请选择学者名字">
              <el-option
                v-for="item in nameList"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              />
            </el-select>
          </el-col>
          <el-col :span="4">
            <el-button type="primary" icon="el-icon-search" @click="getProInfo">获取学者信息</el-button>
          </el-col>
          <el-col>
            <h4>学院老师数量:{{ nameList.length }}</h4>
          </el-col>
        </el-row>
      </div>
    </el-card>
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <span>学者简历</span>
        <!--        <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>-->
      </div>
      <div class="text item">
        <b>name</b>: {{ nameValue }}<br>
        <el-divider></el-divider>
        <b>email</b>: {{ proInfo['email'] }} <br>
        <el-divider></el-divider>
        <b>phone</b>:
        {{ proInfo['phone'] }} <br>
        <el-divider></el-divider>
        <b>title</b>:
        {{ proInfo['title'] }} <br>
        <el-divider></el-divider>
        <b>website</b>:
        {{ proInfo['website'] }} <br>
        <el-divider></el-divider>
        <b>content</b>:
        {{ proInfo['content'] }} <br>
      </div>
    </el-card>
    <el-card>
      <div id="chart" style="width:'100%',height:'3.54rem'"/>
    </el-card>
  </el-main>
</template>

<script>
import {getOrganazationName, searchOrganizationData, getAllData, getCollegeName} from '@/api/search'
import {mapGetters} from 'vuex'
import request from '@/utils/request'
import Highcharts from 'highcharts/highstock'
import timeline from 'highcharts/modules/timeline.js'

timeline(Highcharts)

export default {
  data() {
    return {
      tableData: [],
      tableData2: [],
      organizationValue: '', // 选中
      organizationValue2: '',
      organizationList: [], // select框数据
      collegeValue: '', // 选中
      collegeList: [],
      organizations: [],
      colleges: [],
      total: 0,
      nameValue: '',
      nameList: [],
      proInfo: {email: '', title: '', phone: '', website: '', content: ''}
    }
  },
  watch: {
    organizationValue(newValue, oldValue) {
      getCollegeName(this.token, newValue).then(response => {
        this.colleges = response['data']
        // console.log(response)
        this.collegeList = this.colleges.map(item => {
          return {value: `${item}`, label: `${item}`}
        })
      }).catch()
    },
    collegeValue(newValue, oldValue) {
      getNames(this.token, this.organizationValue, newValue).then(response => {
        this.names = response['data']
        this.nameList = this.names.map(item => {
          return {value: `${item}`, label: `${item}`}
        })
      }).catch()
    }
  },
  mounted() {
    getOrganazationName(this.token).then(response => {
      // console.log(response)
      // console.log(response['data'])
      this.organizations = response['data']
      // console.log(this.states)
      // console.log(this.value.length)
      this.organizationList = this.organizations.map(item => {
        return {value: `${item}`, label: `${item}`}
      })
      // console.log(this.list)
    }).catch()

    getAllData(this.token).then(response => {
      // this.tableData[0].count = response['count']
      this.total = response['count']
    }).catch()
  },
  methods: {
    getProInfo() {
      getInfo(this.token, this.organizationValue, this.collegeValue, this.nameValue).then(response => {
        // console.log(response)
        this.proInfo['phone'] = response['data']['phone'][0]
        this.proInfo['email'] = response['data']['email'][0]
        this.proInfo['title'] = response['data']['title'][0]
        this.proInfo['content'] = response['data']['content'][0]
        this.proInfo['website'] = response['data']['website'][0]
        this.drawChart(response['data']['specContent'])
      }).catch()
    },
    drawChart(data) {
      let drawdata = this.getShowData(data)
      let metaColor = [
        '#4185F3',
        '#427CDD',
        '#406AB2',
        '#3E5A8E',
        '#3B4A68',
        '#363C46'
      ]
      let colorls = []
      for (var i = 0; i < drawdata.length; i++) {
        colorls.push(metaColor[i % 6])
      }
      this.chart = new Highcharts.Chart('chart', {
        chart: {
          type: 'timeline'
        },
        xAxis: {
          visible: false
        },
        yAxis: {
          visible: false
        },
        title: {
          text: this.nameValue + '个人经历'
        },
        subtitle: {
          text: '数据来源：<a href="' + this.proInfo['website'] + '" target="_blank">' + this.nameValue + '个人主页' + '</a>'
        },
        colors: colorls,
        series: [{
          data: drawdata
        }]
      })
    },
    getShowData(cont) {
      let ls = []
      for (var i = 0; i < cont.length; i++) {
        var description = ''
        for (var j = 0; j < cont[i]['pos'].length; j++) {
          description = description + cont[j]['pos']
        }
        ls.push({
          label: cont[i]['timeKey'].toString(),
          name: cont[i]['pos'][0],
          description: description
        })
      }
      return ls
    },
    searchScholarCount() {
      searchOrganizationData(this.token, this.organizationValue, this.collegeValue).then(response => {
        // console.log(response)
        this.tableData.push({
          organizationName: response['organizationName'],
          collegeName: response['collegeName'],
          count: response['count'],
          total_count: response['total_count']
        })
        this.uniqueForCard1(this.tableData)
      }).catch()
    },
    uniqueForCard1(obj) {
      // 去掉重复选取的数据
      for (var i = 0; i < obj.length; i++) {
        for (var j = i + 1; j < obj.length;) {
          if (obj[i].organizationName === obj[j].organizationName && obj[i].collegeName === obj[j].collegeName) { // 通过photoid属性进行匹配；
            obj.splice(j, 1)// 去除重复的对象；
          } else {
            j++
          }
        }
      }
    },
    searchCollegeCount() {
      getCollegeName(this.token, this.organizationValue2).then(response => {
        // console.log(response)
        var count = response['data'].length
        this.tableData2.push({
          organizationName: this.organizationValue2,
          count: count,
          collegeList: response['data'].join('，')
        })
        this.uniqueForCard2(this.tableData2)
      }).catch()
    },
    uniqueForCard2(obj) {
      // 去掉重复选取的数据
      for (var i = 0; i < obj.length; i++) {
        for (var j = i + 1; j < obj.length;) {
          if (obj[i].organizationName === obj[j].organizationName) { // 通过photoid属性进行匹配；
            obj.splice(j, 1)// 去除重复的对象；
          } else {
            j++
          }
        }
      }
    }
  }
}

export function getNames(token, organizationName, collegeName) {
  return request({
    url: '/mongo/getPerson/',
    method: 'get',
    params: {
      organizationName: organizationName,
      collegeName: collegeName,
      database: 'scholar_temp'
    }
  })
}

export function getInfo(token, organizationName, collegeName, nameValue) {
  return request({
    url: '/mongo/getPersonInfo/',
    method: 'get',
    params: {
      organizationName: organizationName,
      collegeName: collegeName,
      database: 'scholar_temp',
      name: nameValue
    }
  })
}
</script>

<style>

.card2 {
  margin-top: 30px;
  margin-bottom: 30px;
}
</style>
