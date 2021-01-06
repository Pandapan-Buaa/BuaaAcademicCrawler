<template>
  <el-main>
    <div style="margin-bottom: 20px">
      <el-row class="search">
        <el-col :span="4" >
          <el-select
            v-model="value"
            multiple
            filterable
            remote
            reserve-keyword
            placeholder="请输入待查询高校名称"
            :remote-method="remoteMethod"
            :loading="loading"
          >
            <el-option
              v-for="item in options"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            />
          </el-select>

        </el-col>
        <el-col :span="4">
          <el-button type="primary" icon="el-icon-search" @click="searchOrganazationCount">搜索</el-button>
        </el-col>
      </el-row>
    </div>
    <el-table
      :data="tableData"
      stripe
      style="width: 100%"
    >
      <el-table-column
        prop="name"
        label="查询名称"
        width="180"
      />
      <el-table-column
        prop="count"
        label="已爬取数量"
      />
    </el-table>

  </el-main>
</template>

<script>
import { getOrganazationName, searchOrganizationData, getAllData } from '@/api/search'
import { mapGetters } from 'vuex'

export default {
  computed: {
    ...mapGetters([
      'token'
    ])
  },
  data() {
    return {
      tableData: [{
        name: '数据总数',
        count: 0
      }],
      options: [],
      value: [],
      list: [],
      loading: false,
      states: []
    }
  },
  mounted() {
    getOrganazationName(this.token).then(response => {
      // console.log(response)
      // console.log(response['data'])
      this.states = response['data']
      // console.log(this.states)
      this.list = this.states.map(item => {
        return { value: `${item}`, label: `${item}` }
      })
      // console.log(this.list)
    }).catch(error => {
      console.log(error.message)
    })

    getAllData(this.token).then(response => {
      this.tableData[0].count = response['count']
    }).catch(error => {
    })
  },
  methods: {
    remoteMethod(query) {
      if (query !== '') {
        this.loading = true
        setTimeout(() => {
          this.loading = false
          this.options = this.list.filter(item => {
            return item.label.toLowerCase()
              .indexOf(query.toLowerCase()) > -1
          })
        }, 200)
      } else {
        this.options = []
      }
    },
    searchOrganazationCount() {
      for (let i = 0; i < this.value.length; i++) {
        searchOrganizationData(this.token, this.value[i]).then(response => {
          this.tableData.push({ name: this.value[i], count: response['count'] })
          this.unique(this.tableData)
        }).catch(error => {
          // console.log(error.message)
        })
      }
    },
    unique(obj) {
      // 去掉重复选取的数据
      for (var i = 0; i < obj.length; i++) {
        for (var j = i + 1; j < obj.length;) {
          if (obj[i].name === obj[j].name) { // 通过photoid属性进行匹配；
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
.data {
  margin-bottom:50px;
}
.text {
  font-size: 14px;
}

.item {
  margin-bottom: 18px;
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
  width: 480px;
}
</style>
