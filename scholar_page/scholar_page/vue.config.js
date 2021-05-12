const path = require('path');

module.exports = {
  publicPath:'./',
  assetsDir:'static',
  productionSourceMap:false,
  filenameHashing:false,
  pages: {
    index:{
      entry: 'src/main.js',
      title:''
    }
  },
  lintOnSave: false,
  configureWebpack:{
    resolve:{
      extensions:[],
      alias:{
        img:'@/img',
        common:'@/common',
        pages:'@/pages'
      }
    }
  }

}