<template>
  <div class="index-product">
    <div class="index-product-box">
      <span class="index-product-box-name">科研活跃度Top 10</span>
      <div class="index-product-box-select">
        <el-button-group>
          <el-button type="primary" size="mini">近七天</el-button>
          <el-button size="mini">本月</el-button>
          <el-button size="mini">本年</el-button>
        </el-button-group>
      </div>
      <div class="index-product-box-charts">
        <dv-scroll-ranking-board :config="config" style="width:500px;height:450px; color: red;"/>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      config: {
        data: [
          {
            name: '北京',
            value: 100
          },
          {
            name: '上海',
            value: 90
          },
          {
            name: '广州',
            value: 80
          },
          {
            name: '武汉',
            value: 70
          },
          {
            name: '深圳',
            value: 70
          },
          {
            name: '杭州',
            value: 70
          },
          {
            name: '西安',
            value: 60
          },
          {
            name: '成都',
            value: 50
          },
          {
            name: '福州',
            value: 40
          }
        ],
        unit: '',
        rowNum: 10
      }

    }
  }
}
</script>
<style scoped>
.index-product {
  width: 100%;
  height: auto;
  background: #ffffff;
  border-radius: 5px;
  padding: 15px;
  box-sizing: border-box;
}

.index-product-box {
  width: 100%;
  /* height: 200px; */
  border: 1px solid #E6E6E6;
  position: relative;
  padding: 20px 15px;
  box-sizing: border-box;
}

.index-product-box-name {
  position: absolute;
  width: 100px;
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

.index-product-box-select {
  width: 100%;
  height: 40px;
  /* background: burlywood; */
  display: flex;
  justify-content: flex-end;
  align-items: center;
  margin-bottom: 10px;
}

.index-product-box-charts {
  width: 100%;
  height: 500px;
  /* background: chocolate; */
}
</style>
