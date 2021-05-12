import Vue from 'vue'
import App from './App.vue'

Vue.config.productionTip = false
require('./common/element.js')

new Vue({
  render: h => h(App),
}).$mount('#app')
