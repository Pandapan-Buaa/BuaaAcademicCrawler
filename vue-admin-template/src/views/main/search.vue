<template>
  <el-main>
    <el-row type="flex" justify="center" class="data">
      <el-col :span="8">
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <span>相关数据</span>
            <!--          <el-button style="float: right; padding: 3px 0" type="text" icon="el-icon-search">操作按钮</el-button>-->
          </div>
          <div v-for="(value, key) in data" :key="key" class="text item">
            {{ key }}:{{ value }}
          </div>
        </el-card>
      </el-col>
    </el-row>
    <el-row class="search">
      <el-col :span="4" :offset="8">
        <el-select
          v-model="value"
          multiple
          filterable
          remote
          reserve-keyword
          placeholder="请输入关键词"
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
      <el-col :span="4" :offset="1">
        <el-button type="primary" icon="el-icon-search" @click="searchOrganazationCount">搜索</el-button>
      </el-col>
    </el-row>
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
      data: {
        数据总数: 0
      },
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
      this.data.数据总数 = response['count']
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
        console.log(i)
        searchOrganizationData(this.token, this.value[i]).then(response => {
          console.log(response)
          this.$set(this.data, this.value[i], response['count'])
          // this.data[this.value[0]] = response['count']
        }).catch(error => {
          // console.log(error.message)
        })
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
