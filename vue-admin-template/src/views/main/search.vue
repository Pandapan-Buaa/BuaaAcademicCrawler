<template>
  <el-main>
    <div class="row">
      <div class="span10">
        <div class="slate clearfix">
          <a class="stat-column">
            <span class="number">{{ organizationList.length }}</span>
            <span>总爬取高校数</span>
          </a>
          <a class="stat-column">
            <span class="number">{{ total }}</span>
            <span>总爬取学者数</span>
          </a>
        </div>
      </div>
    </div>
    <!--    <h4>总爬取高校数:{{ organizationList.length }}</h4>-->
    <!--    <h4>总爬取学者数:{{ total }}</h4>-->

    <el-card class="card1">
      <h2 style="font-weight: 300; text-align: center">详细爬取数量查询</h2>
      <el-divider></el-divider>
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
          <el-col :span="4" >
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
            <el-button type="primary" style="border-radius: 10px;background-color: #38b580;border-color: #38b580" icon="el-icon-search" @click="searchScholarCount">搜索</el-button>
          </el-col>
        </el-row>
      </div>
      <el-table
        :data="tableData"
        stripe
        style="width: 100%"
      >
        <el-table-column
          prop="organizationName"
          label="高校名称"
          width="180"
        />
        <el-table-column
          prop="collegeName"
          label="学院名称"
        />
        <el-table-column
          prop="count"
          label="学院已爬取数量"
        />
        <el-table-column
          prop="total_count"
          label="高校爬取总数量"
        />
      </el-table>
    </el-card>
    <el-card class="card2">
      <h2 style="font-weight: 300; text-align: center">高校爬取学院数查询</h2>
      <el-divider></el-divider>
      <div style="margin-bottom: 20px">
        <el-row class="search">
          <el-col :span="4" :offset="9">
              <el-select
                v-model="organizationValue2"
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
            <el-button type="primary"  style="border-radius: 10px;background-color: #38b580;border-color: #38b580" icon="el-icon-search" @click="searchCollegeCount">搜索</el-button>
          </el-col>

        </el-row>
      </div>
      <el-table
        :data="tableData2"
        stripe
        style="width: 100%"
      >
        <el-table-column
          prop="organizationName"
          label="高校名称"
          width="180"
        />
        <el-table-column
          prop="count"
          label="学院总数"
        />
        <el-table-column
          prop="collegeList"
          label="学院列表"
        />
      </el-table>
    </el-card>
  </el-main>
</template>

<script>
import { getOrganazationName, searchOrganizationData, getAllData, getCollegeName } from '@/api/search'
import { mapGetters } from 'vuex'

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
      collegeList: [],
      organizations: [],
      colleges: [],
      total: 0
    }
  },
  watch: {
    organizationValue(newValue, oldValue) {
      getCollegeName(this.token, newValue).then(response => {
        this.colleges = response['data']
        // console.log(response)
        this.collegeList = this.colleges.map(item => {
          return { value: `${item}`, label: `${item}` }
        })
      }).catch()
    }
  },
  mounted() {
    // clearInterval(this.timer)
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

.row{margin-left:-20px;*zoom:1;}.row:before,.row:after{display:table;content:"";}
.row:after{clear:both;}
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
.row-fluid input[class*="span"],.row-fluid select[class*="span"],.row-fluid textarea[class*="span"],
.row-fluid .input-prepend [class*="span"],.row-fluid .input-append [class*="span"]{display:inline-block;}

/*Span*/

.span10{width:780px; margin-left: 30%}
.row-fluid .span10{width:82.97872339599999%;*width:82.92553190663828%;}
table .span10{float:none;width:764px;margin-left:0;}
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
