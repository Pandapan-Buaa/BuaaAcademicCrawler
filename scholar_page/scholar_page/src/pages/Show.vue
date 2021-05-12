<template>
  <div class="show">
    <header>
      <div class="container header-box">
        <img src="~img/icon2.png" alt="">
        <div class="right">
          <h1>教师成果主页</h1>
          <p><i class="el-icon-user-solid"></i>{{people_info.name}}个人主页</p>
        </div>
      </div>
    </header>
    <div class="container clearfix">
      <div class="main">
        <h2>基本信息 <div class="right"><a href="#"><img src="~img/icon1.png" alt="">分享Ta的个人主页</a></div></h2>
        <el-row class="info">
          <el-col :span="5">
            <img class="head-pic" src="~img/head.png" alt="">
          </el-col>
          <el-col class="info-box" :span="19">
            <el-row >
              <el-col :span="8">
                <div class="item">
                  <p><span>姓名：</span>{{people_info.name}}</p>
                  <p><span>单位：</span>{{people_info.unit}}</p>
                  <p><span>院系：</span>{{people_info.department}}</p>
                  <p><span>研究方向：</span>{{people_info.direction}}</p>
                </div>
              </el-col>
              <el-col :span="8"  :push="8">
                <div class="item">
                  <p><span>职称：</span>{{people_info.position}}</p>
                  <p><span>办公地址：</span>{{people_info.address}}</p>
                  <p><span>座机：</span>{{people_info.tel}}</p>
                  <p><span>邮箱：</span>{{people_info.email}}</p>
                </div>
              </el-col>
            </el-row>
            <div class="intro">
              <p>{{people_info.intro}} <el-button size="media" type="text">展开<i class="el-icon-d-arrow-right"></i></el-button></p>
            </div>
          </el-col>
        </el-row>
        <div class="steps">
          <el-tabs type="border-card">
            <el-tab-pane v-for="(item,index) in step_info" :key="index" :label="item.name">
              <div class="step-box" :style="{width:item.list.length>5 ? (100+20*(item.list.length-5))+'%':'90%'}">
                <div class="item" v-for="(single,num) in item.list" :key="num">
                  <p><i class="el-icon-date"></i>{{single.start_time}}-{{single.end_time}}</p>
                  <div class="circle">
                    0{{num+1}}
                  </div>
                  <p>{{single.descri}}</p>
                </div>
              </div>
            </el-tab-pane>
          </el-tabs>
        </div>
        <div class="academic">
          <h2>学术成果（129） <div class="right"><a href="#"><img src="~img/icon3.png" alt=""></a></div></h2>
          <el-tabs type="border-card">
            <el-tab-pane label="论文（12）">
              <div class="paper">
                <div class="paper-top">
                  <p class="year"><span :class="{active:paper_current_year==0}" @click="yearClick(0)">全部</span><span @click="yearClick(item)" :class="{active:paper_current_year==item}" v-for="(item,index) in paper.year_list" :key="index">{{item}}</span></p>
                  <p class="type"><span :class="{active:paper_current_type==0}" @click="typeClick(0)">全部</span><span @click="typeClick(item)" :class="{active:paper_current_type==item}" v-for="(item,index) in paper.type_list" :key="index">{{item}}</span></p>
                </div>
                <div class="paper-list">
                  <el-row type="flex" class="item" align="middle" v-for="(item,index) in paper.paper_list" :key="index">
                    <el-col :span="20">
                      <h3><el-tag effect="dark" :type="tag_bg_list[index]" size="small" v-for="(tag,index) in item.tags" :key="index">{{tag}}</el-tag>{{item.title}}</h3>
                      <p>{{item.descri}}</p>
                      <p class="bottom">
                        <span>发表日期：{{item.created}}年</span>
                        <span>引用量：{{item.used}}</span>
                        <span>{{item.tips}}</span>
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
                    <h3>{{item.title}}</h3>
                    <p>发表日期：{{item.created}}</p>
                    <p>发明人：{{item.peoples}}</p>
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
            <p>现招软件工程研究生2名。条件如下;所有考生均须配合考点工作人员进行体温检测,体温低于37.3°C后,方可正常进入考点参加考试。体温异常的考生，可适当休息后听从工作人员安排使用其他设备或其他方式再次测量。若考生体温仍然异常,北京理工大学( 1107 )报考点将在保障广大考生命安全<el-button size="media" type="text">展开<i class="el-icon-d-arrow-right"></i></el-button></p>
          </dd>
          <dd>
            <h2>大数据项目合作</h2>
            <p>现招软件工程研究生2名。条件如下;所有考生均须配合考点工作人员进行体温检测,体温低于37.3°C后,方可正常进入考点参加考试。体温异常的考生，可适当休息后听从工作人员安排使用其他设备或其他方式再次测量。若考生体温仍然异常,北京理工大学( 1107 )报考点将在保障广大考生命安全<el-button size="media" type="text">展开<i class="el-icon-d-arrow-right"></i></el-button></p>
          </dd>
        </dl>
        <div class="img-list">
          <figure>
            <figcaption>研究热词</figcaption>
            <img src="~img/img1.png" alt="">
          </figure>
          <figure>
            <figcaption>科研关系图谱</figcaption>
            <img src="~img/img2.png" alt="">
          </figure>
          <figure>
            <figcaption>领域前沿分析</figcaption>
            <img src="~img/img3.png" alt="">
          </figure>
          <figure>
            <figcaption>领域前沿分析</figcaption>
            <img src="~img/img4.png" alt="">
          </figure>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
