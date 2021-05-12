<template>
  <el-main>
    <el-col>
      <el-card>
        <el-table
          class="dataTable tb-edit"
          :data="multiIdScholarTableData.slice((currentPage-1)*pageSize,currentPage*pageSize)"
          style="width: 100%"
          highlight-current-row
          @row-click="handleCurrent"
        >
          <el-table-column
            prop="mongoid"
            label="MongoId"
            width="200"
            align="center"
          />
          <el-table-column label="知兔ID" width="200">
            <template scope="scope">
              <el-select v-model="scope.row.zhituid" @focus="getDatalist(scope.row)" placeholder="请选择ID">
                <el-option v-for="item in idList" :key="item.id" :label="item.id" :value="item.id">
                </el-option>
              </el-select>
            </template>
          </el-table-column>
          <el-table-column
            prop="name"
            label="姓名"
            width="100"
            align="center"
          />
          <el-table-column
            prop="organizationName"
            label="所在大学"
            width="100"
            align="center"
          />
          <el-table-column
            prop="collegeName"
            label="所在院系"
            width="100"
            align="center"
          />
          <el-table-column
            prop="website"
            label="学者个人主页"
            width="200"
            align="center"
          />
          <el-table-column
            prop="alljson"
            label="隐藏"
            width="200"
            align="center"
            v-if="show"
          />
          <el-table-column label="重复学者信息" width="600">
          <template scope="scope">
            <el-col v-model="scope.row.json" v-html="scope.row.json">
            </el-col>
          </template>
          </el-table-column>
          <el-table-column label="操作">
            <template scope="scope">
              <el-button type="primary" size="small" @click="handleUpdate(scope.$index, scope.row)">确认ID</el-button>
              <!--              <el-button size="small" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>-->
            </template>
          </el-table-column>
        </el-table>
        <el-pagination
          class="pagination"
          align="center"
          :current-page="currentPage"
          :page-sizes="[1,5,10,20]"
          :page-size="pageSize"
          layout="total, sizes, prev, pager, next, jumper"
          :total="multiIdScholarTableData.length"
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
        />
      </el-card>
    </el-col>
  </el-main>
</template>

<script>
import { mapGetters } from 'vuex'
import { getMultiIdScholars,updateMultiIdScholarById } from '@/api/multiIdScholar'

export default {
  name: 'MultiIdScholar',
  computed: {
    ...mapGetters([
      'name',
      'token'
    ])
  },
  data() {
    return {
      show: false,
      multiIdScholarTableData: [],
      currentPage: 1, // 当前页码
      total: 20, // 总条数
      pageSize: 10, // 每页的数据条数
      idList: []
    }
  },
  mounted() {
    getMultiIdScholars().then(
      response => {
        console.log(response['data'])
        // console.log(response['data'][0]['_id'])
        console.log('total length:' + response['data'].length)
        for (var i = 0; i < response['data'].length; i++) {
          // console.log(response['data'][i]['ids'].split(' '))
          // console.log(i)
          // console.log(response['data'][i])
          console.log(response['data'][i]['json'])
          this.multiIdScholarTableData.push({
            organizationName: response['data'][i]['organizationName'],
            collegeName: response['data'][i]['collegeName'],
            name: response['data'][i]['name'],
            mongoid: response['data'][i]['_id'],
            website: response['data'][i]['website'],
            alljson: response['data'][i]['json'],
            json: this.jsonparse(response['data'][i]['json'])
          })
        }
      }
    ).catch()
  },
  methods: {
    getDatalist(row) {
      var jsonObject = JSON.parse(row.alljson)
      console.log(row.alljson)
      var list = []
      for (var i = 0; i < jsonObject['data'].length; i++) {
        var temp = {}
        temp['id'] = JSON.stringify(jsonObject['data'][i]['id'])
        list.push(temp)
      }
      console.log(list)
      this.idList = list
    },
    jsonparse(json) {
      var jsonObject = JSON.parse(json)
      var res = ''
      console.log('data length:' + jsonObject['data'].length)
      for (var i = 0; i < jsonObject['data'].length; i++) {
        console.log(i)
        res += '知兔id:' + JSON.stringify(jsonObject['data'][i]['id']) + ' '
        res += '性别:' + JSON.stringify(jsonObject['data'][i]['gender']) + ' '
        res += '学校名:' + JSON.stringify(jsonObject['data'][i]['orgName']) + ' '
        res += '院系名:' + JSON.stringify(jsonObject['data'][i]['department']) + ' '
        res += '职称:' + JSON.stringify(jsonObject['data'][i]['title']) + ' '
        res += '学历:' + JSON.stringify(jsonObject['data'][i]['education']) + ' '
        res += '研究方向:' + JSON.stringify(jsonObject['data'][i]['major']) + ' '
        res += '电话:' + JSON.stringify(jsonObject['data'][i]['phone']) + ' '
        res += '邮箱:' + JSON.stringify(jsonObject['data'][i]['email']) + ' '
        res += '</br>'
        res += '</br>'
      }
      console.log(res)
      return res
    },
    handleCurrent(row, event, column) {
      // console.log(row, event, column)
    },
    handleEdit(index, row) {
      // console.log(index, row)
    },
    handleUpdate(index, row) {
      console.log(row)
      var id = row.mongoid
      var zhituId = row.zhituid
      updateMultiIdScholarById(id, zhituId).then(
        this.$message({
          message: '保存成功' + ' mongoid:' + id + ' zhituId:' + zhituId,
          type: 'success'
        })).catch()
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

</style>
