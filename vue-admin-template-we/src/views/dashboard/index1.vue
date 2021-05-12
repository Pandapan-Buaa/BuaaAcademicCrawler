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
import china from 'highcharts'
import Highcharts from 'highcharts'
import Highmaps from 'highcharts/modules/map'
// 注意，这里的import world from './world'是核心代码，是个啥我将在下面继续介绍
import world from 'highcharts/world'
// 注意：这是API调用方法，千万不要忘记写哦
Highmaps(Highcharts)
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
    drawmap() {
      Highcharts.Map('Map', {
        chart: {
          borderWidth: 1
        },
        colors: ['rgba(19,64,117,0.05)', 'rgba(19,64,117,0.2)', 'rgba(19,64,117,0.4)',
          'rgba(19,64,117,0.5)', 'rgba(19,64,117,0.6)', 'rgba(19,64,117,0.8)', 'rgba(19,64,117,1)'],
        title: {
          text: '世界学者信息地图'
        },
        mapNavigation: {
          enabled: true
        },
        legend: {
          title: {
            text: '发生事件',
            style: {
              color: (Highcharts.theme && Highcharts.theme.textColor) || 'black'
            }
          },
          align: 'left',
          verticalAlign: 'bottom',
          floating: true,
          layout: 'vertical',
          valueDecimals: 0,
          backgroundColor: (Highcharts.theme && Highcharts.theme.legendBackgroundColor) || 'rgba(255, 255, 255, 0.85)',
          symbolRadius: 0,
          symbolHeight: 14
        },
        colorAxis: {
          dataClasses: [{
            to: 3
          }, {
            from: 3,
            to: 10
          }, {
            from: 10,
            to: 30
          }, {
            from: 30,
            to: 100
          }, {
            from: 100,
            to: 300
          }, {
            from: 300,
            to: 1000
          }, {
            from: 1000
          }]
        },
        series: [{
          data: [{
            name: '北京',
            value: 2000,
            rank: 1
          }, {
            name: '上海',
            value: 1500,
            rank: 2
          }],
          mapData: world,
          joinBy: ['iso-a2', 'code'],
          animation: true,
          name: 'Population density',
          states: {
            hover: {
              color: '#BADA55'
            }
          },
          tooltip: {
            valueSuffix: '/km²'
          }
        }]
      })
    }
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