export default {
  data(){
    return{
      people_info:{
        name:'张雪华',
        position:'院士',
        unit:'北京航天航空大学',
        address:'北京市学院路37号',
        department:'计算机学院',
        tel:'010-12559876',
        direction:'人工智能、大数据、AI算法、人脸识别、物联网',
        email:'zhangxuehua@bunn.cn',
        intro:'张雪华，女江苏徐州人，博士学历,全国注册岩土工程师，北京科技大学土木工程系主任、教授，国家自然科学基金和北京市自然科学基金通讯评委，《岩土工程学报》等国内外多个期刊杂志的独立审稿人。[1] 近年来,主持和参与了10余项国家自然科学基金青年和面上项目、科技部"863计划"',
      },
      step_info:[
        {
          name:"工作经历",
          list:[
            {
              start_time:'2015/09',
              end_time:'2020/01',
              descri:'在北京航空航天大学担任讲师一职'
            },
            {
              start_time:'2011/05',
              end_time:'2015/09',
              descri:'在北京大学担任院士一职'
            }
          ]
        },
        {
          name:"教育背景",
          list:[
            {
              start_time:'2015/09',
              end_time:'2020/01',
              descri:'在北京航空航天大学担任讲师一职'
            },
            {
              start_time:'2011/05',
              end_time:'2015/09',
              descri:'在北京大学担任院士一职'
            },
            {
              start_time:'2015/09',
              end_time:'2020/01',
              descri:'在北京航空航天大学担任讲师一职'
            },
            {
              start_time:'2011/05',
              end_time:'2015/09',
              descri:'在北京大学担任院士一职'
            },
            {
              start_time:'2015/09',
              end_time:'2020/01',
              descri:'在北京航空航天大学担任讲师一职'
            },
            {
              start_time:'2011/05',
              end_time:'2015/09',
              descri:'在北京大学担任院士一职'
            }
          ]
        },
        {
          name:"社会兼职",
          list:[
            {
              start_time:'2015/09',
              end_time:'2020/01',
              descri:'在北京航空航天大学担任讲师一职'
            },
            {
              start_time:'2011/05',
              end_time:'2015/09',
              descri:'在北京大学担任院士一职'
            }
          ]
        },
        {
          name:"社会荣誉",
          list:[
            {
              start_time:'2015/09',
              end_time:'2020/01',
              descri:'在北京航空航天大学担任讲师一职'
            },
            {
              start_time:'2011/05',
              end_time:'2015/09',
              descri:'在北京大学担任院士一职'
            }
          ]
        }
      ],
      paper_current_year:0,
      paper_current_type:0,
      tag_bg_list:['default','success','danger','info'],
      paper:{
        year_list:[2021,2020,2019,2018,2017,2016,2015,2014,2013,2012,2011,2010,2009,2008],
        type_list:['SEI','EI'],
        paper_list:[
          {
            title:'《用一种小波分解和三角函数相结合的坐标建模方法研究》',
            tags:['SCI','EI'],
            created:'2019',
            used:23,
            tips:'IF=5.30,JCR分区Q1',
            uploaed:false,
            descri:'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt utlabore et dolore magna aliqua. Quis ipsum susLorem ipsum dolor sit amet, consectetur adipiscingelit, sed do eiusmod tempor incididunt ut labore et dolore trices gravida. Risus commodo viverraincididunt ut labore et dolore trices gravida. Risus commodo viverra...'
          },
          {
            title:'《用一种小波分解和三角函数相结合的坐标建模方法研究》',
            tags:['SCI','EI'],
            created:'2019',
            used:23,
            tips:'IF=5.30,JCR分区Q1',
            uploaed:true,
            descri:'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt utlabore et dolore magna aliqua. Quis ipsum susLorem ipsum dolor sit amet, consectetur adipiscingelit, sed do eiusmod tempor incididunt ut labore et dolore trices gravida. Risus commodo viverraincididunt ut labore et dolore trices gravida. Risus commodo viverra...'
          },
          {
            title:'《用一种小波分解和三角函数相结合的坐标建模方法研究》',
            tags:['SCI','EI'],
            created:'2019',
            used:23,
            tips:'IF=5.30,JCR分区Q1',
            uploaed:true,
            descri:'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt utlabore et dolore magna aliqua. Quis ipsum susLorem ipsum dolor sit amet, consectetur adipiscingelit, sed do eiusmod tempor incididunt ut labore et dolore trices gravida. Risus commodo viverraincididunt ut labore et dolore trices gravida. Risus commodo viverra...'
          },
          {
            title:'《用一种小波分解和三角函数相结合的坐标建模方法研究》',
            tags:['SCI','EI'],
            created:'2019',
            used:23,
            tips:'IF=5.30,JCR分区Q1',
            uploaed:false,
            descri:'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt utlabore et dolore magna aliqua. Quis ipsum susLorem ipsum dolor sit amet, consectetur adipiscingelit, sed do eiusmod tempor incididunt ut labore et dolore trices gravida. Risus commodo viverraincididunt ut labore et dolore trices gravida. Risus commodo viverra...'
          }
        ],
      },
      patent:[
        {
          title:'深紫外线LED结构及制作方法',
          created:'2019-12-08',
          peoples:'郝智彪、罗毅、刘洋、望莱'
        },
        {
          title:'深紫外线LED结构及制作方法',
          created:'2019-12-08',
          peoples:'郝智彪、罗毅、刘洋、望莱'
        },
        {
          title:'深紫外线LED结构及制作方法',
          created:'2019-12-08',
          peoples:'郝智彪、罗毅、刘洋、望莱'
        },
        {
          title:'深紫外线LED结构及制作方法',
          created:'2019-12-08',
          peoples:'郝智彪、罗毅、刘洋、望莱'
        },
        {
          title:'深紫外线LED结构及制作方法',
          created:'2019-12-08',
          peoples:'郝智彪、罗毅、刘洋、望莱'
        },
        {
          title:'深紫外线LED结构及制作方法',
          created:'2019-12-08',
          peoples:'郝智彪、罗毅、刘洋、望莱'
        },
        {
          title:'深紫外线LED结构及制作方法',
          created:'2019-12-08',
          peoples:'郝智彪、罗毅、刘洋、望莱'
        },
        {
          title:'深紫外线LED结构及制作方法',
          created:'2019-12-08',
          peoples:'郝智彪、罗毅、刘洋、望莱'
        },
        {
          title:'深紫外线LED结构及制作方法',
          created:'2019-12-08',
          peoples:'郝智彪、罗毅、刘洋、望莱'
        },
        {
          title:'深紫外线LED结构及制作方法',
          created:'2019-12-08',
          peoples:'郝智彪、罗毅、刘洋、望莱'
        },
        {
          title:'深紫外线LED结构及制作方法',
          created:'2019-12-08',
          peoples:'郝智彪、罗毅、刘洋、望莱'
        },
        {
          title:'深紫外线LED结构及制作方法',
          created:'2019-12-08',
          peoples:'郝智彪、罗毅、刘洋、望莱'
        },
        {
          title:'深紫外线LED结构及制作方法',
          created:'2019-12-08',
          peoples:'郝智彪、罗毅、刘洋、望莱'
        },
        {
          title:'深紫外线LED结构及制作方法',
          created:'2019-12-08',
          peoples:'郝智彪、罗毅、刘洋、望莱'
        },
        {
          title:'深紫外线LED结构及制作方法',
          created:'2019-12-08',
          peoples:'郝智彪、罗毅、刘洋、望莱'
        }
      ]
    }
  },
  methods:{
    yearClick(year){
      this.paper_current_year = year
    },
    typeClick(type){
      this.paper_current_type = type
    }
  }
}
</script>

