import request from '@/utils/jrequest'
import mrequest from '@/utils/request'

export function loadConfig(name) {
  return request({
    url: '/load_config/',
    method: 'get',
    params: {
      name: name
    }
  })
}
export function loadConfigStatus(name) {
  return request({
    url: '/load_config_status/',
    method: 'get',
    params: {
      name: name
    }
  })
}

export function crawler(name) {
  return request({
    url: '/crawler/',
    method: 'get',
    params: {
      name: name
    }
  })
}
export function crawlerStatus(name) {
  return request({
    url: '/crawler_status/',
    method: 'get',
    params: {
      name: name
    }
  })
}

export function imgCrawler(name) {
  return request({
    url: '/imgCrawler/',
    method: 'get',
    params: {
      name: name
    }
  })
}
export function imgCrawlerStatus(name) {
  return request({
    url: '/imgCrawler_status/',
    method: 'get',
    params: {
      name: name
    }
  })
}
export function detail(name) {
  return request({
    url: '/detail/',
    method: 'get',
    params: {
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
export function detailMatch(name) {
  return request({
    url: '/detail_match/',
    method: 'get',
    params: {
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

export function antiCrawler(name) {
  return request({
    url: '/anti_crawler/',
    method: 'get',
    params: {
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
