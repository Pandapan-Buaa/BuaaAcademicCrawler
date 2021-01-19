import request from '@/utils/request'

export function getOrganazationName(token) {
  return request({
    // url: '/vue-admin-template/user/info',
    url: '/mongo/getOrganization/',
    method: 'get'
    // params: { token }
  })
}

export function getCollegeName(token, organizationName) {
  return request({
    // url: '/vue-admin-template/user/info',
    url: '/mongo/getCollege/',
    method: 'get',
    params: {
      organizationName: organizationName
    }
  })
}

export function searchOrganizationData(token, organizationName, collegeName) {
  return request({
    url: '/mongo/getByName/',
    method: 'get',
    params: {
      organizationName: organizationName,
      collegeName: collegeName
    }
  })
}

export function getAllData(token) {
  return request({
    url: '/mongo/getAll/',
    method: 'get'
  })
}

export function getUrl(token, organizationName, collegeName) {
  return request({
    url: '/mongo/getUrl/',
    method: 'get',
    params: {
      organizationName: organizationName,
      collegeName: collegeName
    }
  })
}
