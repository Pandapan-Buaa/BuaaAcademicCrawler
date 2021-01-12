import request from '@/utils/jrequest'
export function loadConfig() {
  return request({
    url: '/load_config/',
    method: 'get'
  })
}
export function loadConfigStatus() {
  return request({
    url: '/load_config_status/',
    method: 'get'
  })
}

export function crawler() {
  return request({
    url: '/crawler/',
    method: 'get'
  })
}
export function crawlerStatus() {
  return request({
    url: '/crawler_status/',
    method: 'get'
  })
}

export function imgCrawler() {
  return request({
    url: '/imgCrawler/',
    method: 'get'
  })
}
export function imgCrawlerStatus() {
  return request({
    url: '/imgCrawler_status/',
    method: 'get'
  })
}
export function detail() {
  return request({
    url: '/detail/',
    method: 'get'
  })
}
export function detailStatus() {
  return request({
    url: '/detail_status/',
    method: 'get'
  })
}
export function detailMatch() {
  return request({
    url: '/detail_match/',
    method: 'get'
  })
}
export function detailMatchStatus() {
  return request({
    url: '/detail_match_status/',
    method: 'get'
  })
}
