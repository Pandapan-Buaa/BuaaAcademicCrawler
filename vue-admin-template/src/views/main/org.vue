<template>
  <el-main>
    <!--    <h4>总爬取高校数:{{ organizationList.length }}</h4>-->
    <!--    <h4>总爬取学者数:{{ total }}</h4>-->

    <el-card class="card1">
      <h2 style="font-weight: 300; text-align: center">学校数据分析</h2>
      <el-divider />
      <div style="margin-bottom: 20px">
        <el-row class="search">
          <el-col :span="4" :offset="8">
            <el-select
              v-model="organizationValue"
              filterable
              reserve-keyword
              placeholder="请输入待查询高校名称"
              style="border-radius: 25%"
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
            <el-select v-model="fieldName" filterable placeholder="选择分析的领域名字">
              <el-option
                v-for="item in fields"
                :key="item.value"
                :label="item.label"
                :value="item[0]"
              />
            </el-select>
          </el-col>
          <el-col :span="4">
            <el-button
              type="primary"
              style="border-radius: 10px;background-color: #38b580;border-color: #38b580"
              icon="el-icon-search"
              @click="searchScholarCount"
            >搜索
            </el-button>
          </el-col>
        </el-row>
        <br>
        <br>
        <div style="text-align: center">
          <h1>{{ organizationValue }}数据可视化</h1>
        </div>
        <el-row>
          <el-col :span="6">
            <div id="Bar" style="width:'1000px',height:'3.54rem'" />
          </el-col>
          <el-col :span="6">
            <div id="Bar1" style="width:'1000px',height:'3.54rem'" />
          </el-col>
          <el-col :span="6">
            <div id="Bar2" style="width:'1000px',height:'3.54rem'" />
          </el-col>
          <el-col :span="6">
            <div id="Bar3" style="width:'1000px',height:'3.54rem'" />
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="12">
            <div id="WordCloud" />
          </el-col>
          <el-col :span="12">
            <div id="Pie" />
          </el-col>
        </el-row>
      </div>
    </el-card>
  </el-main>
</template>

<script>
import { getOrganazationName, searchOrganizationData, getAllData, getCollegeName } from '@/api/search'
import { mapGetters } from 'vuex'
import Highcharts from 'highcharts/highstock'
import request from '@/utils/request'
import wordcloud from 'highcharts/modules/wordcloud.js'

