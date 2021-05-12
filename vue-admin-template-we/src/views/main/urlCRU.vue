<template>
  <el-main>

    <el-card class="card1">
      <h2>新增url</h2>
      <div style="margin-bottom: 20px">
        <el-row class="search">
          <el-form ref="Form1" :model="ruleForm1" :rules="rules1" label-width="100px" class="demo-ruleForm">
            <el-form-item label="高校名称" prop="organizationName">
              <el-input v-model="ruleForm1.organizationName" />
            </el-form-item>
            <el-form-item label="学院名称" prop="collegeName">
              <el-input v-model="ruleForm1.collegeName" />
            </el-form-item>
            <el-form-item label="URL" prop="url">
              <el-input v-model="ruleForm1.url" />
            </el-form-item>
            <el-form-item>
              <el-col :span="8" :offset="20">
                <el-button type="primary" icon="el-icon-plus" @click="addUrl">添加</el-button>
                <el-button @click="resetForm('Form1')">重置</el-button>
              </el-col>
            </el-form-item>
          </el-form>

        </el-row>
      </div>
    </el-card>
    <el-card class="card2">
      <h2>更新url</h2>
      <div style="margin-bottom: 20px">
        <el-row class="search">
          <el-form ref="Form2" :model="ruleForm2" :rules="rules2" label-width="100px" class="demo-ruleForm">
            <el-form-item label="高校名称" prop="organizationName">
              <el-select
                v-model="ruleForm2.organizationName"
                filterable
                reserve-keyword
                placeholder="请输入待更新高校名称"
              >
                <el-option
                  v-for="item in organizationList"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value"
                />
              </el-select>
            </el-form-item>
            <el-form-item label="学院名称" prop="collegeName">
              <el-select v-model="ruleForm2.collegeName" filterable placeholder="请选择待更新院系名称">
                <el-option
                  v-for="item in collegeList2"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value"
                />
              </el-select>
            </el-form-item>
            <el-form-item label="URL" prop="url">
              <el-input v-model="ruleForm2.url" />
            </el-form-item>
            <el-form-item>
              <el-col :span="8" :offset="20">
                <el-button type="primary" icon="el-icon-plus" @click="putUrl">更新</el-button>
                <el-button @click="resetForm('Form2')">重置</el-button>
              </el-col>
            </el-form-item>
          </el-form>

        </el-row>
      </div>
    </el-card>
    <el-card class="card3">
      <h2>高校学院url查询</h2>
      <div style="margin-bottom: 20px">
        <el-row class="search">
          <el-col :span="4">
            <el-select
              v-model="organizationValue3"
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
            <el-select v-model="collegeValue3" filterable placeholder="请选择待查询院系名称">
              <el-option
                v-for="item in collegeList3"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              />
            </el-select>
          </el-col>
          <el-col :span="4">
            <el-button type="primary" icon="el-icon-search" @click="searchUrl">搜索</el-button>
          </el-col>
        </el-row>
      </div>
      <el-table
        :data="tableData3"
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
          prop="url"
          label="学院url"
        />
      </el-table>
    </el-card>
    <el-card class="card4">
      <h2>导出未采集部分</h2>
      <div style="margin-bottom: 20px">
        <el-button type="primary" icon="el-icon-download" @click="download">下载csv</el-button>
      </div>
    </el-card>
  </el-main>
</template>

<script>
import { mapGetters } from 'vuex'
import { getCollegeName, getOrganazationName, getUrl, postUrl, putUrl, exportCsv } from '@/api/urlCRU'

