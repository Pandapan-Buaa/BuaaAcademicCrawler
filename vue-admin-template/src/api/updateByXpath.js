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
