<template>
  <div class="dashboard-container">
    <div class="dashboard-text">学者爬虫系统首页</div>
    <div class="dashboard-text">用户: {{ name }}</div>
    <el-card>
      <div id="Map" style="width:'100%'"/>
    </el-card>
    <div id="myChart" style="{width:'100%',height:'3.54rem'}"/>
  </div>
<!--  <div id="demo-wrapper">-->
<!--    <div id="mapBox">-->
<!--      <div id="up"></div>-->
<!--      <div class="selector">-->
<!--        <button id="btn-prev-map" class="prev-next"><i class="fa fa-angle-left"></i></button>-->
<!--        <select id="mapDropdown" class="ui-widget combobox"></select>-->
<!--        <button id="btn-next-map" class="prev-next"><i class="fa fa-angle-right"></i></button>-->
<!--      </div>-->
<!--      <div id="container"></div>-->
<!--    </div>-->
<!--    <div id="sideBox">-->
<!--      <input type="checkbox" id="chkDataLabels" checked='checked' />-->
<!--      <label for="chkDataLabels" style="display: inline">显示数据标签</label>-->
<!--      <div id="infoBox">-->
<!--        <div id="download"></div>-->
<!--      </div>-->
<!--    </div>-->
<!--  </div>-->
</template>
<script>
import {mapGetters} from 'vuex'
import china from 'highcharts'
import Highcharts from 'highcharts'
import Highmaps from 'highcharts/modules/map'
// 注意，这里的import world from './world'是核心代码，是个啥我将在下面继续介绍
import world from 'highcharts/world'
// 注意：这是API调用方法，千万不要忘记写哦
Highmaps(Highcharts)
// import echarts from 'echarts'
const echarts = require('echarts/lib/echarts')

export default {
  name: 'Dashboard',
  computed: {
    ...mapGetters([
      'name'
    ])
  },
  mounted() {
    this.drawmap()
    this.drawLine()
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

<style lang="scss" scoped>
.dashboard {
  &-container {
    margin: 30px;
  }

  &-text {
    font-size: 30px;
    line-height: 46px;
  }
}
#demo-wrapper {
  max-width: 1000px;
  margin: 0 auto;
  height: 560px;
}
#mapBox {
  width: 80%;
  float: left;
}
#container {
  height: 500px;
}
#sideBox {
  float: right;
  width: 16%;
  margin: 100px 1% 0 1%;
  padding-left: 1%;
  border-left: 1px solid silver;
  display: none;
}
#infoBox {
  margin-top: 10px;
}
.or-view-as {
  margin: 0.5em 0;
}
#up {
  height: 20px;
  max-width: 400px;
  margin: 0 auto;
}
#up a {
  cursor: pointer;
  padding-left: 40px;
}
.selector {
  height: 40px;
  max-width: 400px;
  margin: 0 auto;
  position: relative;
}
.selector .prev-next {
  position: absolute;
  padding: 0 10px;
  font-size: 30px;
  line-height: 20px;
  background: white;
  font-weight: bold;
  color: #999;
  top: -2px;
  display: none;
  border: none;
}
.selector .custom-combobox {
  display: block;
  position: absolute;
  left: 40px;
  right: 110px;
}
.selector .custom-combobox .custom-combobox-input {
  position: absolute;
  font-size: 14px;
  color: silver;
  border-radius: 0;
  height: 24px;
  display: block;
  /*     background: url(http://api.highcharts.com/resources/images/search.png) 5px 5px no-repeat white; */
  padding: 1px 5px 1px 30px;
  width: 100%;
}
.selector .custom-combobox .ui-autocomplete-input:focus {
  color: black;
}
.selector .custom-combobox .ui-autocomplete-input.valid {
  color: black;
}
.selector .custom-combobox-toggle {
  position: absolute;
  display: block;
  right: -78px;
  border-radius: 0;
}
.selector #btn-next-map {
  right: -12px;
}
.ui-autocomplete {
  max-height: 500px;
  overflow: auto;
}
.ui-autocomplete .option-header {
  font-style: italic;
  font-weight: bold;
  margin: 5px 0;
  font-size: 1.2em;
  color: gray;
}
.loading {
  margin-top: 10em;
  text-align: center;
  color: gray;
}
.ui-button-icon-only .ui-button-text {
  height: 26px;
  padding: 0 !important;
  background: white;
}
#infoBox .button {
  border: none;
  border-radius: 3px;
  background: #a4edba;
  padding: 5px;
  color: black;
  text-decoration: none;
  font-size: 12px;
  white-space: nowrap;
  cursor: pointer;
  margin: 0 3px;
  line-height: 30px;
}
@media (max-width: 768px) {
  #demo-wrapper {
    width: auto;
    height: auto;
  }
  #mapBox {
    width: auto;
    float: none;
  }
  #container {
    height: 310px;
  }
  #sideBox {
    float: none;
    width: auto;
    margin-top: 0;
    border-left: none;
    border-top: 1px solid silver;
  }
  /*
  .selector {
  width: 300px;
}
  .selector .custom-combobox .custom-combobox-input {
  width: 190px;
}
  .selector .custom-combobox-toggle {
  left: 226px;
}
  .selector #btn-next-map {
  left: 310px;
}
  */
}

</style>