export default {
  name: 'UrlCRU',
  computed: {
    ...mapGetters([
      'token'
    ])
  },
  data() {
    var urlPass = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('url不能为空'))
      }
      callback()
    }
    return {
      ruleForm1: {
        organizationName: '',
        collegeName: '',
        url: ''
      },
      rules1: {
        organizationName: [
          { required: true, message: '请输入高校名称', trigger: 'blur' },
          { min: 4, max: 20, message: '长度在 4 个字符以上', trigger: 'blur' }
        ],
        collegeName: [
          { required: true, message: '请输入学院名称', trigger: 'blur' },
          { min: 4, max: 20, message: '长度在 4 个字符以上', trigger: 'blur' }
        ],
        url: [
          { required: true, trigger: 'blur', validator: urlPass }
        ]

      },
      ruleForm2: {
        organizationName: '',
        collegeName: '',
        url: ''
      },
      rules2: {
        url: [
          { required: true, trigger: 'blur', validator: urlPass }
        ]
      },
      tableData3: [],
      organizationValue3: '',
      organizationList: [], // select框数据
      collegeValue3: '',
      collegeList2: [],
      collegeList3: [], // select框数据
      organizations: [],
      colleges: []
    }
  },
  watch: {
    'ruleForm2.organizationName'(newValue, oldValue) {
      getCollegeName(this.token, newValue).then(response => {
        this.colleges = response['data']
        // console.log(response)
        this.collegeList2 = this.colleges.map(item => {
          return { value: `${item}`, label: `${item}` }
        })
      }).catch()
    },
    organizationValue3(newValue, oldValue) {
      getCollegeName(this.token, newValue).then(response => {
        this.colleges = response['data']
        // console.log(response)
        this.collegeList3 = this.colleges.map(item => {
          return { value: `${item}`, label: `${item}` }
        })
      }).catch()
    }
  },
  mounted() {
    getOrganazationName(this.token).then(response => {
      console.log(response)
      console.log(response['data'])
      this.organizations = response['data']
      // console.log(this.states)
      // console.log(this.value.length)
      this.organizationList = this.organizations.map(item => {
        return { value: `${item}`, label: `${item}` }
      })
      // console.log(this.list)
    }).catch()
  },
  methods: {
    addUrl() {
      this.$refs['Form1'].validate((valid) => {
        if (valid) {
          postUrl(this.token, this.ruleForm1.organizationName, this.ruleForm1.collegeName, this.ruleForm1.url).then(
            this.$message({
              message: '添加成功 ' + this.ruleForm1.organizationName + ' ' + this.ruleForm1.collegeName + ' ' + this.ruleForm1.url,
              type: 'success'
            })
          ).catch()
          getCollegeName(this.token, this.ruleForm2.organizationName).then(response => {
            this.colleges = response['data']
            // console.log(response)
            this.collegeList2 = this.colleges.map(item => {
              return { value: `${item}`, label: `${item}` }
            })
          }).catch()
          getCollegeName(this.token, this.organizationValue3).then(response => {
            this.colleges = response['data']
            // console.log(response)
            this.collegeList3 = this.colleges.map(item => {
              return { value: `${item}`, label: `${item}` }
            })
          }).catch()
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
    putUrl() {
      this.$refs['Form2'].validate((valid) => {
        if (valid) {
          putUrl(this.token, this.ruleForm2.organizationName, this.ruleForm2.collegeName, this.ruleForm2.url).then(
            this.$message({
              message: '修改成功 ' + this.ruleForm2.organizationName + ' ' + this.ruleForm2.collegeName + ' ' + this.ruleForm2.url,
              type: 'success'
            })
          ).catch()
          getCollegeName(this.token, this.ruleForm2.organizationName).then(response => {
            this.colleges = response['data']
            // console.log(response)
            this.collegeList2 = this.colleges.map(item => {
              return { value: `${item}`, label: `${item}` }
            })
          }).catch()
          getCollegeName(this.token, this.organizationValue3).then(response => {
            this.colleges = response['data']
            // console.log(response)
            this.collegeList3 = this.colleges.map(item => {
              return { value: `${item}`, label: `${item}` }
            })
          }).catch()
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
    download() {
      exportCsv(this.token).then(response => {
        console.log(response)
        this.downloadFile(response.data)
      }
      ).catch()
    },
    downloadFile(data) {
      // 文件导出
      if (!data) {
        return
      }
      console.log(data)
      const url = window.URL.createObjectURL(new Blob([data], { type: 'application/vmd.ms-excel' }))
      // const url = window.URL.createObjectURL(blob)
      const link = document.createElement('a')
      link.style.display = 'none'
      link.href = url
      link.setAttribute('download', '未采集部分.csv')

      document.body.appendChild(link)
      link.click()
    },
    resetForm(formName) {
      this.$refs[formName].resetFields()
    },
    uniqueForCard3(obj) {
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
    searchUrl() {
      getUrl(this.token, this.organizationValue3, this.collegeValue3).then(response => {
        // console.log(response)
        this.tableData3.push({
          organizationName: this.organizationValue3,
          collegeName: this.collegeValue3,
          url: response['url']
        })
        this.uniqueForCard3(this.tableData3)
      }).catch()
    }
  }
}
</script>

<style scoped>
.card2 {
  margin-top: 30px;
  margin-bottom: 30px;
}
.card3{
  margin-bottom: 30px;
}
</style>
