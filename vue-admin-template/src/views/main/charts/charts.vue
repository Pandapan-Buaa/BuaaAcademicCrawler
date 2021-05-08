<template>
  <el-main>
    <el-card class="card1">
      <h2 style="font-weight: 300; text-align: center">学者信息查询</h2>
      <div style="margin-bottom: 20px">
        <el-row class="search">
          <el-col :span="4" :offset="6">
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
            <el-button
              type="primary"
              style="border-radius: 10px;background-color: #38b580;border-color: #38b580"
              icon="el-icon-search"
              @click="getProInfo"
            >获取学者信息
            </el-button>
          </el-col>
          <el-col>
            <h4 style="font-weight: 300; text-align: center">学院老师数量:{{ nameList.length }}</h4>
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
        <el-divider/>
        <b>email</b>: {{ proInfo['email'] }} <br>
        <el-divider/>
        <b>phone</b>:
        {{ proInfo['phone'] }} <br>
        <el-divider/>
        <b>title</b>:
        {{ proInfo['title'] }} <br>
        <el-divider/>
        <b>website</b>:
        {{ proInfo['website'] }} <br>
        <el-divider/>
        <b>papercount</b>
        {{ proInfo['paperCount'] }}
        <el-divider/>
<!--        <b>content</b>:-->
<!--        {{ proInfo['content'] }} <br>-->
      </div>
    </el-card>
    <el-card>
      <div id="chart" style="width:'100%',height:'3.54rem'"/>
    </el-card>
    <el-card>
      <div id="NetWork" style="width:'100%'"/>
    </el-card>
  </el-main>
</template>

<script>
import {getOrganazationName, searchOrganizationData, getAllData, getCollegeName} from '@/api/search'
import {mapGetters} from 'vuex'
import request from '@/utils/request'
import Highcharts from 'highcharts/highstock'
import timeline from 'highcharts/modules/timeline.js'
import networkgraph from 'highcharts/modules/networkgraph.js'

timeline(Highcharts)
networkgraph(Highcharts)

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
      proInfo: {email: '', title: '', phone: '', website: '', content: '', imgsrc: '', paperCount: ''}
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
      getZtInfo1(this.token, this.organizationValue, this.nameValue).then(response => {
        this.proInfo['paperCount'] = response['data']['content'][0]['paperCount']
        this.drawNetWork(response['links'])
      }).catch()
    },
    drawChart(data) {
      const drawdata = this.getShowData(data)
      const metaColor = [
        '#4185F3',
        '#427CDD',
        '#406AB2',
        '#3E5A8E',
        '#3B4A68',
        '#363C46'
      ]
      const colorls = []
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
    drawNetWork(data) {
      // Add the nodes option through an event call. We want to start with the parent
      // item and apply separate colors to each child element, then the same color to
      // grandchildren.
      Highcharts.addEvent(
        Highcharts.seriesTypes.networkgraph,
        'afterSetOptions',
        function (e) {
          var colors = Highcharts.getOptions().colors
          var i = 0
          var nodes = {}
          // e.options.data.forEach(function (link) {
          //   if (link[0] === 'Proto Indo-European') {
          //     nodes['Proto Indo-European'] = {
          //       id: 'Proto Indo-European',
          //       marker: {
          //         radius: 20
          //       }
          //     }
          //     nodes[link[1]] = {
          //       id: link[1],
          //       marker: {
          //         radius: 10
          //       },
          //       color: colors[i++]
          //     }
          //   } else if (nodes[link[0]] && nodes[link[0]].color) {
          //     nodes[link[1]] = {
          //       id: link[1],
          //       color: nodes[link[0]].color
          //     }
          //   }
          // })
          e.options.nodes = Object.keys(nodes).map(function(id) {
            return nodes[id]
          })
        }
      )
      this.chart = Highcharts.chart('NetWork', {
        chart: {
          type: 'networkgraph',
          height: '600px'
        },
        title: {
          text: this.nameValue + '科研关系图'
        },
        // subtitle: {
        //   text: 'A Force-Directed Network Graph in Highcharts'
        // },
        plotOptions: {
          networkgraph: {
            keys: ['from', 'to'],
            layoutAlgorithm: {
              enableSimulation: true
            }
          }
        },
        series: [{
          dataLabels: {
            enabled: true
          },
          data: data
        }]
      })
    },
    getShowData(cont) {
      const ls = []
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

export function getZtInfo1(token, organizationName, nameValue) {
  return request({
    url: '/mongo/getZhituInfo/',
    method: 'get',
    params: {
      scholarName: nameValue,
      orgName: organizationName
    }
  })
}

</script>

<style>
.card2 {
  margin-top: 30px;
  margin-bottom: 30px;
}

.el-select .el-input__inner {
  width: 105%;
  border-radius: 10px;
}

/*Row*/

.row {
  margin-left: -20px;
  *zoom: 1;
}

.row:before, .row:after {
  display: table;
  content: "";
}

.row:after {
  clear: both;
}

.row-fluid [class*="span"] {
  display: block;
  width: 100%;
  min-height: 28px;
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  -ms-box-sizing: border-box;
  box-sizing: border-box;
  float: left;
  margin-left: 2.127659574%;
  *margin-left: 2.0744680846382977%;
}

.row-fluid [class*="span"]:first-child {
  margin-left: 0;
}

.row-fluid input[class*="span"], .row-fluid select[class*="span"], .row-fluid textarea[class*="span"],
.row-fluid .input-prepend [class*="span"], .row-fluid .input-append [class*="span"] {
  display: inline-block;
}

/*Span*/

.span10 {
  width: 780px;
  margin-left: 30%
}

.row-fluid .span10 {
  width: 82.97872339599999%;
  *width: 82.92553190663828%;
}

table .span10 {
  float: none;
  width: 764px;
  margin-left: 0;
}

input.span10, textarea.span10,

  /* Slates */

.slate {
  background: #FFF;
  padding: 10px 20px;
  border: 1px solid #F8F8F8;
  margin-bottom: 20px;
}

.slate h2 {
  font-weight: normal;
  font-family: "Oxygen", sans-serif;
  font-size: 18px;
}

.slate .table tbody tr:hover td,
.slate .table tbody tr:hover th {
  background-color: #EEE;
}

.slate .table th,
.slate .table td {
  border-top: none;
  border-bottom: 1px solid #EBEBEB;
}

.slate .form-inline input,
.slate .form-inline select {
  margin-right: 6px;
}

/*Clearfix*/

.clearfix {
  *zoom: 1;
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}

.clearfix:after {
  clear: both;
}

/*Stat*/

@media (max-width: 767px) {
  .stat-column {
    width: auto;
    float: none;
  }
}

.stat-column {
  width: 30%;
  float: left;
  text-align: center;
  display: block;
  color: #999;
  margin: 0 4%;
  padding: 12px 2%;
}

.stat-column:hover {
  background: #38b580;
  color: #FFF;
  text-decoration: none;
  -webkit-border-radius: 8px;
  -moz-border-radius: 8px;
  border-radius: 8px;
}

.stat-column span {
  font-weight: normal;
  font-family: "Oxygen", sans-serif;
  font-size: 14px;
  display: block;
}

.stat-column span.number {
  font-size: 32px;
  font-weight: normal;
  font-family: "Oxygen", sans-serif;
  margin: 0;
  margin: 14px 0 10px 0;
}
</style>
