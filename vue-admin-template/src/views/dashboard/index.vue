<template>
  <div class="index">
    <!-- 销售数据 -->
    <div class="index-sales">
      <div class="index-sales-box">
        <span class="index-sales-box-name">爬取数据统计</span>
        <el-row :gutter="20">
          <Cards colors='#FFA333' name='今日爬取数量' :number='10' ionc='DealSvg'  />
          <Cards colors='#A155E8' name='昨日爬取数量' :number='120' ionc='DealSvg'  />
          <Cards colors='#6D91FF' name='本月爬取数量' :number='1405' ionc='DealSvg'  />
          <Cards colors='#A233A2' name='累计爬取量(年)' :number='110' ionc='DealSvg'  />
        </el-row>
      </div>
    </div>
    <!-- 统计 -->
    <el-row :gutter="20">
      <el-col :xs="24" :sm="24" :md="24" :lg="12" :xl="12" style="margin-bottom: 20px;">
        <Pays />
      </el-col>
      <el-col :xs="24" :sm="24" :md="24" :lg="12" :xl="12" style="margin-bottom: 20px;">
        <Clients />
      </el-col>
      <el-col :xs="24" :sm="24" :md="24" :lg="12" :xl="12" style="margin-bottom: 20px;">
        <Maps />
      </el-col>
      <el-col :xs="24" :sm="24" :md="24" :lg="12" :xl="12" style="margin-bottom: 20px;">
        <Product />
      </el-col>
    </el-row>
  </div>
</template>

<script>
import Cards from '../../components/analyze/cards'
import Pays from '../../components/analyze/pay'
import Clients from '../../components/analyze/client'
import Maps from '../../components/analyze/map'
import Product from '../../components/analyze/product'
import {mapGetters} from 'vuex'
export default {
  components:{
    Cards,
    Pays,
    Clients,
    Maps,
    Product
  },
  name: 'Dashboard',
  computed: {
    ...mapGetters([
      'name'
    ])
  },
  mounted() {
    //this.drawmap()
  },
  methods: {
  }
}
</script>

<style scoped>
.index{
  background: #F5F7F9;
  padding: 15px;
  box-sizing: border-box;
  width: 100%;
  min-height: 100%;
}
.index-sales{
  width: 100%;
  height: auto;
  padding: 20px 15px;
  box-sizing: border-box;
  /* background: brown; */
  /* border:  1px solid #E6E6E6; */
  border-radius: 5px;
  background: #ffffff;
  margin-bottom: 20px;
}
.index-sales-box{
  border:  1px solid #E6E6E6;
  width: 100%;
  height: auto;
  position: relative;
  padding: 25px 15px 5px;
  box-sizing: border-box;

}
.index-sales-box-name{
  position: absolute;
  width: 130px;
  height: 30px;
  background: #ffffff;
  display: inline-block;
  text-align: center;
  line-height: 30px;
  font-size: 13px;
  color: #000000;
  left: 25px;
  top: -15px;
}


</style>