wordcloud(Highcharts)
export default {
  computed: {
    ...mapGetters([
      'token'
    ])
  },
  data() {
    return {
      tableData: [],
      tableData2: [],
      organizationValue: '', // 选中
      organizationValue2: '',
      organizationList: [], // select框数据
      collegeValue: '', // 选中
      fieldValue: '',
      collegeList: [],
      organizations: [],
      colleges: [],
      total: 0,
      fieldName: '',
      fieldId: 0,
      fields: [],
      word_cloud: [],
      paperCount_list: [],
      projectCount_list: [],
      patentCount_list: [],
      innovationIndex_list: [],
      pieData: []
    }
  },
  watch: {
    organizationValue(newValue, oldValue) {
      // getCollegeName(this.token, newValue).then(response => {
      //   this.colleges = response['data']
      //   // console.log(response)
      //   this.collegeList = this.colleges.map(item => {
      //     return {value: `${item}`, label: `${item}`}
      //   })
      // }).catch()
      this.fieldName = ''
      getZtOrgInfo(this.token, newValue, 0).then(response => {
        this.fields = response['fields']
        this.innovationIndex_list = response['innovationIndex_list']
        this.paperCount_list = response['paperCount_list']
        this.patentCount_list = response['patentCount_list']
        this.projectCount_list = response['projectCount_list']
        this.word_cloud = response['word_cloud']
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
        return { value: `${item}`, label: `${item}` }
      })
      // console.log(this.list)
    }).catch()

    getAllData(this.token).then(response => {
      // this.tableData[0].count = response['count']
      this.total = response['count']
    }).catch()
  },
  methods: {
    searchScholarCount() {
      if (this.fieldName !== '') {
        for (let i = 0; i < this.fields.length; i++) {
          if (this.fields[i][0] === this.fieldName) {
            this.fieldId = this.fields[i][1]
            break
          }
        }
        getZtOrgInfo(this.token, this.organizationValue, this.fieldId).then(response => {
          this.innovationIndex_list = response['innovationIndex_list']
          this.paperCount_list = response['paperCount_list']
          this.patentCount_list = response['patentCount_list']
          this.projectCount_list = response['projectCount_list']
          this.word_cloud = response['word_cloud']
        }).catch()
      }
      this.getPieData()
      this.drawBar()
      this.drawBar1()
      this.drawBar2()
      this.drawBar3()
      this.drawWordCloud()
      this.drawPie()
      // getZtInfo2(this.token, this.organizationValue, this.collegeValue).then(response => {
      //   this.drawBar(response['statistic_data']['paperCountList'])
      //   this.drawBar1(response['statistic_data']['projectCountList'])
      // }).catch()
    },
    getPieData() {
      this.pieData = []
      for (let i = 0; i < this.word_cloud.length; i++) {
        this.pieData.push(
          {
            name: this.word_cloud[i]['name'],
            y: this.word_cloud[i]['weight']
          }
        )
      }
    },
    drawBar() {
      var chart = Highcharts.chart('Bar', {
        chart: {
          type: 'column'
        },
        title: {
          text: '学者论文数量Top10'
        },
        subtitle: {
          text: '数据截止 2021-03'
        },
        xAxis: {
          type: 'category',
          labels: {
            rotation: -45 // 设置轴标签旋转角度
          }
        },
        yAxis: {
          min: 0,
          title: {
            text: '篇'
          }
        },
        legend: {
          enabled: false
        },
        tooltip: {
          pointFormat: '论文数量: <b>{point.y:.1f} 篇</b>'
        },
        series: [{
          name: '论文数量',
          data: this.paperCount_list,
          dataLabels: {
            enabled: true,
            rotation: -90,
            color: '#FFFFFF',
            align: 'right',
            format: '{point.y:.f}', // :.1f 为保留 1 位小数
            y: 10
          }
        }]
      })
    },
    drawBar1() {
      var chart = Highcharts.chart('Bar1', {
        chart: {
          type: 'column'
        },
        title: {
          text: '学者项目数量Top10'
        },
        subtitle: {
          text: '数据截止 2021-03'
        },
        xAxis: {
          type: 'category',
          labels: {
            rotation: -45 // 设置轴标签旋转角度
          }
        },
        yAxis: {
          min: 0,
          title: {
            text: '个'
          }
        },
        legend: {
          enabled: false
        },
        tooltip: {
          pointFormat: '项目数量: <b>{point.y:.1f} 个</b>'
        },
        series: [{
          name: '项目数量',
          data: this.projectCount_list,
          dataLabels: {
            enabled: true,
            rotation: -90,
            color: '#FFFFFF',
            align: 'right',
            format: '{point.y:.f}', // :.1f 为保留 1 位小数
            y: 10
          }
        }]
      })
    },
    drawBar2() {
      var chart = Highcharts.chart('Bar2', {
        chart: {
          type: 'column'
        },
        title: {
          text: '学者专利数量Top10'
        },
        subtitle: {
          text: '数据截止 2021-03'
        },
        xAxis: {
          type: 'category',
          labels: {
            rotation: -45 // 设置轴标签旋转角度
          }
        },
        yAxis: {
          min: 0,
          title: {
            text: '个'
          }
        },
        legend: {
          enabled: false
        },
        tooltip: {
          pointFormat: '专利数量: <b>{point.y:.1f} 个</b>'
        },
        series: [{
          name: '专利数量',
          data: this.patentCount_list,
          dataLabels: {
            enabled: true,
            rotation: -90,
            color: '#FFFFFF',
            align: 'right',
            format: '{point.y:.f}', // :.1f 为保留 1 位小数
            y: 10
          }
        }]
      })
    },
    drawBar3() {
      var chart = Highcharts.chart('Bar3', {
        chart: {
          type: 'column'
        },
        title: {
          text: '学者创新指数Top10'
        },
        subtitle: {
          text: '数据截止 2021-03'
        },
        xAxis: {
          type: 'category',
          labels: {
            rotation: -45 // 设置轴标签旋转角度
          }
        },
        yAxis: {
          min: 0,
          title: {
            text: '分数'
          }
        },
        legend: {
          enabled: false
        },
        tooltip: {
          pointFormat: '创新指数: <b>{point.y:.1f} </b>'
        },
        series: [{
          name: '创新指数',
          data: this.innovationIndex_list,
          dataLabels: {
            enabled: true,
            rotation: -90,
            color: '#FFFFFF',
            align: 'right',
            format: '{point.y:.1f}', // :.1f 为保留 1 位小数
            y: 10
          }
        }]
      })
    },
    drawWordCloud() {
      Highcharts.chart('WordCloud', {
        series: [{
          type: 'wordcloud',
          data: this.word_cloud
        }],
        title: {
          text: '研究领域词云图'
        }
      })
    },
    drawPie() {
      Highcharts.chart('Pie', {
        chart: {
          plotBackgroundColor: null,
          plotBorderWidth: null,
          plotShadow: false,
          type: 'pie'
        },
        title: {
          text: '研究领域饼图'
        },
        tooltip: {
          pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        plotOptions: {
          pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
              enabled: false
            },
            showInLegend: true
          }
        },
        series: [{
          name: 'Brands',
          colorByPoint: true,
          data: this.pieData
          //   [{
          //   name: 'Chrome',
          //   y: 61.41,
          //   sliced: true,
          //   selected: true
          // }, {
          //   name: 'Internet Explorer',
          //   y: 11.84
          // }, {
          //   name: 'Firefox',
          //   y: 10.85
          // }, {
          //   name: 'Edge',
          //   y: 4.67
          // }, {
          //   name: 'Safari',
          //   y: 4.18
          // }, {
          //   name: 'Other',
          //   y: 7.05
          // }]
        }]
      })
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

export function getZtInfo2(token, organizationName, collegeName) {
  return request({
    url: '/mongo/getPerson/',
    method: 'get',
    params: {
      organizationName: organizationName,
      database: 'scholar_temp'
    }
  })
}

export function getZtOrgInfo(token, organizationName, fieldId) {
  return request({
    url: '/mongo/getZhituOrgInfo/',
    method: 'get',
    params: {
      orgName: organizationName,
      fieldId: fieldId,
      num: 10
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
<style>
.img-list figure {
  margin: 40px 0 0;
}

.img-list figcaption {
  text-align: center;
  font-size: 20px;
  margin-bottom: 15px;
}

.img-list figure img {
  display: block;
  width: 100%;
}

.notice dt {
  line-height: 50px;
  background: #0078F2;
  color: #fff;
  text-align: center;
  font-size: 22px;
}

.notice dd {
  border: 1px solid #d7dae2;
  border-top: none;
  margin: 0;
  padding: 10px 15px 0;
}

.notice dd p {
  line-height: 1.7;
  font-size: 14px;
  color: #565656;
}

</style>

<style>
.show .el-tabs--border-card {
  box-shadow: none;
  background: #F6F5F5;
}

.show .el-tabs--border-card > .el-tabs__header {
  background: #fff;
}

.show .el-tabs--border-card > .el-tabs__header .el-tabs__item.is-active {
  color: #fff;
  background-color: #0078F2;
  border-right-color: #0078F2;
  border-left-color: #0078F2;
}

.show .academic .el-tabs--border-card {
  border: none;
  background: #fff;
}

.show .academic .el-tabs--border-card > .el-tabs__header {
  border: 1px solid #e5e5e5;
}

.show .academic .el-tabs--border-card > .el-tabs__content {
  padding: 15px 0;
}
</style>

<style scoped>
header {
  padding: 8px 0;
  margin-bottom: 20px;
  background: url('img/head-bg.png') no-repeat center / auto 100%;
}

.header-box {
  display: flex;
  align-items: center;
}

.header-box > img {
  width: 66px;
  height: 50px;
  margin-right: 15px;
}

.header-box .right {
  flex: 1;
}

.header-box h1 {
  font-weight: 500;
  font-size: 24px;
  color: #fff;
  margin-bottom: 15px;
}

.header-box p {
  color: #fff;
}

.header-box p i {
  margin-right: 6px;
}

.main {
  width: 1010px;
  float: left;
}

.side {
  width: 320px;
  float: right;
}

h2 {
  font-size: 18px;
  border-left: 4px solid #0078F2;
  margin-bottom: 20px;
  padding-left: 9px;
  line-height: 1;
}

h2 .right {
  float: right;
}

h2 .right a {
  display: flex;
  align-items: center;
  font-weight: 500;
  text-decoration: none;
  color: #0078F2;
}

h2 .right a img {
  width: 18px;
  height: 18px;
  margin-right: 8px;
}

.info {
  border: 1px solid #d7dae2;
  padding: 0 15px;
  margin-top: 20px;
}

.info .head-pic {
  padding-top: 15px !important;
  width: 88%;
  display: block;
}

.info-box .item {
  font-size: 16px;
}

.info-box .item span {
  color: #999;
}

.info-box .item p {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.info-box .intro {
  line-height: 1.7;
  color: #454545;
}

.info-box .intro .el-button {
  color: #0078F2;
}

.steps {
  margin-top: 20px;
}

.step-box {
  position: relative;
  display: flex;
  margin: 0 auto;
}

.step-box .item {
  position: relative;
  flex: 1;
  text-align: center;
  padding: 0 10px;
}

.step-box .item:after {
  content: '';
  display: block;
  background: #0078F2;
  height: 3px;
  width: 100%;
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  left: 0;
}

.step-box:after, .step-box::before {
  content: '';
  display: block;
  background: #0078F2;
  height: 6px;
  border: 2px solid #DCEAF7;
  border-radius: 50%;
  width: 6px;
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  left: 0;
  z-index: 1;
}

.step-box::before {
  left: auto;
  right: -7px;
}

.step-box p {
  font-size: 14px;
  line-height: 1.6;
  min-height: 60px;
  display: flex;
  justify-content: center;
}

.step-box p:first-child {
  color: #0078F2;
  align-items: center;
  padding: 0 0 60px;
}

.step-box .circle {
  width: 40px;
  height: 40px;
  line-height: 40px;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  z-index: 2;
  background: #0078F2;
  border: 5px solid #DCEAF7;
  border-radius: 50%;
  color: #fff;
}

.steps .el-tab-pane {
  overflow-x: auto;
}

.academic {
  margin-top: 26px;
}

.paper-top p span {
  font-size: 14px;
  margin: 0 15px;
  cursor: pointer;
}

.paper-top p span.active {
  color: #0078F2;
  font-weight: 700;
}

.paper-list .item {
  border: 1px solid #d7dae2;
  padding: 0px 16px;
  margin: 0 0 15px;
}

.paper-list h3 {
  font-weight: 500;
}

.paper-list h3 .el-tag {
  margin-right: 5px;
}

.paper-list .btns {
  text-align: center;
}

.paper-list p {
  line-height: 1.7;
  font-size: 14px;
  color: #565656;
}

.paper-list p.bottom span {
  color: #999;
  margin-right: 20px;
  font-size: 13px;
}

.patent .item {
  border: 1px solid #d7dae2;
  padding: 5px 15px 12px;
  margin-bottom: 20px;
}

.patent .item h3 {
  font-weight: 500;
}

.patent .item p {
  font-size: 14px;
  color: #898989;
  line-height: 1;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.clearfix:after {
  content: '';
  display: block;
  height: 0;
  line-height: 0;
  overflow: hidden;
  clear: both;
}

.container {
  width: 1360px;
  margin: 0 auto;
}
</style>
