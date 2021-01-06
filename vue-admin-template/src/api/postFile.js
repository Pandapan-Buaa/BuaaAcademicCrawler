import request from '@/utils/request'

export function postFile(token) {
  return request({
    // url: '/vue-admin-template/user/info',
    url: '/mongo/file/',
    method: 'post'
    // params: { token }
  })
}
