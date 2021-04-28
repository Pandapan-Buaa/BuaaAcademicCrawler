import request from '@/utils/jrequest'
import mrequest from '@/utils/request'
export function detail(organizationName, collegeName, name) {
  return request({
    url: '/detail/',
    method: 'get',
    params: {
      organizationName: organizationName,
      collegeName: collegeName,
      refresh: true,
      name: name
    }
  })
}
export function detailStatus(name) {
  return request({
    url: '/detail_status/',
    method: 'get',
    params: {
      name: name
    }
  })
}
export function detailMatch(organizationName, collegeName, name) {
  return request({
    url: '/detail_match/',
    method: 'get',
    params: {
      organizationName: organizationName,
      collegeName: collegeName,
      refresh: true,
      name: name
    }
  })
}
export function detailMatchStatus(name) {
  return request({
    url: '/detail_match_status/',
    method: 'get',
    params: {
      name: name
    }
  })
}

export function antiCrawler(organizationName, collegeName, name) {
  return request({
    url: '/anti_crawler/',
    method: 'get',
    params: {
      organizationName: organizationName,
      collegeName: collegeName,
      refresh: true,
      name: name
    }
  })
}
export function antiCrawlerStatus(name) {
  return request({
    url: '/anti_crawler_status/',
    method: 'get',
    params: {
      name: name
    }
  })
}

export function updateStatus(name) {
  return request({
    url: '/update_status/',
    method: 'get',
    params: {
      name: name
    }
  })
}

export function getErrors(name) {
  return request({
    url: '/errors/',
    method: 'get',
    params: {
      name: name
    }
  })
}
export function getErrorLog(name) {
  return request({
    url: '/errorlog/',
    method: 'get',
    params: {
      name: name
    }
  })
}

export function updateScholar(id, name, organizationName, collegeName, title, email, phone) {
  return mrequest({
    url: '/mongo/updateScholarById/',
    method: 'post',
    params: {
      id: id,
      name: name,
      organizationName: organizationName,
      collegeName: collegeName,
      title: title,
      email: email,
      phone: phone
    }
  })
}
