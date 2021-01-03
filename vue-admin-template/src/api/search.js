import request from '@/utils/request'

export function getOrganazationName(token) {
  return request({
    // url: '/vue-admin-template/user/info',
    url: '/mongo/getOrganization/',
    method: 'get'
    // params: { token }
  })
}

export function searchOrganizationData(token, name) {
  return request({
    url: '/mongo/getByName/',
    method: 'get',
    params: {
      name: name
    }
  })
}

export function getAllData(token) {
  return request({
    url: '/mongo/getAll/',
    method: 'get'
  })
}
