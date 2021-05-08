import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

/* Layout */
import Layout from '@/layout'

/**
 * Note: sub-menu only appear when route children.length >= 1
 * Detail see: https://panjiachen.github.io/vue-element-admin-site/guide/essentials/router-and-nav.html
 *
 * hidden: true                   if set true, item will not show in the sidebar(default is false)
 * alwaysShow: true               if set true, will always show the root menu
 *                                if not set alwaysShow, when item has more than one children route,
 *                                it will becomes nested mode, otherwise not show the root menu
 * redirect: noRedirect           if set noRedirect will no redirect in the breadcrumb
 * name:'router-name'             the name is used by <keep-alive> (must set!!!)
 * meta : {
    roles: ['admin','editor']    control the page roles (you can set multiple roles)
    title: 'title'               the name show in sidebar and breadcrumb (recommend set)
    icon: 'svg-name'/'el-icon-x' the icon show in the sidebar
    breadcrumb: false            if set false, the item will hidden in breadcrumb(default is true)
    activeMenu: '/example/list'  if set path, the sidebar will highlight the path you set
  }
 */

/**
 * constantRoutes
 * a base page that does not have permission requirements
 * all roles can be accessed
 */
export const constantRoutes = [
  {
    path: '/login',
    component: () => import('@/views/login/index'),
    hidden: true
  },

  {
    path: '/404',
    component: () => import('@/views/404'),
    hidden: true
  },

  {
    path: '/',
    component: Layout,
    redirect: '/dashboard',
    children: [{
      path: 'dashboard',
      name: 'Dashboard',
      component: () => import('@/views/dashboard/index'),
      meta: { title: '首页', icon: 'dashboard' }
    }]
  },
  {
    path: '/',
    component: Layout,
    redirect: '/urlCRU',
    children: [{
      path: 'urlCRU',
      name: 'urlCRU',
      component: () => import('@/views/main/urlCRU'),
      meta: { title: '高校url标准库', icon: 'el-icon-folder-checked' }
    }]
  },
  {
    path: '/',
    component: Layout,
    redirect: '/updateAll',
    children: [{
      path: 'updateAll',
      name: 'updateAll',
      component: () => import('@/views/main/updateAll'),
      meta: { title: '学者详情更新', icon: 'el-icon-refresh' }
    }]
  },
  {
    path: '/',
    component: Layout,
    redirect: '/updateByXpath',
    children: [{
      path: 'updateByXpath',
      name: 'updateByXpath',
      component: () => import('@/views/main/updateByXpath'),
      meta: { title: '学者详情新增', icon: 'el-icon-circle-plus' }
    }]
  },
  {
    path: '/',
    component: Layout,
    redirect: '/updateByOrganization',
    children: [{
      path: 'updateByOrganization',
      name: 'updateByOrganization',
      component: () => import('@/views/main/updateByOrganization'),
      meta: { title: '选择高校更新', icon: 'el-icon-school' }
    }]
  },
  {
    path: '/',
    component: Layout,
    redirect: '/search',
    children: [{
      path: 'search',
      name: 'Search',
      component: () => import('@/views/main/search'),
      meta: { title: '数据统计', icon: 'el-icon-s-data' }
    }]
  },
  {
    path: '/',
    component: Layout,
    redirect: '/charts',
    // meta: {
    //   title: '学者数据分析',
    //   icon: 'el-icon-s-custom'
    // },
    children: [
      {
        path: 'charts',
        component: () => import('@/views/main/scholar'),
        name: 'Charts',
        meta: { title: '学者数据查询', noCache: true, icon: 'el-icon-menu' }
      }
      // ,
      // {
      //   path: 'charts',
      //   component: () => import('@/views/main/charts/charts'),
      //   name: 'Charts',
      //   meta: { title: '学者数据查询', noCache: true, icon: 'el-icon-menu' }
      // },
      // {
      //   path: 'keyboard',
      //   component: () => import('@/views/main/charts/keyboard'),
      //   name: 'KeyboardChart',
      //   meta: { title: 'Keyboard Chart', noCache: true }
      // },
      // {
      //   path: 'line',
      //   component: () => import('@/views/main/charts/line'),
      //   name: 'LineChart',
      //   meta: { title: 'Line Chart', noCache: true }
      // },
      // {
      //   path: 'mix-chart',
      //   component: () => import('@/views/main/charts/mix-chart'),
      //   name: 'MixChart',
      //   meta: { title: 'Mix Chart', noCache: true }
      // }
    ]
  },
  {
    path: '/',
    component: Layout,
    redirect: '/organization',
    // meta: {
    //   title: '学校数据分析',
    //   icon: 'el-icon-s-custom'
    // },
    children: [
      {
        path: 'organization',
        component: () => import('@/views/main/org'),
        name: 'orgCharts',
        meta: { title: '学校数据分析', noCache: true, icon: 'el-icon-s-order' }
      }
    ]
  },
  // 404 page must be placed at the end !!!
  { path: '*', redirect: '/404', hidden: true }
]

const createRouter = () => new Router({
  // mode: 'history', // require service support
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRoutes
})

const router = createRouter()

// Detail see: https://github.com/vuejs/vue-router/issues/1234#issuecomment-357941465
export function resetRouter() {
  const newRouter = createRouter()
  router.matcher = newRouter.matcher // reset router
}

export default router