<style>
.img-list figure{
  margin:40px 0 0;
}
.img-list figcaption{
  text-align: center;
  font-size:20px;
  margin-bottom:15px;
}
.img-list figure img{
  display: block;
  width:20%;
}


.notice dt{
  line-height:50px;
  background: #0078F2;
  color:#fff;
  text-align: center;
  font-size:22px;
}
.notice dd{
  border:1px solid #d7dae2;
  border-top:none;
  margin:0;
  padding:10px 15px 0;
}
.notice dd p{
  line-height:1.7;
  font-size:14px;
  color:#565656;
}

</style>

<style>
.show .el-tabs--border-card{
  box-shadow:none;
  background:#F6F5F5;
}
.show .el-tabs--border-card>.el-tabs__header{
  background: #fff;
}
.show .el-tabs--border-card>.el-tabs__header .el-tabs__item.is-active{
  color:#fff;
  background-color: #0078F2;
  border-right-color: #0078F2;
  border-left-color: #0078F2;
}
.show .academic .el-tabs--border-card{
  border:none;
  background:#fff;
}
.show .academic .el-tabs--border-card>.el-tabs__header{
  border:1px solid #e5e5e5;
}
.show .academic .el-tabs--border-card>.el-tabs__content{
  padding:15px 0;
}
</style>

