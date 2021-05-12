<template>
  <div id="app">
    <Show />
  </div>
</template>

<script>
import Edit from './pages/Edit.vue'
import Show from './pages/Show.vue'
export default {
  name: 'App',
  components: {
    Edit,
    Show
  }
}
</script>
<style>
body{
  margin:0;
  padding:0;
  font-size:16px;
  color:#333;
  font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
}
.clearfix:after{
  content:'';
  display:block;
  height:0;
  line-height:0;
  overflow:hidden;
  clear:both;
}
.container{
  width:1360px;
  margin:0 auto;
}
</style>