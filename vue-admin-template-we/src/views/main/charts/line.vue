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
    <div class="show">
      <header>
        <div class="container header-box">
          <img src="./img/icon2.png" alt="">
          <div class="right">
            <h1>教师成果主页</h1>
            <p><i class="el-icon-user-solid"></i>{{ nameValue }}个人主页</p>
          </div>
        </div>
      </header>
      <div class="container clearfix">
        <div class="main">
          <h2>基本信息
            <div class="right"><a href="#"><img src="./img/icon1.png" alt="">分享Ta的个人主页</a></div>
          </h2>
          <el-row class="info">
            <el-col :span="5">
              <img class="head-pic" :src="proInfo['imgUrl']" alt="">
            </el-col>
            <el-col class="info-box" :span="19">
              <el-row>
                <el-col :span="8">
                  <div class="item">
                    <p><span>姓名：</span>{{ nameValue }}</p>
                    <p><span>单位：</span>{{ organizationValue }}</p>
                    <p><span>院系：</span>{{ collegeValue }}</p>
                    <p><span>研究方向：</span>{{ proInfo['fieldName'] }}</p>
                  </div>
                </el-col>
                <el-col :span="8" :push="8">
                  <div class="item">
                    <p><span>职称：</span>{{ proInfo['title'] }}</p>
                    <p><span>办公地址：</span>{{ people_info.address }}</p>
                    <p><span>座机：</span>{{ proInfo['phone'] }}</p>
                    <p><span>邮箱：</span>{{ proInfo['email'] }}</p>
                  </div>
                </el-col>
              </el-row>
              <div class="intro">
                <p>{{ proInfo['content'] }}
                  <el-button size="media" type="text">展开<i class="el-icon-d-arrow-right"></i></el-button>
                </p>
              </div>
            </el-col>
          </el-row>
          <div class="steps">
            <el-tabs type="border-card">
              <el-tab-pane v-for="(item,index) in step_info" :key="index" :label="item.name">
                <div class="step-box" :style="{width:item.list.length>5 ? (100+20*(item.list.length-5))+'%':'90%'}">
                  <div class="item" v-for="(single,num) in item.list" :key="num">
                    <p><i class="el-icon-date"></i>{{ single.start_time }}-{{ single.end_time }}</p>
                    <div class="circle">
                      0{{ num + 1 }}
                    </div>
                    <p>{{ single.descri }}</p>
                  </div>
                </div>
              </el-tab-pane>
            </el-tabs>
          </div>
          <div class="academic">
            <h2>学术成果（129）
              <div class="right"><a href="#"><img src="./img/icon3.png" alt=""></a></div>
            </h2>
            <el-tabs type="border-card">
              <el-tab-pane label="论文（12）">
                <div class="paper">
                  <div class="paper-top">
                    <p class="year"><span :class="{active:paper_current_year==0}" @click="yearClick(0)">全部</span><span
                      @click="yearClick(item)" :class="{active:paper_current_year==item}"
                      v-for="(item,index) in paper.year_list" :key="index">{{ item }}</span></p>
                    <p class="type"><span :class="{active:paper_current_type==0}" @click="typeClick(0)">全部</span><span
                      @click="typeClick(item)" :class="{active:paper_current_type==item}"
                      v-for="(item,index) in paper.type_list" :key="index">{{ item }}</span></p>
                  </div>
                  <div class="paper-list">
                    <el-row type="flex" class="item" align="middle" v-for="(item,index) in paper.paper_list"
                            :key="index">
                      <el-col :span="20">
                        <h3>
                          <el-tag effect="dark" :type="tag_bg_list[index]" size="small" v-for="(tag,index) in item.tags"
                                  :key="index">{{ tag }}
                          </el-tag>
                          {{ item.title }}
                        </h3>
                        <p>{{ item.descri }}</p>
                        <p class="bottom">
                          <span>发表日期：{{ item.created }}年</span>
                          <span>引用量：{{ item.used }}</span>
                          <span>{{ item.tips }}</span>
                        </p>
                      </el-col>
                      <el-col :span="4" class="btns">
                        <template v-if="item.uploaed">
                          <el-button type="primary" size="small">下载全文</el-button>
                        </template>
                        <template v-else>
                          <p>暂无全文</p>
                          <el-button type="warning" size="small">上传全文</el-button>
                        </template>
                      </el-col>
                    </el-row>
                  </div>
                  <el-pagination
                    small
                    layout="prev, pager, next"
                    :total="50">
                  </el-pagination>
                </div>
              </el-tab-pane>
              <el-tab-pane label="专利(4)">
                <el-row class="patent" :gutter="25">
                  <el-col :span="8" v-for="(item,index) in patent" :key="index">
                    <div class="item">
                      <h3>{{ item.title }}</h3>
                      <p>发表日期：{{ item.created }}</p>
                      <p>发明人：{{ item.peoples }}</p>
                    </div>
                  </el-col>
                </el-row>
                <el-pagination
                  small
                  layout="prev, pager, next"
                  :total="50">
                </el-pagination>

              </el-tab-pane>
              <el-tab-pane label="项目(0)">项目</el-tab-pane>
              <el-tab-pane label="著作(1)">著作</el-tab-pane>
              <el-tab-pane label="获奖(0)">获奖</el-tab-pane>
              <el-tab-pane label="学生获奖(0)">学生获奖</el-tab-pane>
              <el-tab-pane label="著作(1)">著作</el-tab-pane>
            </el-tabs>
          </div>
        </div>
        <div class="side">
          <dl class="notice">
            <dt>个人公告</dt>
            <dd>
              <h2>招生信息</h2>
              <p>
                现招软件工程研究生2名。条件如下;所有考生均须配合考点工作人员进行体温检测,体温低于37.3°C后,方可正常进入考点参加考试。体温异常的考生，可适当休息后听从工作人员安排使用其他设备或其他方式再次测量。若考生体温仍然异常,北京理工大学(
                1107 )报考点将在保障广大考生命安全
                <el-button size="media" type="text">展开<i class="el-icon-d-arrow-right"></i></el-button>
              </p>
            </dd>
            <dd>
              <h2>大数据项目合作</h2>
              <p>
                现招软件工程研究生2名。条件如下;所有考生均须配合考点工作人员进行体温检测,体温低于37.3°C后,方可正常进入考点参加考试。体温异常的考生，可适当休息后听从工作人员安排使用其他设备或其他方式再次测量。若考生体温仍然异常,北京理工大学(
                1107 )报考点将在保障广大考生命安全
                <el-button size="media" type="text">展开<i class="el-icon-d-arrow-right"></i></el-button>
              </p>
            </dd>
          </dl>
          <div class="img-list">
            <figure>
              <figcaption>研究热词</figcaption>
              <img src="./img/img1.png" alt="">
            </figure>
            <figure>
              <figcaption>科研关系图谱</figcaption>
              <img src="./img/img2.png" alt="">
            </figure>
            <figure>
              <figcaption>领域前沿分析</figcaption>
              <img src="./img/img3.png" alt="">
            </figure>
            <figure>
              <figcaption>领域前沿分析</figcaption>
              <img src="./img/img4.png" alt="">
            </figure>
          </div>

        </div>
      </div>
    </div>
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
      proInfo: {
        email: '',
        title: '',
        phone: '',
        website: '',
        content: '',
        imgsrc: '',
        paperCount: '',
        imgUrl: '',
        fieldName: ''
      },
      people_info: {
        name: '张雪华',
        position: '院士',
        unit: '北京航天航空大学',
        address: '北京市学院路37号',
        department: '计算机学院',
        tel: '010-12559876',
        direction: '人工智能、大数据、AI算法、人脸识别、物联网',
        email: 'zhangxuehua@bunn.cn',
        intro: '张雪华，女江苏徐州人，博士学历,全国注册岩土工程师，北京科技大学土木工程系主任、教授，国家自然科学基金和北京市自然科学基金通讯评委，《岩土工程学报》等国内外多个期刊杂志的独立审稿人。[1] 近年来,主持和参与了10余项国家自然科学基金青年和面上项目、科技部"863计划"',
      },
      step_info: [
        {
          name: "工作经历",
          list: [
            {
              start_time: '2015/09',
              end_time: '2020/01',
              descri: '在北京航空航天大学担任讲师一职'
            },
            {
              start_time: '2011/05',
              end_time: '2015/09',
              descri: '在北京大学担任院士一职'
            }
          ]
        },
        {
          name: "教育背景",
          list: [
            {
              start_time: '2015/09',
              end_time: '2020/01',
              descri: '在北京航空航天大学担任讲师一职'
            },
            {
              start_time: '2011/05',
              end_time: '2015/09',
              descri: '在北京大学担任院士一职'
            },
            {
              start_time: '2015/09',
              end_time: '2020/01',
              descri: '在北京航空航天大学担任讲师一职'
            },
            {
              start_time: '2011/05',
              end_time: '2015/09',
              descri: '在北京大学担任院士一职'
            },
            {
              start_time: '2015/09',
              end_time: '2020/01',
              descri: '在北京航空航天大学担任讲师一职'
            },
            {
              start_time: '2011/05',
              end_time: '2015/09',
              descri: '在北京大学担任院士一职'
            }
          ]
        },
        {
          name: "社会兼职",
          list: [
            {
              start_time: '2015/09',
              end_time: '2020/01',
              descri: '在北京航空航天大学担任讲师一职'
            },
            {
              start_time: '2011/05',
              end_time: '2015/09',
              descri: '在北京大学担任院士一职'
            }
          ]
        },
        {
          name: "社会荣誉",
          list: [
            {
              start_time: '2015/09',
              end_time: '2020/01',
              descri: '在北京航空航天大学担任讲师一职'
            },
            {
              start_time: '2011/05',
              end_time: '2015/09',
              descri: '在北京大学担任院士一职'
            }
          ]
        }
      ],
      paper_current_year: 0,
      paper_current_type: 0,
      tag_bg_list: ['default', 'success', 'danger', 'info'],
      paper: {
        year_list: [2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008],
        type_list: ['SEI', 'EI'],
        paper_list: [
          {
            title: '《用一种小波分解和三角函数相结合的坐标建模方法研究》',
            tags: ['SCI', 'EI'],
            created: '2019',
            used: 23,
            tips: 'IF=5.30,JCR分区Q1',
            uploaed: false,
            descri: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt utlabore et dolore magna aliqua. Quis ipsum susLorem ipsum dolor sit amet, consectetur adipiscingelit, sed do eiusmod tempor incididunt ut labore et dolore trices gravida. Risus commodo viverraincididunt ut labore et dolore trices gravida. Risus commodo viverra...'
          },
          {
            title: '《用一种小波分解和三角函数相结合的坐标建模方法研究》',
            tags: ['SCI', 'EI'],
            created: '2019',
            used: 23,
            tips: 'IF=5.30,JCR分区Q1',
            uploaed: true,
            descri: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt utlabore et dolore magna aliqua. Quis ipsum susLorem ipsum dolor sit amet, consectetur adipiscingelit, sed do eiusmod tempor incididunt ut labore et dolore trices gravida. Risus commodo viverraincididunt ut labore et dolore trices gravida. Risus commodo viverra...'
          },
          {
            title: '《用一种小波分解和三角函数相结合的坐标建模方法研究》',
            tags: ['SCI', 'EI'],
            created: '2019',
            used: 23,
            tips: 'IF=5.30,JCR分区Q1',
            uploaed: true,
            descri: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt utlabore et dolore magna aliqua. Quis ipsum susLorem ipsum dolor sit amet, consectetur adipiscingelit, sed do eiusmod tempor incididunt ut labore et dolore trices gravida. Risus commodo viverraincididunt ut labore et dolore trices gravida. Risus commodo viverra...'
          },
          {
            title: '《用一种小波分解和三角函数相结合的坐标建模方法研究》',
            tags: ['SCI', 'EI'],
            created: '2019',
            used: 23,
            tips: 'IF=5.30,JCR分区Q1',
            uploaed: false,
            descri: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt utlabore et dolore magna aliqua. Quis ipsum susLorem ipsum dolor sit amet, consectetur adipiscingelit, sed do eiusmod tempor incididunt ut labore et dolore trices gravida. Risus commodo viverraincididunt ut labore et dolore trices gravida. Risus commodo viverra...'
          }
        ],
      },
      patent: [
        {
          title: '深紫外线LED结构及制作方法',
          created: '2019-12-08',
          peoples: '郝智彪、罗毅、刘洋、望莱'
        },
        {
          title: '深紫外线LED结构及制作方法',
          created: '2019-12-08',
          peoples: '郝智彪、罗毅、刘洋、望莱'
        },
        {
          title: '深紫外线LED结构及制作方法',
          created: '2019-12-08',
          peoples: '郝智彪、罗毅、刘洋、望莱'
        },
        {
          title: '深紫外线LED结构及制作方法',
          created: '2019-12-08',
          peoples: '郝智彪、罗毅、刘洋、望莱'
        },
        {
          title: '深紫外线LED结构及制作方法',
          created: '2019-12-08',
          peoples: '郝智彪、罗毅、刘洋、望莱'
        },
        {
          title: '深紫外线LED结构及制作方法',
          created: '2019-12-08',
          peoples: '郝智彪、罗毅、刘洋、望莱'
        },
        {
          title: '深紫外线LED结构及制作方法',
          created: '2019-12-08',
          peoples: '郝智彪、罗毅、刘洋、望莱'
        },
        {
          title: '深紫外线LED结构及制作方法',
          created: '2019-12-08',
          peoples: '郝智彪、罗毅、刘洋、望莱'
        },
        {
          title: '深紫外线LED结构及制作方法',
          created: '2019-12-08',
          peoples: '郝智彪、罗毅、刘洋、望莱'
        },
        {
          title: '深紫外线LED结构及制作方法',
          created: '2019-12-08',
          peoples: '郝智彪、罗毅、刘洋、望莱'
        },
        {
          title: '深紫外线LED结构及制作方法',
          created: '2019-12-08',
          peoples: '郝智彪、罗毅、刘洋、望莱'
        },
        {
          title: '深紫外线LED结构及制作方法',
          created: '2019-12-08',
          peoples: '郝智彪、罗毅、刘洋、望莱'
        },
        {
          title: '深紫外线LED结构及制作方法',
          created: '2019-12-08',
          peoples: '郝智彪、罗毅、刘洋、望莱'
        },
        {
          title: '深紫外线LED结构及制作方法',
          created: '2019-12-08',
          peoples: '郝智彪、罗毅、刘洋、望莱'
        },
        {
          title: '深紫外线LED结构及制作方法',
          created: '2019-12-08',
          peoples: '郝智彪、罗毅、刘洋、望莱'
        }
      ]
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
        this.proInfo['imgUrl'] = response['data']['content'][0]['avg']
        // var str = ''
        // for (var i = 0; i < response['data']['content'][0]['webFiledVOS'].size(); i++) {
        //   // eslint-disable-next-line eqeqeq
        //   if (i == 0) {
        //     str += response['data']['content'][0]['webFiledVOS'][i]['fieldName']
        //   } else {
        //     str += '、' + response['data']['content'][0]['webFiledVOS'][i]['fieldName']
        //   }
        // }
        // this.proInfo['fieldName'] = response['data']['content'][0]['webFiledVOS'][0]['fieldName']
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
          e.options.nodes = Object.keys(nodes).map(function (id) {
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