<style scoped>
header{
  padding:8px 0;
  margin-bottom:20px;
  background: url('~img/head-bg.png') no-repeat center / auto 100%;
}
.header-box{
  display: flex;
  align-items: center;
}
.header-box>img{
  width:66px;
  height:50px;
  margin-right:15px;
}
.header-box .right{
  flex:1;
}
.header-box h1{
  font-weight:500;
  font-size:24px;
  color:#fff;
  margin-bottom:15px;
}
.header-box p{
  color:#fff;
}
.header-box p i{
  margin-right:6px;
}
.main{
  width:1010px;
  float: left;
}
.side{
  width:320px;
  float:right;
}
h2{
  font-size:18px;
  border-left:4px solid #0078F2;
  margin-bottom:20px;
  padding-left:9px;
  line-height:1;
}
h2 .right{
  float:right;
}
h2 .right a{
  display: flex;
  align-items: center;
  font-weight:500;
  text-decoration: none;
  color:#0078F2;
}
h2 .right a img{
  width:18px;
  height:18px;
  margin-right:8px;
}
.info{
  border: 1px solid #d7dae2;
  padding:0 15px;
  margin-top:20px;
}
.info .head-pic{
  padding-top:15px !important;
  width:88%;
  display: block;
}
.info-box .item{
  font-size:16px;
}
.info-box .item span{
  color:#999;
}
.info-box .item p{
  overflow:hidden;
	text-overflow:ellipsis;
	white-space:nowrap;
}
.info-box .intro{
  line-height: 1.7;
  color:#454545;
}
.info-box .intro .el-button{
  color:#0078F2;
}

.steps{
  margin-top:20px;
}
.step-box{
  position: relative;
  display: flex;
  margin:0 auto;
}
.step-box .item{
  position:relative;
  flex:1;
  text-align: center;
  padding:0 10px;
}
.step-box .item:after{
  content: '';
  display: block;
  background: #0078F2;
  height:3px;
  width:100%;
  position: absolute;
  top:50%;
  transform: translateY(-50%);
  left:0;
}

.step-box:after,.step-box::before{
  content: '';
  display: block;
  background: #0078F2;
  height:6px;
  border:2px solid #DCEAF7;
  border-radius:50%;
  width:6px;
  position: absolute;
  top:50%;
  transform: translateY(-50%);
  left:0;
  z-index:1;
}
.step-box::before{
  left:auto;
  right:-7px;
}
.step-box p{
  font-size:14px;
  line-height:1.6;
  min-height:60px;
  display: flex;
  justify-content: center;
}
.step-box p:first-child{
  color:#0078F2;
  align-items:center;
  padding:0 0 60px;
}
.step-box .circle{
  width:40px;
  height:40px;
  line-height:40px;
  position: absolute;
  left:50%;
  top:50%;
  transform:translate(-50%,-50%);
  z-index:2;
  background: #0078F2;
  border:5px solid #DCEAF7;
  border-radius:50%;
  color:#fff;
}
.steps .el-tab-pane{
  overflow-x:auto;
}

.academic{
  margin-top:26px;
}

.paper-top p span{
  font-size:14px;
  margin:0 15px;
  cursor:pointer;
}
.paper-top p span.active{
  color:#0078F2;
  font-weight:700;
}

.paper-list .item{
  border:1px solid #d7dae2;
  padding:0px 16px;
  margin:0 0 15px;
}

.paper-list h3{
  font-weight:500;
}
.paper-list h3 .el-tag{
  margin-right:5px;
}

.paper-list .btns{
  text-align:center;
}

.paper-list p{
  line-height:1.7;
  font-size:14px;
  color:#565656;
}
.paper-list p.bottom span{
  color:#999;
  margin-right:20px;
  font-size:13px;
}
.patent .item{
  border:1px solid #d7dae2;
  padding:5px 15px 12px;
  margin-bottom:20px;
}
.patent .item h3{
  font-weight:500;
}
.patent .item p{
  font-size:14px;
  color:#898989;
  line-height:1;
  overflow:hidden;
  text-overflow:ellipsis;
  white-space:nowrap;
}

</style>
