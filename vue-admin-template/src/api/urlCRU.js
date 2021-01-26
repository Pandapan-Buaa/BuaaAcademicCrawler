import request from '@/utils/request'

export function getOrganazationName(token) {
  return request({
    // url: '/vue-admin-template/user/info',
    url: '/mongo/getOrganization/',
    method: 'get',
    params: { database: 'organization' }
  })
}

export function getCollegeName(token, organizationName) {
  return request({
    // url: '/vue-admin-template/user/info',
    url: '/mongo/getCollege/',
    method: 'get',
    params: {
      database: 'organization',
      organizationName: organizationName
    }
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
export function postUrl(token, organizationName, collegeName, url) {
  return request({
    url: '/mongo/getUrl/',
    method: 'post',
    params: {
      organizationName: organizationName,
      collegeName: collegeName,
      url: url
    }
  })
}
export function putUrl(token, organizationName, collegeName, url) {
  return request({
    url: '/mongo/getUrl/',
    method: 'put',
    params: {
      organizationName: organizationName,
      collegeName: collegeName,
      url: url
    }
  })
}
export function exportCsv(token) {
  return request({
    url: '/mongo/exportCsv/',
    method: 'get',
    responseType: 'blob'
  })
}

