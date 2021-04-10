import request from '@/utils/jrequest'
import mrequest from '@/utils/request'
export function detail(organizationName, collegeName) {
  return request({
    url: '/detail/',
    method: 'get',
    params: {
      organizationName: organizationName,
      collegeName: collegeName,
      refresh: true
    }
  })
}
export function detailStatus() {
  return request({
    url: '/detail_status/',
    method: 'get'
  })
}
export function detailMatch(organizationName, collegeName) {
  return request({
    url: '/detail_match/',
    method: 'get',
    params: {
      organizationName: organizationName,
      collegeName: collegeName,
      refresh: true
    }
  })
}
export function detailMatchStatus() {
  return request({
    url: '/detail_match_status/',
    method: 'get'
  })
}

export function antiCrawler(organizationName, collegeName) {
  return request({
    url: '/anti_crawler/',
    method: 'get',
    params: {
      organizationName: organizationName,
      collegeName: collegeName,
      refresh: true
    }
  })
}
export function antiCrawlerStatus() {
  return request({
    url: '/anti_crawler_status/',
    method: 'get'
  })
}

export function updateStatus() {
  return request({
    url: '/update_status/',
    method: 'get'
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
